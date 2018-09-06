import re
import settings

from models.Language import Language

CPPToPythonTypeDefaultMap =	{
  ".*int.*": "0",
  ".*Set.*": "[]",
  ".*List.*": "[]",
  ".*String": "\"\"",
  ".*DateTime": "datetime.min"
}

# TODO: move to respective class
def get_python_type_default(language, param_type):
	if language == Language.CPP:
		ptdMap = CPPToPythonTypeDefaultMap
	else:
		# input language to python mapping isn't defined
		return "None"

	returnString = "None"
	keyMatched = False
	for key, value in ptdMap.iteritems():   # iter on both keys and values
		p = re.compile(key)
		if p.match(param_type) != None:
			keyMatched = True
			returnString = value
			break

	if keyMatched == False:
		if settings.DEBUG.DISPLAY_UNMATCHING_TYPES:
			print "No default value for type: " + param_type

	return returnString

