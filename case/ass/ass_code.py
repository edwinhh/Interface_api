# -*- coding: utf-8 -*-
import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *
sys.path.append('e:/project/Interface_api-master')
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://GIS-RSS-PROXY.intsit.sfdc.com.cn:1080/tip'
url='http://gis-ass-tip.intsit.sfdc.com.cn:1080/sch_code'
#url='http://10.202.73.142:8080/sch_code'
#url='http://10.117.156.14:8080/tip'
#url='http://10.202.95.115:9090/tip'

name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class ass_code(TestAbstract):


	def test_1(self):
		data = {'code': '深圳东海王大厦', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		
		#self.assertEqual(0,res['status'])

	def test_2(self):
		data = {'code': ' 755aM001', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		
		# self.assertEqual(1,res['status'])

	def test_3(self):
		data = {'code': '755aM001', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_4(self):
		data = {'code': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		

	def test_5(self):
		data = {'code': '<scrpit>alert()</scrpt>', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_6(self):
		data = {'code': 'shenzhen', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		


	def test_7(self):
		data = {'code': '深圳', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)

	

	def test8(self):
		data = {'code': ' ', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)

	def test_9(self):
		data = {'code': '755aM001 ', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_10(self):
		data = {'code': '&&', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_11(self):
		data = {'code': '\\', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)



	def test_12(self):
		data = {'code': '"1"="1"', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_13(self):
		data = {'code': '不存在的单元区域', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_14(self):
		data = {'code': '1080', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_15(self):
		data = {'code': 'http://10.202.73.142:8080/sch_code', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_16(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)

	def test_17(self):
		data = {
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	



	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r)


if __name__ == "__main__":
#
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(ass_code))
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








