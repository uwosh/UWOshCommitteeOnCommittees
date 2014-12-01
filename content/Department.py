# -*- coding: utf-8 -*-
#
# File: Department.py
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

from Products.ATBackRef.BackReferenceField import BackReferenceField, BackReferenceWidget
from Products.UWOshCommitteeOnCommittees.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    BackReferenceField(
        name='member',
        widget=BackReferenceWidget(
            label='Member',
            label_msgid='UWOshCommitteeOnCommittees_label_member',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        allowed_types=('CommitteeMember',),
        multiValued=1,
        relationship='member_department'
    ),

    BackReferenceField(
        name='divisions',
        widget=BackReferenceWidget(
            label='Divisions',
            label_msgid='UWOshCommitteeOnCommittees_label_divisions',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        allowed_types=('Division',),
        multiValued=0,
        relationship='division_department'
    ),

    BackReferenceField(
        name='colleges',
        widget=BackReferenceWidget(
            label='Colleges',
            label_msgid='UWOshCommitteeOnCommittees_label_colleges',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        allowed_types=('College',),
        multiValued=0,
        relationship='college_department'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Department_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Department(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Department'

    meta_type = 'Department'
    portal_type = 'Department'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'Department.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Department"
    typeDescMsgId = 'description_edit_department'

    _at_rename_after_creation = True

    schema = Department_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Department, PROJECTNAME)
# end of class Department

##code-section module-footer #fill in your manual code here
##/code-section module-footer



