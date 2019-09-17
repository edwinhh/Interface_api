from SIT_tool.pyflask.lib.MyDB import MyDB
from SIT_tool.pyflask.lib.myredis import RedisQueue
from SIT_tool.pyflask.lib.readconfig import getdb
from SIT_tool.pyflask.lib.readconfig import getsql
from SIT_tool.pyflask.lib.readconfig import getredis
from SIT_tool.pyflask.lib.jira_lib import jira_lib
import decimal
import time
from decimal import *
import datetime

class jira():
#数据库和reids初始化
	def __init__(self,db,res):
		self.host = db[0]
		self.username = db[1]
		self.password = db[2]
		self.port = int(db[3])
		self.database = db[4]
		# self.hostrc = redis[0]
		# self.passwordrc = redis[1]
		# self.portrc = int(redis[2])
		# self.dbrc = redis[3]
		self.mydb = MyDB(self.host, self.username, self.password, self.port, self.database)
		self.rc=RedisQueue(res)
		self.buglist=['调研中','待修复','修复中','已修复','测试中','关闭']




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

#输入项目名或者项目名，版本号，返回	相关bug状态的统计数量 （返回类型是字典）
	def project_counts(self,project,verson='all'):
		temp=[]
		dic={}
		num=0
		if verson=='all':
			res=self.project_all(project)
		else:
			res=self.project_all_version(project,verson)
		for i in self.buglist:
			temp= [i for j in res if j[-2] == i]
			dic[i]=temp.count(i)
		return dic

#输入项目名返回该项目下所有版本的bug状态的统计数量 （返回类型是list）
	def project_vnames_counts(self,project):
		vname=[]
		counts={}
		bugs = []
		temp=[]
		res=self.project_all(project)
		for i in res:
			temp.append(i[6])
		vname=list(set(temp))
		vname.sort(reverse=1)
		
		for v in vname:
			res=self.project_counts(project,v)
			res1=self.project_all_version(project,v)
			bug=[]
			counts[v]=res
			bug=[i for i in list(res.values())]
			bug.insert(0,v)
			c=self.counts(project,v)
			bug.append(c['project'])
			bug.append(c['bug'])
			bug.append(res1[0][7])
			bug.append(res1[0][8])
			bug.append(self.interval(res1[0][7],res1[0][8]))
			bugs.append(bug)
		return bugs

#获取所有项目编码
	def project(self):
		result=self.rc.get("project")
		return result
		
#通过项目名查询下面所有的版本号
	def vname(self,name):
		res = self.rc.get("vname")
		result=[i[1] for i in res if i[0]==name]
		return  result

#返回时间差
	def interval(self,t1,t2):
		start_date = t1
		end_date = t2
		if start_date and end_date:
			start_sec = time.mktime(time.strptime(start_date, '%Y-%m-%d %H:%M:%S'))
			end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d %H:%M:%S'))
			s = int((end_sec - start_sec))
			ts=s/ (60 * 60)
			if ts <24:
				return str(ts)+'小时'
			else:
				work_days = int(s / (24 * 60 * 60))
				return str(work_days)+'天'


