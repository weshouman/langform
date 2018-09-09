
# use simplejson to ease debugging
import simplejson as sjson
from dotmap import DotMap

import settings

import lib.interpc as interpc

def modify_settings_by_gui():

	socket = interpc.open_and_get_socket()

	msg = socket.recv()

	if settings.VERBOSE:
		print "Received message is: " + msg

	# parse json
	parsedMsg = sjson.loads(msg)

	if settings.VERBOSE:
		print "Parsed message is: " + parsedMsg

	parsedMsgMap = DotMap(parsedMsg)
	parsedSettings = parsedMsgMap.settings

	# get the different settings and overwrite the settings with it
	for parsedSetting, value in parsedSettings.iteritems():
		if parsedSetting in dir(settings):
			# TODO: instead of dir-ing a class' attributes.
			#       make all the settings in a dictionary.
			#       and use ```if parsedSetting in settings:``` directly
			settings.classXMLDir = parsedSettings.classXMLDir
			result = 'Value of {0} is set to {1}!'.format(parsedSetting, settings.classXMLDir)
			print result
			socket.send(result)

	socket.close()

	settings.DEBUG.DISPLAY_UNMATCHING_TYPES = True