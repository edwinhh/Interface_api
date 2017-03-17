import MySQLdb,time,datetime

class UserInfo:

	conn = None
	cursor = None

	def __init__(self):
		if self.conn ==None:
			self.conn = MySQLdb.connect(host="127.0.0.1",port=8090,user='write',passwd='123456',db='test',charset='utf8')
			self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)


	def __del__(self):
		if self.cursor:
			self.cursor.close()
		if self.conn:
			self.conn.close()


	def get(self,uid=0):
		sql='select * from user_info where uid=%s' % uid
		n = self.cursor.execute(sql)
		data = self.cursor.fetchall()
		userinfo = []
		for info in data:
			if info['addtime']:
				info['addtime'] = info['addtime'].strftime("%Y-%m-%d %H:%M:%S")
			if info['modtime']:
				info['modtime'] = info['modtime'].strftime("%Y-%m-%d %H:%M:%S")
			userinfo.append(info)
		return userinfo[0]

	def add(self,params={}):
		uid = int(time.time())
		sql='insert into user_info set uid=%s' % str(uid)
		for k,v in params.items():
			sql += ',`%s`="%s"' % (k,v)
		sql = sql.rstrip(',')
		sql += ",`modtime`='%s' " %  (time.strftime('%Y-%m-%d %H:%M:%S'),)
		n = self.cursor.execute(sql)
		self.conn.commit()
		if n>0:
			time.sleep(1)
			return uid
		else:
			return 0

	def set(self,uid,params):
		if len(params)==0:
			return False
		sql='update user_info set'
		for k,v in params.items():
			sql += ' `%s`="%s",' % (k,v)
		sql = sql[:-1]
		#print sql
		sql += ",`modtime`='%s' where uid=%s" %  (time.strftime('%Y-%m-%d %H:%M:%S'),uid)
		n = self.cursor.execute(sql)
		self.conn.commit()
		return True

	def delete(self,uid=0):
		sql='delete from user_info where uid=%s' % uid
		n = self.cursor.execute(sql)
		self.conn.commit()
		return True