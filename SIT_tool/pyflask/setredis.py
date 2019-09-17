from SIT_tool.pyflask.lib.MyDB import MyDB
from SIT_tool.pyflask.lib.myredis import RedisQueue
from SIT_tool.pyflask.lib.readconfig import getdb
from SIT_tool.pyflask.lib.readconfig import getsql
from SIT_tool.pyflask.lib.readconfig import getredis
from SIT_tool.pyflask.lib.jira_lib import jira_lib
import schedule
import time
import datetime

class setredis():
	def __init__(self,redis):
		self.hostrc = redis[0]
		self.passwordrc = redis[1]
		self.portrc = int(redis[2])
		self.dbrc = redis[3]
		self.rc = RedisQueue(self.hostrc, self.passwordrc, self.portrc, self.dbrc)
		self.jira_lib = jira_lib(getdb('jira'))
	
	def set_project_all (self):
		project=self.jira_lib.project()
		self.rc.put('project', project)
		print("写入项目编号完成")
		self.rc.put('vname',self.jira_lib.vname())
		print("写入项目版本完成")
		for i in project:
			res=self.jira_lib.rds_all(i)
			self.rc.put(i,res)
			print("写入 %s 完成" % (i))
		print("执行完成")
	

	def del_reids(self):
		keys=self.rc.keys()
		for i in keys:
			if "GIS" in i:
				self.rc.delall(i)
		print("删除完毕")
		
		
def redis():
	rc=setredis(getredis('ak'))
	#rc.del_reids()
	rc.set_project_all()
	
def job(t):
	try:
		schedule.every().day.at(t).do(redis)
	except Exception as e:
		print('Error: %s'% e)
		
	while True:
		schedule.run_pending()
		time.sleep(1)
	
redis()
#job("00:00")


