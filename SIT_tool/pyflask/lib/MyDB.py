import pymysql
import json
from SIT_tool.pyflask.lib.readconfig import getdb

class MyDB():
     def __init__(self , host, username, password, port, database):
        '''类例化，处理一些连接操作'''
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.cur = None
        self.con = None
	    #self.charset=charset
        # connect to mysql
        try:
            self.con = pymysql.connect(host = self.host, user = self.username, password = self.password, port = self.port, database = self.database,charset='utf8')
            self.cur = self.con.cursor()
        except :
            raise "DataBase connect error,please check the db config."

     def close(self):
        '''结束查询和关闭连接'''
        self.con.close()

     def create_table(self,sql_str):
        '''创建数据表'''
        try:
            self.cur.execute(sql_str)
        except Exception as e:
            print(e)
     def query_formatrs(self,sql_str):
         '''查询数据，返回一个列表，里面的每一行是一个字典，带字段名
             cursor 为连接光标
             sql_str为查询语句
         '''
         try:
             self.cur.execute(sql_str)
             rows = self.cur.fetchall()
             r = []
             for x in rows:
                 r.append(dict(zip(self.cur.column_names,x)))

             return r
         except:
             return False

     def query(self,sql_str):
        '''查询数据并返回
             cursor 为连接光标
             sql_str为查询语句
        '''
        try:
            self.cur.execute(sql_str)
            rows = self.cur.fetchall()
            return rows
        except:
            return False

     def execute_update_insert(self,sql):
        '''
        插入或更新记录 成功返回最后的id
        '''
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.lastrowid


# if __name__ == "__main__":
# 	list=getdb('jira')
# 	host =list[0]
# 	username = list[1]
# 	password = list[2]
# 	port = int(list[3])
# 	database =list[4]
#
# 	sql = "SELECT jiraissue.issuenum,jiraissue.summary,project1.pname,jiraissue.reporter,jiraissue.assignee,jiraissue.creator,jiraissue.summary,projectversion.description,projectversion.vname,projectversion.startdate,projectversion.releasedate,jiraissue.created,jiraissue.updated,jiraissue.duedate,issuestatus1.pname,cwd_user.display_name\
# 	FROM jiratestdb.jiraissue as jiraissue,jiratestdb.project as project1,jiratestdb.projectversion as projectversion,jiratestdb.nodeassociation as nodeassociation,\
# 	jiratestdb.issuestatus as issuestatus1,\
# 	jiratestdb.cwd_user as cwd_user\
# 	where\
# 	jiraissue.project=project1.id\
# 	and cwd_user.user_name =jiraissue.reporter\
# 	and issuestatus1.id=jiraissue.issuestatus\
# 	and projectversion.project=jiraissue.project\
# 	and nodeassociation.source_node_id=jiraissue.id\
# 	and projectversion.id=nodeassociation.sink_node_id\
# 	and project1.originalkey='GIS_ASS_RDS'\
# 	and projectversion.vname='V4.0'"
	
	# mydb = MyDB(host, username, password, port, database)
	# results = mydb.query(sql)
	# for i in results:
	# 	print(i)
	# for row in results:
	# 	productname = row[0]
	# 	supportname = row[1]
	# 	productinterface = row[2]
	# 	print("productname=%s,supportname=%s,productinterface=%s" % \
     #           (productname, supportname, productinterface))
    # list = mydb.query_formatrs("SELECT * FROM detailinfo")
    # for i in list:
    #     print ("记录号：%s   值：%s" % (list.index(i) + 1, i))
    # #关闭数据库
	#mydb.close()
