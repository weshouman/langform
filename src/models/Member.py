class Member:
	""" Member class """

	def __init__(self, id=None, name=None, kind="", type="", params=[], sectionKind="", inline=False, static=False, explicit=False, virtuality="", prot="", briefDesc="", detailedDesc="", inbodyDesc="", headFile="", headLine="", bodyFile="", bodyStart=0, bodyEnd=0, reimplementers=[], isConstructor=False, isCopyConstructor=False, isDestructor=False):
		self.id				= id
		self.name 			= name
		self.kind			= kind
		self.type			= type
		self.params 		= params
		self.sectionKind	= sectionKind
		self.inline 		= inline
		self.static 		= static
		self.explicit 		= explicit
		self.virtuality 	= virtuality
		self.prot			= prot
		self.briefDesc 		= briefDesc
		self.detailedDesc 	= detailedDesc
		self.inbodyDesc 	= inbodyDesc
		self.headFile 		= headFile
		self.headLine 		= headLine
 		# bodyFile is usually empty if pure virtual
 		self.bodyFile 		= bodyFile
 		self.bodyStart 		= bodyStart
 		self.bodyEnd 		= bodyEnd
		self.reimplementers	= reimplementers
		self.isConstructor	= isConstructor
		self.isCopyConstructor	= isCopyConstructor
		self.isDestructor   = isDestructor

	@staticmethod
	def get_by_name(memberList, memberName):
		for member in memberList:
			if member.name == memberName:
				return member

		return None

	def get_args_separated_with_commas(self):
		params = self.params
		paramNames = list(map(lambda x: x.name, params))
		if (len(paramNames) > 0 ):
			returnString = ", ".join(paramNames)
		else:
			returnString = ""
		return returnString

	def get_reimplementers_separated_with_commas(self):
		return ", ".join(self.reimplementers)


