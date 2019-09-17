import os,sys,unittest,time,json
import redis
import hashlib
from rediscluster import StrictRedisCluster
from SIT_tool.pyflask.lib.readconfig import *
#from SIT_tool.pyflask.lib.myredis import RedisQueue
from SIT_tool.pyflask.lib.readconfig import getdb
from SIT_tool.pyflask.lib.readconfig import getsql
from SIT_tool.pyflask.lib.readconfig import getredis

# cluster = [
# 	{'host' : '10.203.238.172', 'port' : 8080},
# 	{'host' : '10.203.238.173', 'port' : 8080}
# ]
# password='awmpsnyc5psr5qny'
# r= StrictRedisCluster(startup_nodes=cluster,decode_responses=True,password='awmpsnyc5psr5qny')




def redis_cluster():
	redis_nodes = [{'host': '10.203.168.94', 'port': 8080},
				   {'host': '10.203.168.97', 'port': 8080}
				   ]
	
	try:
		rc = StrictRedisCluster(startup_nodes=redis_nodes,decode_responses=True, password='sf123456')


	except Exception as e:
		print("Connect Error!")
		sys.exit(1)




#redis_cluster()

class myRedis(object):
	def __init__(self, redis_type=None, **args):
		if redis_type == "cluster":
			self.r_conn = StrictRedisCluster(**args)
		else:
			self.pool = redis.ConnectionPool(**args)
			self.r_conn = redis.Redis(connection_pool=self.pool)


if __name__ == '__main__':

#单点
	host = '10.203.62.40'
	password = 'yzjy9kerhsku4by1'
	port = 8080
	db = 1
	conn_dict={'host': host, 'port': port,'password':password,'db':db}
	conn_dict2=getredis("ak_sit")
	myredis = myRedis(**conn_dict)
	print(myredis.r_conn.get("project"))
#cluster
	# redis_nodes = [{'host': '10.203.168.94', 'port': 8080},
	# 		   {'host': '10.203.168.97', 'port': 8080}
	# 		   ]
	# password='sf123456'
	# conn_dict={"startup_nodes":redis_nodes,'password':password,'decode_responses':'True'}
	# #conn_dict2=getredis("ak_cluster")
	# print(getredis("ak_cluster"))
	# print(getredis("ak_sit"))

	#redis_type='cluster'
	#myredis = myRedis(redis_type,**conn_dict2)
	#print(myredis.r_conn.get("test"))




