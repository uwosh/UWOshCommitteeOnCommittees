# import csv
# reader = csv.reader(open("membership.txt", "r"))
# for row in reader:
#     name, department, constituency, committee, startYear, endYear = row
#     print name, department, constituency, committee, startYear, endYear

# return printed

import csv
from zLOG import LOG, INFO

fileName = "/Users/kim/faculty_senate/membership.txt"

def importCommitteeMembers(self):
    reader = csv.reader(open(fileName, "r"))
    pm = self.portal_membership
    pr = self.portal_registration 
    pg = self.portal_groups
    out = []
    ignoreLine = 1
    
    #out.append("opened file ok")

    for row in reader:
        #out.append("reading a line: %s" % row)
        # ignore blank lines
        if not row: continue

#         if ignoreLine:
#             continue
#             ignoreLine = 0
        
        #out.append("got a line: %s" % row)
        # check we have exactly 4 items 
#        assert len(row) == 4
#        assert len(row) == 3

#        out.append("line has 4 items")
#        out.append("line has 3 items")

        name, department, constituency, committee, startYear, endYear = row
#     print name, department, constituency, committee, startYear, endYear
#        id, name, email, password = row
#        id, name, email, groups = row
#        id, name, email = row
        
        out.append("%s %s %s %s %s %s" % (name, department, constituency, committee, startYear, endYear))
#        out.append("id is %s" % id )
#        out.append("name is %s" % name)
#        out.append("email is %s" % email)
#        out.append("groups is %s" % groups)

#	if not password:
#		password = pr.generatePassword()
   
#        out.append("password is %s" % password)

        #try: 
             #pr.addMember(id = id,
                 #password = password,
                 #roles = ["Member",],
                 #properties = {
                     #'fullname': name,
                     #'username': id,
                     #'email': email,
                     #}
                 #)
#        LOG("import_users_with_groups", INFO, "About to add member %s" % id)
#        pr.addMember(id = id,password = password,roles = ["Member","ScreenerRole",],properties = {'fullname': name,'username':id,'email': email,})

              #for groupId in groups.split(','):
                  #group = pg.getGroupById(groupId)
                  #group.addMember(id)

             #group = pg.getGroupById('Member')
             #group.addMember (id)

#        out.append("Added user %s ok" % id)
                
#        except ValueError:
#            out.append("Skipped %s" % id)
            
    return "\n".join(out)            
