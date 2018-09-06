import sys

sys.path.append('./src')

# import presenters
from presenters.ClassyPresenter import ClassyPresenter
from presenters.Classy2Presenter import Classy2Presenter

# import languages
from models.Language import Language

import creator
import template_process
import settings

def main():
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
