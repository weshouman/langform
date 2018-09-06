import datetime
from jinja2 import Environment, FileSystemLoader

# TODO: support the following structure if seen better
# def print_to_template(outputFile, inputFile):

def print_to_template_simple(outputFile, presenter):
	"""
	simplest template example, an extandable function for starting new languages
	"""
	file_loader = FileSystemLoader('src/templates')
	env = Environment(loader=file_loader)

	template = env.get_template('classy.py.tmpl')

	template.globals['now'] = datetime.datetime.utcnow

	output = template.render(presenter=presenter)

	with open(outputFile, 'wb') as pyfile:
		pyfile.write(output.encode('utf-8'))

	return

def print_to_template(outputFile, presenter):
	file_loader = FileSystemLoader('src/templates')


	env = Environment(
		loader=file_loader,
		keep_trailing_newline=True,  # newline-terminate generated files
		lstrip_blocks=True,  # so can indent control flow tags
		trim_blocks=True)  # so don't need {%- -%} everywhere

	template = env.get_template('classy2.py.tmpl')

	template.globals['now'] = datetime.datetime.utcnow

	output = template.render(presenter=presenter)

	with open(outputFile, 'wb') as pyfile:
		pyfile.write(output.encode('utf-8'))

	return
