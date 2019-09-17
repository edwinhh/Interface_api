# -*- coding: utf-8 -*-
import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *
import json
sys.path.append('e:/project/Interface_api-master')
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://GIS-RSS-PROXY.intsit.sfdc.com.cn:1080/tip'
url='http://gis-ass-oms-gk.sit.sf-express.com/pub/redis/get'
#url='http://10.202.73.142:8080/sch_code'
#url='http://10.117.156.14:8080/tip'
#url='http://10.202.95.115:9090/tip'

name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]

class oms_ak(TestAbstract):
	def test_1(self):
		data = {'key': '*8bb09e5e110845f39a000391668e3e80'}
		res = self.requestGET(url, data)
		#res=json.dumps(res)
		p.append(data)
		r.append(res)
	
	def test_2(self):
		data = {'key': 'gisak@#PASS#|ADD-TC2|ebe9f2fd1f1e41ffbfbc2fc643b96c3b AND 6148=1254|limitDayVolumn|2018-11-14'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	
	def test_3(self):
		data = {'key': 'gisak@GEOEX-WS|-6818 OR 8333=8333|dayTrackOfMinute|20181114'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		
	def test_4(self):
		data = {'key': 'gisak@py3'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)

	def test_5(self):
		data = {'key': '8bb09e5e110845f39a000391668e3e80'}
		res = self.requestGET(url, data)
		print(res)
		#res=json.dumps(res)
		p.append(data)
		r.append(res)
		
	def test_6(self):
		data = {'key': '*'}
		res = self.requestGET(url, data)
		print(res)
		#res=json.dumps(res)
		p.append(data)
		r.append(res)

	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r,"get")


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(oms_ak))
	runner = unittest.TextTestRunner()
	runner.run(suite)
#
#
#
#
	# suite = unittest.TestSuite()
	# suite.addTest(gis_geo1("test_5"))
	# runner = unittest.TextTestRunner()
	# runner.run(suite)








