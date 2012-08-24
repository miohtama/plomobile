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

grok.templatedir("templates")
grok.layer(IAddonSpecific)

# By default, set context to zope.interface.Interface
# which matches all the content items.
# You can register viewlets to be content item type specific
# by overriding grok.context() on class body level
grok.context(Interface)


class MobileUI(grok.Viewlet):
    """
    Contains HTML payload for rendering mobile menus and such.

    This is supplement for mobile.js - inline HTML in JS is always ugly.
    """
    grok.viewletmanager(IPortalHeader)

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
