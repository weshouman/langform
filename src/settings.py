from dotmap import DotMap

# from models.Language import PYTHON
from models.Language import Language
VERBOSE = False

# classXMLDir has more precedence over classXML
classXMLDir = r'/home/walid/shared_on_wifi/xml/'
# classXMLDir = None

# use to debug enters in the detailedDescription
# classXML = r'/home/walid/shared_on_wifi/xml/classAbstractHistory.xml'
classXML = r'/home/walid/shared_on_wifi/classEntry.xml'

OUTPUT_DIR = "generated/"

# HINT: keep empty if both are the same
# OLD_SOURCE_DIR is the original source used for Doxigen xml generation
OLD_SOURCE_DIR = "/home/walid/Documents/tests/tagaini/tagainijisho_doc_py3/"

# NEW_SOURCE_DIR is the current source
NEW_SOURCE_DIR = "/home/walid/Documents/tagainijisho/master/"

# language we generate to
OUTPUT_LANGUAGE = Language.PYTHON

debug_dict = {
"DISPLAY_UNMATCHING_TYPES" : False
}

# now DEBUG.key could be used directly
DEBUG = DotMap(debug_dict)
