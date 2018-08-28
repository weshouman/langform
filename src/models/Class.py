class Class:
	""" Class class. """

	def __init__(self, id="", name="", variables=[], functions=[], signals=[], parents=[], children=[], briefDesc=[], detailedDesc=[], inbodyDesc=[]):
		self.id		= id

		self.name 	= name

		self.variables 	= variables
		self.functions 	= functions
		self.signals 	= signals

		# parent class ids
		self.parents 	= parents
		# children class ids
		self.children 	= children

		self.briefDesc	= briefDesc
		self.detailedDesc = detailedDesc
		self.inbodyDesc = inbodyDesc

	@staticmethod
	def get_by_id(classList, id):
		for cl in classList:
			if cl.id == id:
				return cl

		return None

	def __str__(self):
		returnString = "class: {" 
		returnString += "id: {0}, ".format(str(self.id))
		returnString += "name: {0}, ".format(str(self.name))

		returnString += "variables: ["
		for index, variable in enumerate(self.variables):
			returnString += str(variable.name)

			if (len(self.variables) != index+1): returnString += ", "

		returnString += "], "

		returnString += "functions: ["
		for index, function in enumerate(self.functions):
			returnString += "{"+"name: {0}, ".format(str(function.name))

			returnString += "params: ["
			for index, param in enumerate(function.params):
				returnString += str(param.name)

				if (len(function.params) != index+1): returnString += ", "
			returnString += "]}"

			if (len(self.functions) != index+1): returnString += ", "

		returnString += "], "

		returnString += "signals: ["
		for index, signal in enumerate(self.signals):
			returnString += str(signal.name)

			if (len(self.signals) != index+1): returnString += ", "

		returnString += "], "

		returnString += "parents: ["
		for index, parent in enumerate(self.parents):
			returnString += str(parent)

			if (len(self.parents) != index+1): returnString += ", "

		returnString += "], "

		returnString += "children: ["
		for index, child in enumerate(self.children):
			returnString += str(child)

			if (len(self.children) != index+1): returnString += ", "

		returnString += "]"

		returnString += "}"

		return returnString