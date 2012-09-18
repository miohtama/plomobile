"""

    For more information see

    * http://collective-docs.readthedocs.org/en/latest/views/viewlets.html

"""

# Zope imports
from zope.interface import Interface
from zope.component import getMultiAdapter
from five import grok

# Plone imports
from plone.app.layout.viewlets.interfaces import IPortalFooter
from plone.app.layout.viewlets.interfaces import IPortalHeader

# Local imports
from interfaces import IAddonSpecific

from .viewletrenderer import Viewlets

grok.templatedir("templates")
grok.layer(IAddonSpecific)

# By default, set context to zope.interface.Interface
# which matches all the content items.
# You can register viewlets to be content item type specific
# by overriding grok.context() on class body level
grok.context(Interface)


class MobileUIHeader(grok.Viewlet):
    """
    Contains HTML payload for rendering mobile menus and such.

    This is supplement for mobile.js - inline HTML in JS is always ugly.
    """
    grok.viewletmanager(IPortalHeader)
    grok.template("mobile-ui-header")


class MobileUIFooter(grok.Viewlet):
    """
    Contains HTML payload for rendering mobile menus and such.

    This is supplement for mobile.js - inline HTML in JS is always ugly.
    """
    grok.viewletmanager(IPortalFooter)
    grok.template("mobile-ui-footer")

    def update(self):
        """
        Get mobile quick links.
        """

        context_state = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        self.quick_links = context_state.actions("mobile_quick_links")  # id -> action mappings
        self.quick_links = [ql for ql in self.quick_links if ql["visible"] == True]

    def getMenuCSSClass(self):
        classes = "mobile-slide"
        if self.hasQuickLinks():
            classes += " mobile-slide-quick-links"
        return classes

    def hasQuickLinks(self):
        """
        """
        return self.quick_links

    def renderSectionsListElements(self):
        """
        We need to pull some magic here because section rendering code
        might have been customized...
        """
        context = self.context.aq_inner
        viewlets = Viewlets(context, self.request)
        sections = viewlets.traverse("plone.global_sections")

        # XXX: Get a smarter way to handle this
        sections = sections.replace('<ul id="portal-globalnav">', '')
        sections = sections.replace('</ul>', '')

        return sections

    def renderSearchBox(self):
        """
        Get mobile version of the site search box.
        """
        context = self.context.aq_inner
        viewlets = Viewlets(context, self.request)
        searchBox = viewlets.traverse("plone.searchbox")
        searchBox = searchBox.replace("portal-searchbox", "portal-searchbox-mobile")
        return searchBox
