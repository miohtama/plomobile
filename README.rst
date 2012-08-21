.. contents :: local:

Introduction
-------------

Plomobile is a modern mobile site solution for Plone. It focuses on delivering
good accetable user experience for read-only site access on most mobile phones.

Responsive on steroids
--------------------------

Differences over normal responsive themes, e.g. Plone's default Sunburst theme,
include UI tweaks which optimize the layout more for mobile

* Menu button replaces portal tabs

* Search button - search hidden by default

* Turn lists to mobile friendly tile links

* Suffling UI elements around for more sane mobile layout

Supported fixes
-----------------

The mobile.css contains fixes for popular Plone add-ons, including

* Content well portlets

* Products.Carousel

Custom mobilization Javascript
--------------------------------

You probably want to adjust Javascript fixes for your custom site theme.

This can be done by overriding ``windows.mobilize()`` function from
your Javascript code. Just code the existing ``mobilize()`` from ``mobile.js``
and add in your site specific logic.

History
-----------

This add-on replaces old Web and Mobile add-on

* Plomobile is much more lightweight and maintanable solution due to its
  relying on client-side (Javascript) tricks

* Plomobile plays nicely with Diazo

* All old features of Web and Mobile not supported (different content for different devices)

* Plomobile works on thin-client browsers which support minial on page init Javascript execution
  (Opera Mini)