import re
from presenters.ClassyPresenter import ClassyPresenter
from models.pyt import PythonTypeDefault as ptd
from lib.Language import Language

class Classy2Presenter(ClassyPresenter):

	def __init__(self, cl):
		super(Classy2Presenter, self).__init__(cl)
		self.initVariableNamesWithCommas = self.get_init_variable_names_with_commas()
		self.generateConstructors = False
		self.generateOriginalImplementation = True

	def exists_constructor_params(self):
		constructors = filter(lambda x: (x.isConstructor == True and x.isCopyConstructor == False), self.cl.functions)

		for constructor in constructors:
			if len(constructor.params) > 0:
				return True

		return False

	def get_constructor_params(self):
		constructors = filter(lambda x: (x.isConstructor == True and x.isCopyConstructor == False), self.cl.functions)

		constructorParamList = []
		for constructor in constructors:
			for param in constructor.params:
				constructorParamList.append(str(param.name) + ":"+ str(param.type))

		# use set to remove duplicates if found
		return "# Constructor Params[name:type]: [" + ", ".join(set(constructorParamList)) +"]"

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

	def get_static_decoration(self, function):
		returnString = ""
		returnStringHeader = "\n    "
		returnStringFooter = "\n"

		if function.static == "yes":
			returnString += "@staticmethod"

		if returnString is not "":
			returnString = returnStringHeader + returnString + returnStringFooter

		return returnString

	def get_function_description(self, fn):
		returnString = ""
		returnStringHeader = "        \"\"\"\n"
		returnStringFooter = "        \"\"\""

		# TODO: for oneline description, keep the description after the quotes

		for briefDesc in fn.briefDesc:
			returnString += "        {0}\n".format(briefDesc)

		for detailedDesc in fn.detailedDesc:
			returnString += "        {0}\n".format(detailedDesc)

		for inbodyDesc in fn.inbodyDesc:
			returnString += "        {0}\n".format(inbodyDesc)

		for param in fn.params:
			returnString += "        {0} -- {1}\n".format(param.name, ClassyPresenter.unqueue_type(param.type))

		if fn.type != "void":
			returnString += "        return -- {0}\n".format(ClassyPresenter.unqueue_type(fn.type))

		if returnString is not "":
			returnString = returnStringHeader + returnString + returnStringFooter

		return returnString

	def get_original_implementation(self, fn):
		if self.generateOriginalImplementation == False:
			return ""

		returnString = ""

		if fn.bodyFile:
			filename = fn.bodyFile
			file = open(filename,'r')
			lines = file.readlines()[int(fn.bodyStart)-1:int(fn.bodyEnd)]
			file.close()

			# Use of utf-8 to allow all characters used in the documentation to be displayed
			for line in lines:
				returnString += u"        # {0}".format(line.decode('utf-8'))

		elif fn.headFile:
			filename = fn.headFile
			file = open(filename,'r')
			lines = file.readlines()[int(fn.headLine)]
			file.close()

			returnString += u"        # {0}".format(line.decode('utf-8'))

		return returnString

	def get_reimplementers(self, fn):
		if self.generateReimplementers == False:
			return ""

		returnString = "\n"
		reimplementers = fn.get_reimplementers_separated_with_commas()
		if reimplementers != "":
			returnString += "        # Reimplemented by: [{0}]\n".format(reimplementers)
		else:
			returnString += "";
		return returnString

	def exists_original_implementation(self, fn):
		exists = False
		if fn.bodyFile:
			if (int(fn.bodyEnd) - int(fn.bodyStart)) > 0:
				exists = True

		elif fn.headFile:
			exists = True

		return exists

	def exists_reimplementers(self, fn):
		return len(fn.reimplementers) > 0

	def exists_function_description(self, fn):
		if (len(fn.briefDesc)+len(fn.detailedDesc)+len(fn.inbodyDesc) > 0) or \
		   (len(fn.params) > 0) or \
		   (fn.type != "void"):
			return True
		else:
			return False