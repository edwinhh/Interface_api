from SIT_tool.pyflask.lib.jira import jira
from SIT_tool.pyflask.lib.readconfig import getdb
from SIT_tool.pyflask.lib.readconfig import getredis
import json
from SIT_tool.pyflask.lib.jira_lib import jira_lib


# jira=jira_lib(getdb('jira'))
# #g=jira.rds_issuetype('GIS_ASS_RDS')
# k=jira.rds_all_version('GIS_ASS_RDS','V4.0')
# g=jira.name('01369602')
# print(k)

#
jira=jira(getdb('jira'),getredis('ak'))
g=jira.project_all('GIS_ASS_RDS')
k=jira.project_all_version('GIS_ASS_RDS',"V4.0")
j=jira.project()
d=jira.counts('GIS_ASS_RDS',"V4.0")
print(g)
# print(k)
# print(d)

# jira.rc.delall('rds')
# jira.rc.delall('rds')
# jira.rc.delall('counts')

# #91
# res=jira_lib.counts('GIS_ASS_RDS','V3.9')
# jira_lib.rc.put('rds',k)
# jira_lib.rc.put('counts',res)
#
# a=jira_lib.rc.get('counts')
# print(a[1])
#
# r=jira_lib.rc.get('rds')
#print(r[0])

# print(len(a))
# print(a)


