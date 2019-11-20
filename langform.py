import sys
import argparse

sys.path.append('./src')

# Presenters
from presenters.ClassyPresenter import ClassyPresenter
from presenters.Classy2Presenter import Classy2Presenter

# Languages
from lib.Language import Language

# Conversion for arguments
import common.conversion as conv

import creator
import template_process

import settings
import gui.gui_settings as gsettings

def get_args():
	# Set defaults
	IS_GUI_DEFAULT			= False

	# Handle different args
	parser = argparse.ArgumentParser(prog='langform')
	parser.add_argument('--gui', dest='isGUI', default=IS_GUI_DEFAULT, type=conv.str2bool)
	args = parser.parse_args()

	return args

def main():
	# Get arguments
	args = get_args()

	if args.isGUI is True:
		print("--------------")
		# allow overwrite of parameters by zmq
		gsettings.modify_settings_by_gui()

	# parse doxygen class xml
	[classList] = creator.create()

	# Start Jinja for the parsed class
	for cl in classList:
		# TODO: after knowing the best conventions for templating,
		# 		IF POSSIBLE, unify it and move template printing out of the switch for languages

		lang = settings.OUTPUT_LANGUAGE

		if (lang == Language.PYTHON_SIMPLE):
			presenter = ClassyPresenter(cl)
			template_process.print_to_template_simple(settings.OUTPUT_DIR + cl.name + ".py", presenter)

		elif (lang == Language.PYTHON):
			presenter = Classy2Presenter(cl)
			template_process.print_to_template(settings.OUTPUT_DIR + cl.name + ".py", presenter)

if __name__ == '__main__':
	main()
