# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import complicated
from urllib2 import Request, urlopen
import json

class ComplicationProPlugin(octoprint.plugin.ProgressPlugin,
							octoprint.plugin.SettingsPlugin,
							octoprint.plugin.TemplatePlugin,
							octoprint.plugin.AssetPlugin,
							octoprint.plugin.SimpleApiPlugin):
	def get_settings_defaults(self):
		# Return default settings
		return dict(
    		apiKey = 'Put your API Key here',
			octoprintUrl = '',
    		circularSmall = '',
    		extraLarge = '',
    		graphicBezel = '',
    		graphicCircular = '',
    		graphicCorner = '',
    		graphicRectangular = '',
    		modularLarge = '',
    		modularSmall = '',
    		utilitarianLarge = '',
    		utilitarianSmall = '',
    		utilitarianSmallFlat = ''
       	)

	def get_template_configs(self):
		return [
        	dict(type = "settings", custom_bindings = False)
		]

	def get_assets(self):
		# Inlcude JavaScript file used to return the Octoprint URL
		return dict(
			js=["js/geturl.js"]
		)

	def get_api_commands(self):
		# Return a simple API command and it's required variable
		return dict(
			getURL = ["url"]
		)

	def on_api_command(self, command, data):
		# Log Octoprint's URL
		self._logger.info("OctoPrint URL: " + str(data["url"]["origin"]))
		# Update ComplicationPro's settings to use the returned URL
		self._settings.set(["octoprintUrl"], str(data["url"]["origin"]))

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			complicationpro = dict(
				displayName = "ComplicationPro",
				displayVersion = self._plugin_version,

				# version check: github repository
				type = "github_release",
				user = "KasimAhmic",
				repo = "ComplicationPro",
				current = self._plugin_version,

				# update method: pip
				pip = "https://github.com/KasimAhmic/ComplicationPro/archive/{target_version}.zip"
			)
		)
	
	def on_print_progress(self, storage, path, progress):
		# Retrieve values for API keys and the Octoprint URL
		apiKey = self._settings.get(["apiKey"])
		octoprintUrl = self._settings.get(["octoprintUrl"])
		octoprintApiKey = self._settings.get(["octoprintApiKey"])

		# Create a list of available complication types
		complications = [
    		"circularSmall",
    		"extraLarge",
    		"graphicBezel",
    		"graphicRectangular",
    		"graphicCircular",
    		"graphicCorner",
    		"modularLarge",
    		"modularSmall",
    		"utilitarianLarge",
    		"utilitarianSmall",
    		"utilitarianSmallFlat"
		]

		# Send a GET request to the Octoprint API to retrieve print job information
		req = Request(octoprintUrl + "/api/job")
		req.add_header("Content-Type", "application/json")
		req.add_header("X-Api-Key", octoprintApiKey)
		# Read returned data as JSON
		data = json.loads(urlopen(req).read())

		# Iterate over list of complications
		for complication in complications:\
			# If complication text was configured in the settings...
			if self._settings.get([complication]) != "":
				# Replace the tokens in the strings with their accompanying print job values
				value = self._settings.get([complication])
				value = value.replace("{progress}", str(round(data["progress"]["completion"], 2)))
				value = value.replace("{timeRemaining}", self.convert_seconds(data["progress"]["printTimeLeft"]))
				value = value.replace("{timeElapsed}", self.convert_seconds(data["progress"]["printTime"]))
				value = value.replace("{fileName}", str(data["file"]["name"]))
				value = value.replace("{state}", str(data["state"]))

				# Submit the change to the Complicated API
				complicated.changeComplication(apiKey, complication, value)
	
	def convert_seconds(self, time):
		hours = time // 3600
		time %= 3600
		minutes = time // 60
		time %= 60
		seconds = time
		return "%02d:%02d:%02d" % (hours, minutes, seconds)

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "ComplicationPro"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ComplicationProPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
