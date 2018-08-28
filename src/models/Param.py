class Param:
	""" Param class """

	def __init__(self, id=None, name="", type=""):
		self.id				= id
		self.name 			= name
		self.type 			= type

	@staticmethod
	def get_by_name(paramList, paramName):
		for param in paramList:
			if param.name == paramName:
				return param

		return None

