# -*- coding: utf-8 -*-
#
# File: CommitteeMember.py
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

from Products.validation.validators import ExpressionValidator
from Products.ATBackRef.BackReferenceField import BackReferenceField, BackReferenceWidget
from Products.UWOshCommitteeOnCommittees.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].searchable = 1
copied_fields['title'].widget.label = "Name"
schema = Schema((

    copied_fields['title'],
        StringField(
        name='role',
        widget=SelectionWidget(
            label='Role',
            label_msgid='UWOshCommitteeOnCommittees_label_role',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        enforceVocabulary=1,
        vocabulary=['Member','Chair'],
        searchable=1
    ),

    IntegerField(
        name='beginYear',
        widget=IntegerField._properties['widget'](
            label="Term Begin Year",
            label_msgid='UWOshCommitteeOnCommittees_label_beginYear',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        validators=(ExpressionValidator('''python:value > 2000'''),),
        searchable=1
    ),

    StringField(
        name='beginTerm',
        widget=SelectionWidget(
            label="Term Begin Semester",
            label_msgid='UWOshCommitteeOnCommittees_label_beginTerm',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        enforceVocabulary=1,
        vocabulary=['','Fall','Spring','Summer'],
        searchable=1
    ),

    IntegerField(
        name='endYear',
        widget=IntegerField._properties['widget'](
            label="Term End Year",
            label_msgid='UWOshCommitteeOnCommittees_label_endYear',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        validators=(ExpressionValidator('''python:value > 2000'''),),
        searchable=1
    ),

    StringField(
        name='endTerm',
        widget=SelectionWidget(
            label="Term End Semester",
            label_msgid='UWOshCommitteeOnCommittees_label_endTerm',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        enforceVocabulary=1,
        vocabulary=['','Fall','Spring','Summer'],
        searchable=1
    ),

    ReferenceField(
        name='constituency',
        widget=ReferenceWidget(
            label='Constituency',
            label_msgid='UWOshCommitteeOnCommittees_label_constituency',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        allowed_types=('Constituency', 'College', 'Division'),
        multiValued=1,
        relationship='committeemember_constituency'
    ),

    ReferenceField(
        name='department',
        widget=ReferenceWidget(
            label='Department',
            label_msgid='UWOshCommitteeOnCommittees_label_department',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        allowed_types=('Department',),
        multiValued=1,
        relationship='member_department'
    ),

    ReferenceField(
        name='person',
        widget=ReferenceWidget(
            label='Person',
            label_msgid='UWOshCommitteeOnCommittees_label_person',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        allowed_types=('Person',),
        multiValued=0,
        relationship='member_person'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

CommitteeMember_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CommitteeMember(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'CommitteeMember'

    meta_type = 'CommitteeMember'
    portal_type = 'CommitteeMember'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'CommitteeMember.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "CommitteeMember"
    typeDescMsgId = 'description_edit_committeemember'

    _at_rename_after_creation = True

    schema = CommitteeMember_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(CommitteeMember, PROJECTNAME)
# end of class CommitteeMember

##code-section module-footer #fill in your manual code here
##/code-section module-footer



