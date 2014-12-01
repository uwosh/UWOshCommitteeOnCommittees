# -*- coding: utf-8 -*-
#
# File: College.py
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
from Products.UWOshCommitteeOnCommittees.content.Constituency import Constituency
from Products.ATBackRef.BackReferenceField import BackReferenceField, BackReferenceWidget
from Products.UWOshCommitteeOnCommittees.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ReferenceField(
        name='departments',
        widget=ReferenceWidget(
            label='Departments',
            label_msgid='UWOshCommitteeOnCommittees_label_departments',
            i18n_domain='UWOshCommitteeOnCommittees',
        ),
        allowed_types=('Department',),
        multiValued=1,
        relationship='college_department'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

College_schema = BaseFolderSchema.copy() + \
    getattr(Constituency, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class College(BaseFolder, Constituency):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),) + (getattr(Constituency,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'College'

    meta_type = 'College'
    portal_type = 'College'
    allowed_content_types = ['Division'] + list(getattr(Constituency, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 1
    #content_icon = 'College.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "College"
    typeDescMsgId = 'description_edit_college'

    _at_rename_after_creation = True

    schema = College_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(College, PROJECTNAME)
# end of class College

##code-section module-footer #fill in your manual code here
##/code-section module-footer



