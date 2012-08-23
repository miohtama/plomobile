.. contents ::

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

Supported add-on tweaks
-------------------------

The mobile.css contains fixes for popular Plone add-ons, including

* Content well portlets

* Products.Carousel

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


History
-----------

This add-on replaces old Web and Mobile add-on

* Plomobile is much more lightweight and maintanable solution due to its
  relying on client-side (Javascript) tricks

* Plomobile plays nicely with Diazo

* All old features of Web and Mobile not supported (different content for different devices)

* Plomobile works on thin-client browsers which support minial on page init Javascript execution
  (Opera Mini)