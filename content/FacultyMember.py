# -*- coding: utf-8 -*-
#
# File: FacultyMember.py
#
# Copyright (c) 2007 by []
# Generator: ArchGenXML Version 1.5.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.UWOshCommitteeOnCommittees.content.Person import Person
from Products.UWOshCommitteeOnCommittees.config import *

# additional imports from tagged value 'import'
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['phone1'] = Person.schema['phone1'].copy()
copied_fields['phone1'].default_method = "getDefaultLDAPWorkPhone"
copied_fields['phoneType1'] = Person.schema['phoneType1'].copy()
copied_fields['phoneType1'].default = "work"
copied_fields['title'] = Person.schema['title'].copy()
copied_fields['title'].default_method = "getDefaultTitleInstructor"
copied_fields['title'].widget.label = "Instructor Name"
schema = Schema((

    copied_fields['phone1'],
        copied_fields['phoneType1'],
        StringField(
        name='officeNumberLDAP',
        widget=StringWidget(
            label="Office Location (from LDAP)",
            label_msgid='UWOshCommitteeOnCommittees_label_officeNumberLDAP',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        default_method="getDefaultOfficeNumberLDAP"
    ),

    StringField(
        name='officeBuilding',
        widget=SelectionWidget(
            label="Office Building",
            visible=0,
            label_msgid='UWOshCommitteeOnCommittees_label_officeBuilding',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        enforceVocabulary=1,
        vocabulary=NamedVocabulary("""UWOshBuildings"""),
        default_method="getDefaultBuilding"
    ),

    StringField(
        name='officeRoom',
        widget=StringWidget(
            label="Office Room",
            visible=0,
            label_msgid='UWOshCommitteeOnCommittees_label_officeRoom',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        default_method="getDefaultRoom"
    ),

    StringField(
        name='officeMailbox',
        widget=StringWidget(
            label="Office Mailbox (optional)",
            label_msgid='UWOshCommitteeOnCommittees_label_officeMailbox',
            i18n_domain='UWOshCommitteeOnCommittees',
        )
    ),

    copied_fields['title'],
        ReferenceField(
        name='researchInterest',
        widget=ReferenceWidget(
            label='Researchinterest',
            label_msgid='UWOshCommitteeOnCommittees_label_researchInterest',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        allowed_types=('ResearchInterest',),
        multiValued=1,
        relationship='facultyMemberResearchInterest'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

FacultyMember_schema = getattr(Person, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class FacultyMember(Person):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(Person,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'FacultyMember'

    meta_type = 'FacultyMember'
    portal_type = 'FacultyMember'
    allowed_content_types = [] + list(getattr(Person, 'allowed_content_types', []))
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'FacultyMember.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "FacultyMember"
    typeDescMsgId = 'description_edit_facultymember'

    _at_rename_after_creation = True

    schema = FacultyMember_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getDefaultTitleInstructor')
    def getDefaultTitleInstructor(self):
        """
        """
        pass

    security.declarePublic('getDefaultOfficeNumberLDAP')
    def getDefaultOfficeNumberLDAP(self):
        """
        """
        pass

    security.declarePublic('getDefaultBuilding')
    def getDefaultBuilding(self):
        """
        """
        pass

    security.declarePublic('getDefaultRoom')
    def getDefaultRoom(self):
        """
        """
        pass


registerType(FacultyMember, PROJECTNAME)
# end of class FacultyMember

##code-section module-footer #fill in your manual code here
##/code-section module-footer



