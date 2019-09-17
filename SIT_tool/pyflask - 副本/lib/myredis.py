import os,sys,unittest,time,json
import redis
import hashlib
from rediscluster import StrictRedisCluster
from SIT_tool.pyflask.lib.readconfig import getredis

class RedisQueue(object):
	def __init__(self, host, password, port, db):
		self.host = host
		self.password = password
		self.db = db
		self.port = port
		self.pool = redis.ConnectionPool(host=host, password=password, port=port, db=db, decode_responses=True)
		self.rc = redis.Redis(connection_pool=self.pool)
		
	def get_all(self, key,block=True, timeout=None):
		for i in self.rc.keys():
			if key in str(i):
				type = self.rc.type(i)
				if type == 'string':
					vals = self.rc.get(i)
	
				elif type == 'list':
					vals = self.rc.lrange(i, 0, -1)
		
				elif type == 'set':
					vals = self.rc.smembers(i)
	
				elif type == 'zset':
					vals = self.rc.zrange(i, 0, -1)
	
				elif type == "hash":
					vals = self.rc.hgetall(i)
				else:
					print(type, i)
		return list(vals[0])
	
	def keys(self):
		keys=self.rc.keys()
		return keys
		
	def iskey(self,key):
		if self.rc.exists(key):
			return 1
		else:
			return 0
		
	def get(self,key):
		res = self.rc.get(key)
		nres = json.loads(res)
		return nres
	
	def put (self,key,value):
		new_value=json.dumps(value)
		res=self.rc.set(key,new_value)
		
	def delall(self,key):
		self.rc.delete(key)
		
		
