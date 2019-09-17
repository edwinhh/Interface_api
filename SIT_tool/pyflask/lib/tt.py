from SIT_tool.pyflask.lib.jira import jira
from SIT_tool.pyflask.lib.readconfig import getdb
from SIT_tool.pyflask.lib.readconfig import getredis
import json
from SIT_tool.pyflask.lib.jira_lib import jira_lib
jira_lib=jira_lib(getdb('jira_sit'))
a=jira_lib.rds_issuetype('GIS_ASS_RDS')
print(a)

# jira=jira_lib(getdb('jira'))
# a=jira.vname()
# print(a)
# # #g=jira.rds_issuetype('GIS_ASS_RDS')
# k=jira.rds_all_version('GIS_ASS_RDS','V4.0')
# g=jira.name('01369602')
# print(len(k))


# jira=jira(getdb('jira_sit'),getredis('ak_sit'))
# #print(jira.vname('GIS_ASS_RDS'))
# # g=jira.project_all('GIS_ASS_RDS')
# k=jira.project_all_version('GIS_ASS_RDS','V3.9')
# c1=jira.project_counts('GIS_ASS_RDS','V3.9')
# c2=jira.project_counts('GIS_ASS_RDS')
# b=jira.project_vnames_counts('GIS_ASS_RDS')
# c=jira.counts('GIS_ASS_RDS','V3.9')
# print(c1)
# print(b)
# #print(jira.interval('',''))
# def counter(a=0):
# 	cn=[0]
# 	def c():
# 		cn[0]+=a
# 		return cn[0]
# 	return c
# co5=counter(5)
# for i in range(3):
# 	print(co5())


# start_sec = time.mktime(time.strptime(start_date,'%Y-%m-%d %H:%M:%S'))
# end_sec = time.mktime(time.strptime(end_date,'%Y-%m-%d %H:%M:%S'))
# s = int((end_sec - start_sec))
# work_days = int((end_sec - start_sec)/(24*60*60))
# print(s/(60*60))
# print(work_days)
#print(c1)

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


