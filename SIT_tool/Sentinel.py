import os,sys,unittest,time,json
import redis
from redis.sentinel import Sentinel
import hashlib
from rediscluster import StrictRedisCluster
from SIT_tool.pyflask.lib.readconfig import getredis

sentinel = Sentinel([('gis-ass-oms-gk1.cachesit.sfdc.com.cn', 8001),
                     ('gis-ass-oms-gk2.cachesit.sfdc.com.cn', 8001),
					 ('gis-ass-oms-gk3.cachesit.sfdc.com.cn', 8001)],
                    socket_timeout=1)

# 获取主服务器地址
master = sentinel.discover_master('GIS_ASS_OMS_REDIS_GK_C01')
print(master)
# 输出：('192.168.196.132', 6379)


# 获取从服务器地址
slave = sentinel.discover_slaves('GIS_ASS_OMS_REDIS_GK_C01')
print(slave)
# 输出：[('192.168.196.129', 6379)]


# 获取主服务器进行写入
master = sentinel.master_for('GIS_ASS_OMS_REDIS_GK_C01', socket_timeout=0.5, password='yzjy9kerhsku4by1', db=2)
w_ret = master.set('foo', 'bar')
# 输出：True

# 获取从服务器进行读取（默认是round-roubin,随机从多个slave服务中读取数据）
slave = sentinel.slave_for('GIS_ASS_OMS_REDIS_GK_C01', socket_timeout=0.5, password='yzjy9kerhsku4by1', db=2)
r_ret = slave.get('foo')
print(r_ret)
# 输出：bar
		
		
