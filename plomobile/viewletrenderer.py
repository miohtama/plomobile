from Acquisition import aq_inner
import zope.interface

from plone.app.customerize import registration

from Products.Five.browser import BrowserView


from zope.traversing.interfaces import ITraversable
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.viewlet.interfaces import IViewlet
from zExceptions import NotFound


class Viewlets(BrowserView):
    """ Expose arbitary viewlets to traversing by name.

    Exposes viewlets to templates by names.

    Example how to render plone.logo viewlet in arbitary template code point::

        <div tal:content="context/@@viewlets/plone.logo" />

    """
    zope.interface.implements(ITraversable)

    def getViewletByName(self, name):
        """ Viewlets allow through-the-web customizations.

        Through-the-web customization magic is managed by five.customerize.
        We need to think of this when looking up viewlets.

        @return: Viewlet registration object
        """
        views = registration.getViews(IBrowserRequest)

        for v in views:

            if v.provided == IViewlet:
                # Note that we might have conflicting BrowserView with the same name,
                # thus we need to check for provided
                if v.name == name:
                    return v

        return None

    def setupViewletByName(self, name):
        """ Constructs a viewlet instance by its name.

        Viewlet update() and render() method are not called.

        @return: Viewlet instance of None if viewlet with name does not exist
        """
        context = aq_inner(self.context)
        request = self.request

        # Perform viewlet regisration look-up
        # from adapters registry
        reg = self.getViewletByName(name)
        if reg == None:
            return None

        # factory method is responsible for creating the viewlet instance
        factory = reg.factory

        # Create viewlet and put it to the acquisition chain
        # Viewlet need initialization parameters: context, request, view
        try:
            viewlet = factory(context, request, self, None).__of__(context)
        except TypeError:
            # Bad constructor call parameters
            raise RuntimeError("Unable to initialize viewlet %s. Factory method %s call failed." % (name, str(factory)))

        return viewlet

    def traverse(self, name, further_path=None):
        """
        Allow travering intoviewlets by viewlet name.

        @return: Viewlet HTML output

        @raise: RuntimeError if viewlet is not found
        """

        viewlet = self.setupViewletByName(name)
        if viewlet is None:
            raise NotFound("Viewlet does not exist by name %s for theme layer" % name)

        viewlet.update()
        return viewlet.render()