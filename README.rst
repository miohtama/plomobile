.. contents ::

Goals and usage
=================

Introduction
-------------

Plomobile is a modern mobile site solution for Plone. It focuses on delivering
good accetable user experience for read-only site access on most mobile phones.

Design goals
--------------

* Mobile browsers get mobile optimized and mobile specific buttons for better user experience

* Desktop and tablets can use desktop version as is

* Depends on jQuery for DOM manipulation

* Server-side changes kept minimal: serve the same HTML payload regardless of the HTTP user agent and thus
  make static caching and CDN easy

Responsivity on steroids
--------------------------

Differences over normal responsive themes, e.g. Plone's default Sunburst theme,
include UI tweaks which optimize the layout more for mobile. These
tweaks cannot be achieved with CSS tuning alone.

* Menu button replaces portal tabs

* Search button - search hidden by default

* Turn lists to mobile friendly tile links

* Suffling UI elements around for more sane mobile layout


Tweaking
============

Supported add-on tweaks
-------------------------

The mobile.css has out of the box support tweaks for popular Plone add-ons, including

* Content well portlets

* Products.Carousel

Expect this list to grow in the future.

Mobile menus
-------------------------

By default, the mobile header of the site has three pull down lists

* Sections (same as portal tabs)

* Quick links (custom portal_actions in ZMI you can populate)

* Search

Quick links is a hand-built menu for mobile shortcuts
you need to create yourself in portal_actions.

Customizing mobile CSS
-------------------------

Override the default Plomobile CSS styles by using a
``cssregistry.xml`` entry similar to one below::

   <stylesheet
      id="++resource++yourtheme/mobile.css"
      media="screen and (max-width: 900px)" rel="stylesheet" rendering="import"
      cacheable="True" compression="safe" cookable="True"
      enabled="1" expression="" />


Custom mobilization Javascript
--------------------------------

Plomobile runs a client-side UI patching Javascript
when the browser window is shrinked to mobile dimensions,
or on the page open, if you have small enough screen to the begin with.

You probably want to adjust Javascript fixes for your custom site theme.
Plomobile provides two jQuery events which both take ``mobilize``
object as the argument besides the event itself.

* mobilizestart - allows you to override the whole process

* mobilizeend - listen for this to run custom mobilization JS besides
  the orignal Plomobile mobile.js

Example::

    /**
     * Custom theme cliet side tune ups - when CSS is not enough
     */

    /*global window, document, console*/

    (function($) {
        "use strict";

        // Run custom mobile UI tweaks
        $(document).bind("mobilizeend", function(event, mobilize) {

            // Convert site custom layouts to mobile friendly UI

            // Convert product listings items to tile links
            mobilize.applyTileLinks(".summary-info");
        });

    })(jQuery);


Then register your Javascript as::


    <object name="portal_javascripts">

        <!-- Make sure our custom JS event handlers are installed before we run mobilize bootsrap -->
        <javascript
            id="++resource++yourtheme/mobile.js"
            cacheable="True" compression="safe" cookable="True"
            enabled="True" expression=""  inline="False" insert-before="++resource++plomobile/mobile.js"/>

    </object>

Conditionally loading Facebook and other external Javascripts
-----------------------------------------------------------------

Here is an example how to making a Facebook Like Box has been
made conditionally, so that mobile clients do not load craploads
of Facebook resources for nothing.

Add the following to a static text portlet in Plone::

    <div class="fb-like-box" data-href="https://www.facebook.com/pages/xxx/yyy" data-width="292" data-height="337" data-show-faces="false" data-stream="true" data-header="false"></div>

    <div id="fb-root"></div>
    <script>(function(d, s, id) {
      if(!window.mobilize.isMobile()) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/fi_FI/all.js#xfbml=1";
        fjs.parentNode.insertBefore(js, fjs);
      }
    }(document, 'script', 'facebook-jssdk'));</script>


Other
=======

History
-----------

This add-on replaces old Web and Mobile add-on

* Plomobile is much more lightweight and maintainable solution due to its
  relying on client-side (Javascript) tricks

* Plomobile plays nicely with Diazo

* All old features of Web and Mobile not supported (different content for different devices)

* Plomobile works on thin-client browsers which support minimal on page init Javascript execution
  (Opera Mini)