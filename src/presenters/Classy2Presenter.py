import re
from presenters.ClassyPresenter import ClassyPresenter
from models.pyt import PythonTypeDefault as ptd
from models.Language import Language

class Classy2Presenter(ClassyPresenter):

	def __init__(self, cl):
		super(Classy2Presenter, self).__init__(cl)
		self.initVariableNamesWithCommas = self.get_init_variable_names_with_commas()

	# TODO: skip generating constructors
	def get_init_variable_names_with_commas(self):
		# TODO: change to variable names=type, in example entry=None

		returnString = "self"

		# Add class attributes
		attributesWithCommas = self.get_attributes_with_commas()
		if attributesWithCommas != "":
			returnString += ", "

		returnString += attributesWithCommas

		# Add constructor variables
		constructorVariableNamesWithCommas = self.cl.get_constructor_variable_names_with_commas()

		if (constructorVariableNamesWithCommas != ""):
			returnString += ", "

		returnString += constructorVariableNamesWithCommas

		return returnString

	def get_attributes_with_commas(self):
		"""
		 Note: we start with a comma
		"""
		variables = self.variables()
		memberNamesEqTypes = list(map(lambda x: x.name+"="+ ptd.get_python_type_default(Language.CPP, x.type), variables))
		returnString = ", ".join(memberNamesEqTypes)
		return returnString

