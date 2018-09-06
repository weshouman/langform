import xml.etree.ElementTree as ET

# Relative to root
XPATH_CLASS = "./compounddef"

# Relative to class
XPATH_SECTION = "./sectiondef"

# Relative to section
XPATH_MEMBER = "./memberdef"
# XPATH_MEMBER = "./memberdef[@kind='variable']"
# XPATH_METHOD = "./memberdef[@kind='function']"

# Relative to memberdef
XPATH_PARENT = "./basecompoundref"
XPATH_CHILD = "./derivedcompoundref"
# XPATH_BRIEF_DESC = "./briefdescription"
# XPATH_DETAILED_DESC = "./detaileddescription"
# XPATH_INBODY_DESC = "./inbodydescription"
XPATH_REIMPLEMENTERS = "./reimplementedby"
XPATH_PARAMS = "./param"

# Relative to a description node
XPATH_PARA = "./para"

def fetch_class_nodes(xmlfile):
	tree = ET.parse(xmlfile)

	root = tree.getroot()

	classNodes = root.findall(XPATH_CLASS)

	return classNodes

##########################
##### Shared getters #####
##########################

def get_node_id(node):
	return node.get('id')

def get_desc_of_desc_node(descNode):
	paraNodes = descNode.findall(XPATH_PARA)
	desc = []

	for index, paraNode in enumerate(paraNodes):
		desc.append(''.join(paraNode.itertext()))

	return desc


#########################
##### Class getters #####
#########################

def get_sections_of_class_node(classNode):
	sectionNodes = classNode.findall(XPATH_SECTION)
	return sectionNodes

def get_parents_of_class_node(classNode):
	""" Fetch the parent references stored in the class"""
	parentRefNodes = classNode.findall(XPATH_PARENT)
	return parentRefNodes

def get_children_of_class_node(classNode):
	""" Fetch the child references stored in the class"""
	childRefNodes = classNode.findall(XPATH_CHILD)
	return childRefNodes

def get_class_id(classNode):
	return get_node_id(classNode)

def get_class_name(classNode):
	return classNode.find('compoundname').text

def get_class_brief_desc(classNode):
	briefDescNode = classNode.find("briefdescription")
	return get_desc_of_desc_node(briefDescNode)

def get_class_detailed_desc(classNode):
	detailedDescNode = classNode.find("detaileddescription")
	return get_desc_of_desc_node(detailedDescNode)

def get_class_inbody_desc(classNode):
	inbodyDescNode = classNode.find("inbodydescription")

	# Handle case of missing inbodydescription nodes for classes
	if inbodyDescNode is None:
		return ""
	else:
		return get_desc_of_desc_node(inbodyDescNode)


###########################
##### Section getters #####
###########################

def get_members_of_section_node(sectionNode):
	""" Fetch the members(variables, functions or signals) stored in the class """
	memberNodes = sectionNode.findall(XPATH_MEMBER)

	return memberNodes

def get_section_kind(sectionNode):
	sectionKind = sectionNode.get('kind')
	return sectionKind


##############################
##### Member Def getters #####
##############################

def get_memberdef_id(memberdefNode):
	return get_node_id(memberdefNode)

def get_memberdef_name(memberdefNode):
	return memberdefNode.find('name').text

def get_memberdef_kind(memberdefNode):
	return memberdefNode.get('kind')

def get_memberdef_type(memberdefNode):
	typeNode = memberdefNode.find('type')
	if typeNode is not None:
		return ''.join(typeNode.itertext())
	else:
		return None

def get_memberdef_inline(memberdefNode):
	return memberdefNode.get('inline')

def get_memberdef_static(memberdefNode):
	return memberdefNode.get('static')

def get_memberdef_explicit(memberdefNode):
	return memberdefNode.get('explicit')

def get_memberdef_virtuality(memberdefNode):
	return memberdefNode.get('virtuality')

def get_memberdef_prot(memberdefNode):
	return memberdefNode.get('prot')

def get_memberdef_brief_desc(memberdefNode):
	briefDescNode = memberdefNode.find("briefdescription")
	return get_desc_of_desc_node(briefDescNode)

def get_memberdef_detailed_desc(memberdefNode):
	detailedDescNode = memberdefNode.find("detaileddescription")
	return get_desc_of_desc_node(detailedDescNode)

