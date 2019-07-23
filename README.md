# ComplicationPro

ComplicationPro is an OctoPrint plugin that allows you to send a large variety of print statistics to your Apple Watch.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/KasimAhmic/ComplicationPro/archive/master.zip


## Configuration

1. Download and install the [Complicated](https://apps.apple.com/us/app/complicated/id1444561091) app on your iPhone.
2. Run through the setup.
3. Open your Watch app and install the Complicated complication.
4. Open the Complicated app on your phne and under the settings screen, take not of the API Key.
5. Open [OctoPrint](http://octopi.local).
6. Naviaget to Settings > ComplicationPro.
7. Insert the API Key into the appropriate text box.
8. Under Complication Text, enter the values you'd like to see for each Complication type you'd like to use. Leave blank if you don't want to use it.

## In Progress
This plugin is far from finished at this point. I'd like to add more statistics and will research how to do that shortly. The following are features that I'd like to add:
- Tracking time elapsed
- Tracking time remaining
- Tracking filament used
- Tracking multiple printers' progress. See [#1](https://github.com/frenchie4111/complicated-octoprint/issues/1)

## Credits
- This plugin was inspired by [Mike Lyons](https://mikelyons.org/)' [complicated-octoprint](https://github.com/frenchie4111/complicated-octoprint) plugin. After using it I felt the functionality a bit lacking so I decided to take a crack at improving upon that.
- This plugin utilizes [Mike Lyons](https://mikelyons.org/)'s [Complicated API](https://mikelyons.org/complicated/) and accompanying app.