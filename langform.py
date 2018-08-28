import sys

sys.path.append('./src')

from presenters.ClassyPresenter import ClassyPresenter
import creator
import template_process
import settings

def main():
	# parse doxygen class xml
	[classList] = creator.create()

	# Start Jinja for the parsed class

	for cl in classList:
		presenter = ClassyPresenter(cl)

		template_process.print_to_template(settings.OUTPUT_DIR + cl.name + ".py", presenter)

if __name__ == '__main__':
	main()