def get_memberdef_inbody_desc(memberdefNode):
	inbodyDescNode = memberdefNode.find("inbodydescription")
	return get_desc_of_desc_node(inbodyDescNode)

# TODO: use another validator that ensures the singularity of those elements in advance!
# we don't need clutter code with cases that would/should never happen here
# def get_memberdef_brief_desc(memberdefNode):
# 	briefDescNodes = memberdefNode.findall(XPATH_BRIEF_DESC)
# 	assert len(briefDescNodes) == 1
# 	briefDescNode =briefDescNodes[0]
# 	return get_desc_of_desc_node(briefDescNode)

# def get_memberdef_detailed_desc(memberdefNode):
# 	detailedDescNodes = memberdefNode.findall(XPATH_DETAILED_DESC)
# 	assert len(detailedDescNodes) == 1
# 	detailedDescNode =detailedDescNodes[0]
# 	return get_desc_of_desc_node(detailedDescNode)

# def get_memberdef_inbody_desc(memberdefNode):
# 	inbodyDescNodes = memberdefNode.findall(XPATH_INBODY_DESC)
# 	assert len(inbodyDescNodes) == 1
# 	inbodyDescNode =inbodyDescNodes[0]
# 	return get_desc_of_desc_node(inbodyDescNode)

def get_memberdef_head_line(memberdefNode):
	locationNode = memberdefNode.find('location')
	headLine = locationNode.get('line')
	return headLine

def get_memberdef_head_file(memberdefNode):
	locationNode = memberdefNode.find('location')
	headFile = locationNode.get('headfile')
	return headFile

def get_memberdef_body_file(memberdefNode):
	locationNode = memberdefNode.find('location')
	bodyFile = locationNode.get('bodyfile')
	return bodyFile

def get_memberdef_body_start(memberdefNode):
	locationNode = memberdefNode.find('location')
	bodyStart = locationNode.get('bodystart')
	return bodyStart

def get_memberdef_body_end(memberdefNode):
	locationNode = memberdefNode.find('location')
	bodyEnd = locationNode.get('bodyend')
	return bodyEnd

def get_reimplementers_of_memberdef_node(memberdefNode):
	"""
	Return a list of refids for classes that reimplement the given memberdef
	"""
	reimplementerNodes = memberdefNode.findall(XPATH_REIMPLEMENTERS)

	reimplementerList = []
	for reimplementerNode in reimplementerNodes:
		reimplementerList.append(reimplementerNode.get('refid'))

	return reimplementerList

def get_params_of_memberdef_node(memberdefNode):
	""" Return param nodes of a memberdef """
	return memberdefNode.findall(XPATH_PARAMS)


#########################
##### Param getters #####
#########################

def get_name_of_param_node(paramNode):
	""" copy constructors don't have names, but rather combound type """
	declname = paramNode.find('declname')
	if declname != None:
		name = declname.text
	else:
		name = ""
	return name

def get_type_node_of_param_node(paramNode):
	return paramNode.find('type')

def get_type_of_param_node(paramNode):
	typeNode = get_type_node_of_param_node(paramNode)

	# TODO: check why
	if typeNode is not None:
		typeText = ''.join(typeNode.itertext())

		if typeText:
			return typeText
		else:
			# TODO: cleanup
			assert False
			typeName = get_name_of_combound_type_node(typeNode)
			return typeName

########################
##### Type getters #####
########################

def get_name_of_combound_type_node(typeNode):
	refText = typeNode.find('ref').text
	return refText

def is_member_copy_constructor(classRefid, paramNode):
	""" return True if given param resembles a copy constructor """
	typeNode = get_type_node_of_param_node(paramNode)
	isCopyConstructor = False

	# TODO: check why
	if typeNode is not None:
		typeRef = typeNode.find('ref')

		if typeRef is not None and (typeRef.get('refid') == classRefid):
			isCopyConstructor = True
		else:
			isCopyConstructor = False

	return isCopyConstructor


###################################
##### Named Reference getters #####
###################################

def get_parent_id(parentNode):
	return parentNode.get('refid')

def get_parent_name(parentNode):
	return parentNode.text

def get_child_id(childNode):
	return childNode.get('refid')

def get_child_name(childNode):
	return childNode.text

