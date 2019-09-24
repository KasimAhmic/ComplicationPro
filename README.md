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
4. Open the Complicated app on your phone and under the settings screen, take note of the API Key.
5. Open [OctoPrint](http://octopi.local).
6. Navigate to Settings > ComplicationPro.
7. Insert the Complicated API Key into the appropriate text box.
8. Insert the OctoPrint API Key into the appropriate text box.
9. Under Complication Text, enter the values you'd like to see for each Complication type you'd like to use. Leave blank if you don't want to use it.

## Options
Currently, ComplicationPro supports 5 tracking tokens.

| Token             | Description                                 | Value Example    | API Location (from api/job/)   |
| ----------------- | ------------------------------------------- | ---------------- | ------------------------------ |
| `{progress}`      | Print progress in percentage form           | "18.26"          | `progress.completion`          |
| `{timeElapsed}`   | How long the print has been going for       | "01:25:37"       | `progress.printTime`           |
| `{timeRemaining}` | How much longer until the print is complete | "00:12:23"       | `progress.printTimeLeft`       |
| `{fileName}`      | Current prints file name                    | "keychain.gcode" | `job.file.name`                |
| `{state}`         | Current printer state                       | "Operational"    | `state`                        |

## In Progress
This plugin is far from finished at this point. I'd like to add more statistics and will research how to do that shortly. The following are features that I'd like to add:
- Tracking filament used
- Tracking multiple printers' progress. See [#1](https://github.com/frenchie4111/complicated-octoprint/issues/1)

## Limitations
Currently, the plugin only updates when the progress of the print is incremented by 1%. It works fine for shorter prints where the percentage is quickly updated but can be somewhat unbearable for excessively long print jobs. Since it takes longer to increment an entire 1%, it takes longer to update any and all of the remaining data. Ideally I'd like the percentage, elapsed time, and remaining time updates to be independent of one another but I have yet to find a way to do that.

That said, it's probably for the best. According to Mike Lyons, Apple only lets you update complications about 15 time per hour; anything above that and you're likely to get rate limited. That gives us a theoretical shortest print time of 6 hours and 40 minutes without having to deal with rate limitation.

For the time being, I'm going to deem that good enough and focus on more pressing matters like adding more print stat trackers to the plugin. I'll still happy to hear out any suggestions if you have them!

## Credits
- This plugin was inspired by [Mike Lyons](https://mikelyons.org/)' [complicated-octoprint](https://github.com/frenchie4111/complicated-octoprint) plugin. After using it I felt the functionality a bit lacking so I decided to take a crack at improving upon that.
- This plugin utilizes [Mike Lyons](https://mikelyons.org/)'s [Complicated API](https://mikelyons.org/complicated/) and accompanying app.