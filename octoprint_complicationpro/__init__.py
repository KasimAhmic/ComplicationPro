# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import complicated
import urllib

class ComplicationProPlugin(octoprint.plugin.ProgressPlugin, octoprint.plugin.SettingsPlugin, octoprint.plugin.TemplatePlugin):
	def get_settings_defaults(self):
		return dict(
    		apiKey = 'Put your API Key here',
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
	
	def on_print_progress(self, storage, path, progress ):
		apiKey = self._settings.get(['apiKey'])
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
		for complication in complications:
			if self._settings.get([complication]) != "":
				value = self._settings.get([complication]).replace("{progress}", str(progress))
				complicated.changeComplication(apiKey, complication, value)

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
