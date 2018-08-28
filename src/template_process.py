import datetime
from jinja2 import Environment, FileSystemLoader

# TODO: support the following structure if seen better
# def print_to_template(outputFile, inputFile):

def print_to_template(outputFile, presenter):
	file_loader = FileSystemLoader('src/templates')
	env = Environment(loader=file_loader)

	template = env.get_template('classy.py.tmpl')

	template.globals['now'] = datetime.datetime.utcnow

	output = template.render(presenter=presenter)

	with open(outputFile, 'wb') as pyfile:
		pyfile.write(output.encode('utf-8'))

	return
