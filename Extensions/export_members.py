import csv, StringIO, time

def export_members(self):
  text = StringIO.StringIO()

  writer = csv.writer(text, delimiter=",")

  committeeMembers = self.queryCatalog({'portal_type':'CommitteeMember'})

  header = ['person', 'committee', 'role', 'beginYear', 'beginTerm', 'endYear', 'endTerm', 'constituency', 'department', ]
  writer.writerow(header)
  
  for committeeMember in committeeMembers:
    committeeMember_props = []
    
    committeeMember = committeeMember.getObject()
    #committeeMember_props.append(committeeMember.Title() or "") # this is the title of the CommitteeMember object (person name plus committee name) so skip it

    # the name of the actual person
    person = committeeMember.getPerson()
    if person:
        committeeMember_props.append(person.Title())
    else:
        committeeMember_props.append("")

    committeeMember_props.append(committeeMember.aq_parent.Title() or "") # name of the committee
    committeeMember_props.append(committeeMember.getRole() or "")
    committeeMember_props.append(committeeMember.getBeginYear() or "")
    committeeMember_props.append(committeeMember.getBeginTerm() or "")
    committeeMember_props.append(committeeMember.getEndYear() or "")
    committeeMember_props.append(committeeMember.getEndTerm() or "")
    
    constituencies = committeeMember.getConstituency()
    if len(constituencies) > 0:
        committeeMember_props.append("|".join([c.Title() for c in constituencies]))
    else:
        committeeMember_props.append("")
    
#     departments = committeeMember.getDepartment()
#     if len(departments) > 0:
#         committeeMember_props.append("|".join([d.Title() for d in departments]))
#     else:
#         committeeMember_props.append("")
    committeeMember_props.append("") # for now can't seem to get the department
    
    writer.writerow(committeeMember_props)


  self.REQUEST.RESPONSE.setHeader('Content-Type','application/csv')
  self.REQUEST.RESPONSE.setHeader('Content-Length',len(text.getvalue()))
  self.REQUEST.RESPONSE.setHeader('Content-Disposition','inline;filename=%scommitteemembers.csv' %
                                time.strftime("%Y%m%d-%H%M%S-",time.localtime()))

  return text.getvalue()

