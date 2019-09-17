from SIT_tool.pyflask.lib.MyDB import MyDB
from SIT_tool.pyflask.lib.myredis import RedisQueue
from SIT_tool.pyflask.lib.readconfig import getdb
from SIT_tool.pyflask.lib.readconfig import getsql
from SIT_tool.pyflask.lib.readconfig import getredis
import decimal
from decimal import *
import datetime

class jira_lib():
#数据库和reids初始化
	def __init__(self,db):
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
		#self.rc=RedisQueue(self.hostrc, self.passwordrc, self.portrc, self.dbrc)

# 传入编号返回是需求类型，比如是需求还是缺陷

	def rds_issuetype(self,newvalue):
		res=newvalue+"%"
		sql1 = getsql('rds', 'sql5')
		sql = sql1 % (res)
		res=self.mydb.query(sql)
		result=self.list(res)
		if result:
			return result
		else:
			return 0

#传入项目名和版本号，返回报告人，指派人，该版本下的需求和bug，编号，时间（等于sql1）
	def rds_version(self,project,version):
		sql1 = getsql('rds', 'sql1')
		sql=sql1%(project,version)
		res=self.mydb.query(sql)
		result=self.list(res)
		result=self.tostr(result)
		return result

	def rds(self,project):
		sql2 = getsql('rds', 'sql2')
		sql=sql2%(project)
		res=self.mydb.query(sql)
		result=self.list(res)
		result=self.tostr(result)
		return result
	
#传入项目名和版本号，返回报告人，指派人，该版本下的需求和bug，类型，编号，时间（相当于sql1结果，然后用编号去sql5返回集获取属性，加入到sql1结果集中）
	def rds_all_version(self,project,version):
		rds_new=[]
		issuetype=[]
		temp=''
		rds=self.rds_version(project,version)
		issuetype=self.rds_issuetype(project)
		for i in rds:
			key=i[2]+'-'+i[0]
			for j in range(len(issuetype)):
				if key==issuetype[j][0]:
					i.append(issuetype[j][1])
					break
				elif j==len(issuetype)-1:
					if key != issuetype[j][0]:
						i.append(temp)
			rds_new.append(i)
		for i in range(len(rds_new)):
			if rds_new[i][3] is not None:
				rds_new[i][3]=self.name(rds_new[i][3])
			if rds_new[i][4] is not None:
				rds_new[i][4]=self.name(rds_new[i][4])
			if rds_new[i][5] is not None:
				rds_new[i][5]=self.name(rds_new[i][5])
		return rds_new
		
	def rds_all(self,project):
		rds_new = []
		issuetype=[]
		temp=''
		rds=self.rds(project)
		issuetype=self.rds_issuetype(project)
		for i in rds:
			key=i[2]+'-'+i[0]
			for j in range(len(issuetype)):
				if key==issuetype[j][0]:
					i.append(issuetype[j][1])
					break
				elif j==len(issuetype)-1:
					if key != issuetype[j][0]:
						i.append(temp)
			rds_new.append(i)
		for i in range(len(rds_new)):
			if rds_new[i][3] is not None:
				rds_new[i][3]=self.name(rds_new[i][3])
			if rds_new[i][4] is not None:
				rds_new[i][4]=self.name(rds_new[i][4])
			if rds_new[i][5] is not None:
				rds_new[i][5]=self.name(rds_new[i][5])
		return rds_new



		
#传入项目名和版本号，返回需求数,bug数
	def counts(self,project,version):
		count={}
		bug=0
		res=self.rds_all_version(project,version)
		for i in res:
			if "版本缺陷" in i[-1]:
				bug+=1
		project=len(res)-bug
		count["project"]=project
		count["bug"] = bug
		return count

#获取所有项目编码
	def project(self):
		result=[]
		sql = getsql('rds', 'sql4')
		res = self.mydb.query(sql)
		res2 = self.list(res)
		result1 = self.tostr(res2)
		for i in result1:
			result.append(i[0])
		return result
#根据工号查找员工姓名
	def name(self,id):
		sql2 = getsql('rds', 'sql8')
		sql = sql2 % (id)
		res = self.mydb.query(sql)
		result = self.list(res)
		result = self.tostr(result)
		return result[0][0]
		
		
#数据库表返回的结果集，将datetime.datetime和decimal类型的全部转为string类型，用于返回的数组在后期做逻辑处理
	def tostr(self,t):
		for i in t:
			for j in range(len(i)):
				if isinstance(i[j],datetime.datetime):
					i[j]=i[j].strftime('%Y-%m-%d %H:%M:%S')
				if isinstance(i[j], decimal.Decimal):
					i[j]=str(Decimal(i[j].quantize(Decimal('0'))))
		return t
	
# 数据库表返回的元组，转为list
	def list(self,res):
		ll=[]
		res1=list(res)
		if len(res):
			for i in range(len(res1)):
				ll.append(list(res1[i]))
		return ll
			
	def rds_test(self):
		sql2 = getsql('rds', 'sql7')
		sql=sql2
		res=self.mydb.query(sql)
		result=self.list(res)
		result=self.tostr(result)
		return result
		
	def close(self):
		self.mydb.close()





#print(len(t[0]))
#print(k[0])
# print(k[0][6])
# print(k[0][7])
# #
# k2=jira1.rds_order()
# print(k2)
