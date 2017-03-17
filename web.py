import MySQLdb,time,datetime
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/userinfo/get')
def get():
	res = {'errno':0,'errmsg':'','data':[]}
	try:
		uid=request.args.get('uid')
		if None == uid:
			res['errno'] =101
			raise Exception('invalid params: uid')
		userinfo = get_user(uid)
		if len(userinfo) == 0:
			res['errno'] = 102
			raise Exception('not exist user')
		res['data'] = userinfo
	except Exception,e:
		if res['errno'] == 0:
			res['errno'] = 999
		res['errmsg'] = str(e)
	return jsonify(res)


def get_user(uid):
	conn = MySQLdb.connect(host="127.0.0.1",port=8090,user='write',passwd='123456',db='test',charset='utf8')
	cursor = conn.cursor(MySQLdb.cursors.DictCursor)
	sql='select * from user_info where uid=%s' % uid
	n = cursor.execute(sql)
	data = cursor.fetchall()
	userinfo = []
	for info in data:
		if info['addtime']:
			info['addtime'] = info['addtime'].strftime("%Y-%m-%d %H:%M:%S")
		if info['modtime']:
			info['modtime'] = info['modtime'].strftime("%Y-%m-%d %H:%M:%S")
		userinfo.append(info)
	return userinfo


@app.route('/userinfo/set')
def set():
	res = {'errno':0,'errmsg':''}
	try:
		uid=request.args.get('uid')
		if None == uid:
			res['errno'] =101
			raise Exception('invalid params: uid')
		params = {}
		if request.args.get('name'):
			params['name'] = request.args.get('name')
		if request.args.get('gender'):
			params['gender'] = request.args.get('gender')
		if request.args.get('mobile'):
			params['mobile'] = request.args.get('mobile')
		if request.args.get('mail'):
			params['mail'] = request.args.get('mail')
		if request.args.get('status'):
			params['status'] = request.args.get('status')
		if len(params)==0:
			res['errno'] =101
			raise Exception('no invalid set param')
		if set_user(uid,params) == False:
			res['errno'] == 102
			raise Exception('update userinfo fail')
	except Exception,e:
		if res['errno'] == 0:
			res['errno'] = 999
		res['errmsg'] = str(e)
	return jsonify(res)



def set_user(uid,params):
	if len(params)==0:
		return False
	conn = MySQLdb.connect(host="127.0.0.1",port=8090,user='write',passwd='123456',db='test',charset='utf8')
	cursor = conn.cursor()
	sql='update user_info set'
	for k,v in params.items():
		sql += ' `%s`="%s",' % (k,v)
	sql = sql[:-1]
	#print sql
	sql += ",`modtime`='%s' where uid=%s" %  (time.strftime('%Y-%m-%d %H:%M:%S'),uid)
	n = cursor.execute(sql)
	return True


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8972, debug=True)
	#app.run(host='192.168.1.114', port=8972, debug=True)
