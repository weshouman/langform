import re

class ClassyPresenter(object):

	def __init__(self, cl=None):
		self.cl = cl

		self.variableNamesWithCommas = self.get_variables_with_commas()

		self.parentNamesWithCommas = self.get_parents_with_commas()

		self.generateOriginalImplementation = True
		self.generateReimplementers = True
		self.generateConstructors = True

	def functions(self):
		if (self.cl):
			if self.generateConstructors == True:
				return self.cl.functions
			else:
				# remove constructors (including copy constructors) and destructors
				return filter(lambda x: (x.isConstructor == False and x.isDestructor == False), self.cl.functions)
		else:
			return []

	def variables(self):
		if (self.cl):
			return self.cl.variables
		else:
			return []

	def parents(self):
		if (self.cl):
			return self.cl.parents
		else:
			return []

	# TODO: move to class.py
	def get_variables_with_commas(self):
		"""
		 Note: we start with a comma
		"""
		variables = self.variables()
		memberNames = list(map(lambda x: x.name, variables))
		if (len(memberNames) > 0 ):
			returnString = ", " + ", ".join(memberNames)
		else:
			returnString = ""
		return returnString

	def get_parents_with_commas(self):
		parentNames = self.parents()
		return ",".join(parentNames)

	def get_args(self, function):
		returnString = ""

		args_separated_with_commas = function.get_args_separated_with_commas()

		if function.static == "no":
			returnString += "self"

			if args_separated_with_commas is not "":
				returnString += ", " 

		returnString += args_separated_with_commas
		return returnString

	@staticmethod
	def unqueue_type(typeText):
		rep = {"QList": "List",
			   "QString": "String",
			   "QSet": "Set",
			   "QDateTime": "DateTime",
			   "QComboBox": "ComboBox"} # define desired replacements here

		rep = dict((re.escape(k), v) for k, v in rep.iteritems())
		pattern = re.compile("|".join(rep.keys()))
		typeText = pattern.sub(lambda m: rep[re.escape(m.group(0))], typeText)
		return typeText

	def get_static_decoration(self, function):
		returnString = ""
		returnStringHeader = "\n    "
		returnStringFooter = "\n"

		if function.static == "yes":
			returnString += "@staticmethod"

		if returnString is not "":
			returnString = returnStringHeader + returnString + returnStringFooter

		return returnString

	def get_description(self, fn):
		returnString = ""
		returnStringHeader = "\n        \"\"\"\n"
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

			if (len(lines) > 0):
				returnString += "\n"
			# Use of utf-8 to allow all characters used in the documentation to be displayed
			for line in lines:
				returnString += u"        # {0}".format(line.decode('utf-8'))

		elif fn.headFile:
			filename = fn.headFile
			file = open(filename,'r')
			lines = file.readlines()[int(fn.headLine)]
			file.close()

			returnString += u"\n        # {0}".format(line.decode('utf-8'))

		return returnString

	def get_reimplementers(self, fn):
		if self.generateReimplementers == False:
			return ""

		reimplementers = fn.get_reimplementers_separated_with_commas()
		if reimplementers != "":
			returnString = "\n        # Reimplementers: [{0}]\n".format(reimplementers)
		else:
			returnString = "";
		return returnString

	def get_class_description(self, cl):

		returnString = "\"\"\" {0} class.".format(self.cl.name)

		tempString = ""
		for briefDesc in cl.briefDesc:
			tempString += "        {0}\n".format(briefDesc)

		for detailedDesc in cl.detailedDesc:
			tempString += "        {0}\n".format(detailedDesc)

		for inbodyDesc in cl.inbodyDesc:
			tempString += "        {0}\n".format(inbodyDesc)

		if tempString == None or tempString == "":
			returnString += " \"\"\""
		else:
			returnString += "\n"
			returnString += tempString
			returnString += "    \"\"\""

		return returnString
