from SIT_tool.pyflask.lib.MyDB import MyDB
from SIT_tool.pyflask.lib.myredis import RedisQueue
from SIT_tool.pyflask.lib.readconfig import getdb
from SIT_tool.pyflask.lib.readconfig import getsql
from SIT_tool.pyflask.lib.readconfig import getredis
from SIT_tool.pyflask.lib.jira_lib import jira_lib
import decimal
from decimal import *
import datetime

class jira():
#数据库和reids初始化
	def __init__(self,db,redis):
		self.host = db[0]
		self.username = db[1]
		self.password = db[2]
		self.port = int(db[3])
		self.database = db[4]
		self.hostrc = redis[0]
		self.passwordrc = redis[1]
		self.portrc = int(redis[2])
		self.dbrc = redis[3]
		self.mydb = MyDB(self.host, self.username, self.password, self.port, self.database)
		self.rc=RedisQueue(self.hostrc, self.passwordrc, self.portrc, self.dbrc)




#传入项目名和版本号，返回报告人，指派人，该版本下的需求和bug，类型，编号，时间（相当于sql1结果，然后用编号去sql5返回集获取属性，加入到sql1结果集中）
	def project_all_version(self,project,version):
		rds=[]
		res=self.rc.get(project)
		for i in res:
			if version == i[6]:
				rds.append(i)
		return rds

#传入项目名，返回报告人，指派人，该版本下的所有版本，需求和bug，类型，编号，时间（相当于sql1结果，然后用编号去sql5返回集获取属性，加入到sql1结果集中）
	def project_all(self,project):
		res=self.rc.get(project)
		return res

# 传入编号返回是需求类型，比如是需求还是缺陷
	def rds_issuetype(self,newvalue):
		sql1 = getsql('rds', 'sql5')
		sql = sql1 % (newvalue)
		res=self.mydb.query(sql)
		result=self.list(res)
		return result

		
#传入项目名和版本号，返回需求数,bug数
	def counts(self,project,version):
		count={}
		bug=0
		res=self.project_all_version(project,version)
		for i in res:
			if "版本缺陷" in i[-1]:
				bug+=1
		project=len(res)-bug
		count["project"]=project
		count["bug"] = bug
		return count

#获取所有项目编码
	def project(self):
		result=self.rc.get("project")
		return result
		
#通过项目名查询下面所有的版本号
	def vname(self,name):
		res = self.rc.get("vname")
		result=[i[1] for i in res if i[0]==name]
		return  result



# jira.rctest('43f7d2425807442b8b8b382607ee203b')
#t=jira.rds_issuetype('GIS_ASS_RDS%')
#k=jira.rds_all('GIS_ASS_RDS','V4.0')
#print(len(t[0]))
#print(k[0])
# print(k[0][6])
# print(k[0][7])
# #
# k2=jira1.rds_order()
# print(k2)
