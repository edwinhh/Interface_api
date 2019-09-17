# -*- coding: utf-8 -*-
import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *


#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url=geturl("geo")
ak=getak("ak")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class v4_01(TestAbstract):
	def test_1(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city':'天门市', \
				'opt':'bd0',\
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('1post: ',res)
		#self.assertEqual("rh",res['result']['src'])

	def test_2(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city':'天门市', \
				'opt':'bd1',\
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('2get: ',res)
		#self.assertEqual("rh", res['result']['src'])

	#
	def test_3(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'bd2', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('3: ',res)
		#self.assertEqual("rh", res['result']['src'])

	def test_4(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'gd1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('4: ',res)
		#self.assertEqual("rh", res['result']['src'])
		
		
	def test_5(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'gd2', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('5: ',res)

	def test_6(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'tc1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('6: ',res)

	def test_7(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'tc2', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('7: ',res)
#
	def test_8(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'yy1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('8: ',res)
#
	def test_9(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'yy2', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('9: ',res)
		# self.assertEqual(1,res['status'])
#
	def test_10(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'sw1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('10: ',res)
		
#		self.assertEqual(1,json.loads(res)['status'])
#
	def test_11(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'sw2', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('10: ',res)

		
	def test_12(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'gf0', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('12: ',res)

	def test_13(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'gf1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('13: ',res)

	def test_14(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'gf1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('14: ',res)

	def test_15(self):
		data = {'address': '软件产业基地', \
				'city': '深圳市', \
				'opt': 'rh0', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('15: ',res)

	def test_16(self):
		data = {'address': '软件产业基地', \
				'city': '深圳市', \
				'opt': 'rh1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('15: ',res)

	def test_17(self):
		data = {'address': '软件产业基地', \
				'city': '深圳市', \
				'opt': 'sf1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('17: ',res)

	def test_18(self):
		data = {'address': '软件产业基地', \
				'city': '深圳市', \
				'opt': 'sf0', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('18: ',res)

	def test_19(self):
		data = {'address': '软件产业基地', \
				'city': '深圳市', \
				'opt': 'sa0', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('19: ',res)

	def test_20(self):
		data = {'address': '软件产业基地', \
				'city': '深圳市', \
				'opt': 'sa1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)

	def test_21(self):
		data = {'address': '软件产业基地', \
				'city': '深圳市', \
				'opt': 'sa2', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('21: ',res)



	def test_22(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city': '天门市', \
				'opt': 'sf30', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('22: ',res)

	def test_23(self):
		data = {'address': '赣州市经济技术开发区迎宾大道74号', \
				'city':'赣州市', \
				'opt': '', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('23: ',res)



	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r,"get")






if __name__ == "__main__":

	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(v4_01))
	runner = unittest.TextTestRunner()
	runner.run(suite)




	# suite = unittest.TestSuite()
	# suite.addTest(gis_geo1("test_5"))
	# runner = unittest.TextTestRunner()
	# runner.run(suite)




