import parsers.class_parser    as parser

import settings
from settings import VERBOSE

from models.Class import Class
from models.Member import Member
from models.Param import Param

import os

from common import list_util

# create classes

def get_members_of_class_node(classNode):
	memberList = []

	classRefid = parser.get_class_id(classNode)
	className  = parser.get_class_name(classNode)

	sectionNodes = parser.get_sections_of_class_node(classNode)
	for sectionNode in sectionNodes:

		mSectionKind	= parser.get_section_kind(sectionNode)

		memberNodes = parser.get_members_of_section_node(sectionNode)
		for memberNode in memberNodes:

			mName 			  = parser.get_memberdef_name(memberNode)

			if (VERBOSE):
				print("processing member: " + mName)

			mId 			  = parser.get_memberdef_id(memberNode)
			mKind 			  = parser.get_memberdef_kind(memberNode)
			mType 			  = parser.get_memberdef_type(memberNode)
			mInline 		  = parser.get_memberdef_inline(memberNode)
			mStatic 		  = parser.get_memberdef_static(memberNode)
			mExplicit 		  = parser.get_memberdef_explicit(memberNode)
			mVirtuality 	  = parser.get_memberdef_virtuality(memberNode)
			mProt			  = parser.get_memberdef_prot(memberNode)
			mBriefDesc 		  = parser.get_memberdef_brief_desc(memberNode)
			mDetailedDesc 	  = parser.get_memberdef_detailed_desc(memberNode)
			mInbodyDesc 	  = parser.get_memberdef_inbody_desc(memberNode)
			mHeadFile 		  = parser.get_memberdef_head_file(memberNode)
			mHeadLine 		  = parser.get_memberdef_head_line(memberNode)
			mBodyFile 		  = parser.get_memberdef_body_file(memberNode)
			mBodyStart 		  = parser.get_memberdef_body_start(memberNode)
			mBodyEnd 		  = parser.get_memberdef_body_end(memberNode)
			mReimplementerIds = parser.get_reimplementers_of_memberdef_node(memberNode)
			mParamNodes		  = parser.get_params_of_memberdef_node(memberNode)

			mIsConstructor     = True if (className == mName) else False
			mIsCopyConstructor = False
			mIsDestructor      = True if ("~"+className == mName) else False

			# Update file locations if necessary
			if (mHeadFile is not None):
				mHeadFile         = mHeadFile.replace(settings.OLD_SOURCE_DIR, settings.NEW_SOURCE_DIR)
			if (mBodyFile is not None):
				mBodyFile         = mBodyFile.replace(settings.OLD_SOURCE_DIR, settings.NEW_SOURCE_DIR)

			mParamList = []
			for index, mParamNode in enumerate(mParamNodes):
				mParamName = parser.get_name_of_param_node(mParamNode)
				mParamType = parser.get_type_of_param_node(mParamNode)

				mIsCopyConstructor = parser.is_member_copy_constructor(classRefid, mParamNode)

				mParam = Param(index, mParamName, mParamType)
				mParamList.append(mParam)

			member = Member(mId, mName, mKind, mType, mParamList,
							mSectionKind, mInline, mStatic, mExplicit, mVirtuality, mProt,
							mBriefDesc, mDetailedDesc, mInbodyDesc,
							mHeadFile, mHeadLine, mBodyFile, mBodyStart, mBodyEnd,
							mReimplementerIds,
							mIsConstructor, mIsCopyConstructor, mIsDestructor)
			memberList.append(member)

	return memberList


def create_class_list(classXML):
	classList = []

	classNodes = parser.fetch_class_nodes(classXML)

	for classNode in classNodes:
		classId = parser.get_class_id(classNode)
		className = parser.get_class_name(classNode)

		if (VERBOSE):
			print("processing class: " + className)

		cBriefDesc 		  = parser.get_class_brief_desc(classNode)
		cDetailedDesc 	  = parser.get_class_detailed_desc(classNode)
		cInbodyDesc 	  = parser.get_class_inbody_desc(classNode)

		# fetch members
		memberList = get_members_of_class_node(classNode)

		# fetch parents classes
		parentList = []
		parentNodes = parser.get_parents_of_class_node(classNode)

		for parentNode in parentNodes:
			pName = parser.get_parent_name(parentNode)

			if (VERBOSE):
				print("processing parent: " + pName)

			# pId = parser.get_parent_id(parentNode)

			parentList.append(pName)

		childList = []
		childNodes = parser.get_children_of_class_node(classNode)

		for childNode in childNodes:
			cName = parser.get_child_name(childNode)

			if (VERBOSE):
				print("processing child: " + cName)

			# cId = parser.get_child_id(childNode)

			childList.append(cName)

		variableList = filter(lambda x: x.kind == "variable", memberList)
		functionList = filter(lambda x: x.kind == "function", memberList)
		signalList 	 = filter(lambda x: x.kind == "signal", memberList)
		cl = Class(classId, className, variableList, functionList, signalList, parentList, childList, cBriefDesc, cDetailedDesc, cInbodyDesc)
		classList.append(cl)

	return classList

def create():

	if (settings.classXMLDir is not None):
		classLists = []
		for (dirpath, dirnames, filenames) in os.walk(settings.classXMLDir):
			for filename in filenames:
				if filename.startswith("class") and filename.endswith(".xml"):
					print("processing file: " + filename)
					classList = create_class_list(os.path.join(dirpath, filename))
					classLists.extend(classList)

		classList = classLists

	else:
		classList = create_class_list(settings.classXML)

	if (VERBOSE):
		print("----")
		for c in classList:
			print(c)

	return [classList]
