import os,sys,unittest,time,json
import redis
import hashlib
from rediscluster import StrictRedisCluster

from lib.mysql import Mysql

r1 = redis.Redis(host='10.203.238.172', password='awmpsnyc5psr5qny', port=8080)
r2 = redis.Redis(host='10.203.238.173', password='awmpsnyc5psr5qny', port=8080)
r3 = redis.Redis(host='10.203.238.176', password='awmpsnyc5psr5qny', port=8080)
r4 = redis.Redis(host='10.203.238.177', password='awmpsnyc5psr5qny', port=8080)
#r5= redis.Redis(host='10.203.62.40', password='yzjy9kerhsku4by1', port=8080)
r=[r1,r2,r3,r4]
#r=[r5]
pool = redis.ConnectionPool(host='10.203.62.40', password='yzjy9kerhsku4by1', port=8080,db=0, decode_responses=True)
rc = redis.Redis(connection_pool=pool)

#key='*gisak@GEO|43f7d2425807442b8b8b382607ee203b|ips*'
# rc.delete('rds')
# test=json.dumps(test)
# print(type(test))
# a=rc.set('rds',test)
# res=rc.get('rds')
# nres=json.loads(res)
# print(len(nres[0]))

def getredisall(rc,key):
	rc=rc
	for i in rc.keys():
		if key in str(i):
			type = rc.type(i)
			print(type)
			if type == 'string':
				vals = rc.get(i)
				print(vals)
			elif type == 'list':
				vals = rc.lrange(i, 0, -1)
				print(vals)
			elif type == 'set':
				vals = rc.smembers(i)
				print(vals)
			elif type == 'zset':
				vals = rc.zrange(i, 0, -1)
				print(vals)
			elif type == "hash":
				vals = rc.hgetall(i)
				print(vals)
			else:
				print(type, i)
		return vals
		
akfile = "c://apache-jmeter-3.0/bin/ak.csv"
aoifile = "c://apache-jmeter-3.0/bin/aoi.csv"
numfile = "c://apache-jmeter-3.0/bin/num.csv"

# with open (akfile,'w+',encoding='utf_8') as f:
# 	for i in rc.keys():
# 		f.write(i+'\n')

with open(numfile, 'w+', encoding='utf_8') as f:
	for i in range(1,101):
			f.write(str(i)+","+str(i) + '\n')
				
				
				
				
				
				
				# def get(self, block=True, timeout=None):
		# for i in rc.keys():
		# 	if key in str(i):
		# 		type = rc.type(i)
		# 		print(type)
		# 		if type == 'string':
		# 			vals = rc.get(i)
		# 			print(vals)
		# 		elif type == 'list':
		# 			vals = rc.lrange(i, 0, -1)
		# 			print(vals)
		# 		elif type == 'set':
		# 			vals = rc.smembers(i)
		# 			print(vals)
		# 		elif type == 'zset':
		# 			vals = rc.zrange(i, 0, -1)
		# 			print(vals)
		# 		elif type == "hash":
		# 			vals = rc.hgetall(i)
		# 			print(vals)
		# 		else:
		# 			print(type, i)





# a=checkredis('43f7d2425807442b8b8b382607ee203b')
# print(a)
        # for single_data in data:
        #     for meta_data in single_data:
        #         #q.put(meta_data)
        #         print(meta_data)


file="e:/项目/地理编码/数据/白名单测试/白名单.csv"

#清除redis四个库的数据
def clean ():
	for i in r:
		print(i)
		i.flushdb()

#统计redis四个库一共多少个key
def rnum():
	k=0
	for i in r:
		k=k+i.dbsize()
	print(' redis一共有%d个key'%k)
	
	
#输入key值，会在四个库查询，如果有就value就返回具体值，没有就返回0
def checkredis(key):
	keys=[]
	k=0
	for i in r:
		for j  in i.keys():
			if key in str(j):
				keys.append(j)
		else:
			k=k+1

	return keys




#通过adcode和address计算key值
def rmd5(adcode,address):
	a = adcode + "|" + address
	key = hashlib.md5(a.encode(encoding='UTF-8')).hexdigest()
	return key

#这个函数的功能是通过读取white.txt文本指定格式数据（按照adcode,address格式），每读一行都去redis查找，如果有就value就返回具体值，没有就返回0。
#主要是为了验证指定数据是否写入redis。
def cklog(file):
	now=time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
	ck = os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + 'check_key_' + now  + '.txt'
	p = open(ck, 'a+', encoding='utf-8')
	k = 1
	with open(file,'r',encoding='utf-8') as f:
		for line in f.readlines():
			temp=line.split(",")
			adcode = temp[1].strip()
			address = temp[0].strip()
			# print(rmd5(a))
			r=checkredis(rmd5(adcode,address))
			print(r)
			
			p.write(str(k))
			p.write('\n')
			p.write(str(adcode))
			p.write('|')
			p.write(str(address))
			p.write('\n')
			p.write('key=%s'%rmd5(adcode,address))
			p.write('\n')
			if r == 0:
				p.write("redis没有该key")
			else:
				p.write(str(r))
			p.write('\n\n')
			k=k+1
	p.close()
# clean()
# rnum()
#cklog(file)
# adcode="北京"
# address="北京市大兴区青云店大集"
# print(rmd5(adcode,address))
# print(checkredis(rmd5(adcode,address)))
# print(checkredis("018a815a6559d789905e9959c3a728d2"))
#7b7dcb064f88fd1b10865e7bd70f0ca6XS
#geo redis一共有17562个key  4008019910
#cklog(file)




