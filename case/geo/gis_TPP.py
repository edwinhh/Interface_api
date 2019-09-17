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


class gis_TPP(TestAbstract):
	def test_1(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'深圳', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('1: ',res)
		self.assertEqual(0,res['status'])
		self.assertEqual('yy', res['result']['src'])

	def test_2(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('2: ',res)
		self.assertEqual(0,res['status'])

	def test_3(self):
		data = {'address': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('3: ',res)
		self.assertEqual(1, res['status'])

	def test_4(self):
		data = {'address': '香港大学', \
				'city': '香港', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('4: ',res)
		self.assertEqual('sf', res['result']['src'])

	def test_5(self):
		data = {'address': '深圳蛇口<scrpit>alert()</scrpit>', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('5: ',res)
		self.assertEqual('yy', res['result']['src'])

	def test_6(self):
		data = {'address': '中国广东省深圳市南山区海德3道3号', \
				'opt': 'sw1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('6: ',res)
		self.assertEqual('sw', res['result']['src'])

	def test_7(self):
		data = {'address': '中国广东省深圳市南山区海德3道3号', \
				'opt': 'sf1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('7: ',res)
		self.assertEqual('sf', res['result']['src'])

	def test_8(self):
		data = {'address': '中国广东省深圳市南山区海德3道3号', \
				'opt': 'yy1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('8: ',res)
		self.assertEqual('yy', res['result']['src'])

	def test_9(self):
		data = {'address': '中国广东省深圳市南山区海德3道3号', \
				'opt': 'gf1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('9: ',res)
		self.assertEqual('gf', res['result']['src'])
		# self.assertEqual(1,res['status'])

	def test_10(self):
		data = {'address': '中国广东省深圳市南山区海德3道3号', \
				'opt': 'bd2', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('10: ',res)
		self.assertEqual('bd', res['result']['src'])

	def test_11(self):
		data = {'address': '中国广东省深圳市南山区海德3道3号', \
				'opt': 'gd2', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('11: ',res)
		self.assertEqual('gd', res['result']['src'])

	def test_12(self):
		data = {'address': '中国广东省深圳市南山区海德3道3号', \
				'opt': 'tc2', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('12: ',res)
		self.assertEqual('tc', res['result']['src'])

	def test_13(self):
		data = {'address': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
				'opt': 'sf30', \
				'span': '1', \
				'city': '%E6%B7%B1%E5%9C%B3&', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('13: ',res)
		self.assertEqual(0, res['status'])

	def test_14(self):
		data = {'address': '南山区蛇口海上世界', \
				'opt': 'sf30', \
				'cc': '', \
				'city':'755', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('14: ',res)
		self.assertEqual(0, res['status'])

	def test_15(self):
		data = {'address': '成都市人民南路二段18号川信大厦36层', \
				'city': '成都市/资阳市/眉山市', \
				'span': '1', \
				'opt': 'sf30', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('15: ',res)
		self.assertEqual(0, res['status'])

	def test_16(self):
		data = {'address': '四川省 成都市/资阳市/眉山市 成都市人民南路二段18号川信大厦36层', \
				'city': '成都市', \
				'span': '1', \
				'opt': 'sf30', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('16: ',res)
		self.assertEqual(0, res['status'])

	def test_17(self):
		data = {'address': '广东省深圳市福田区，顺丰自取。755AC点部', \
				'city': '', \
				'span': '1', \
				'opt': 'sf30', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('17: ',res)
		self.assertEqual('wd', res['result']['src'])

	def test_18(self):
		'''city字段x s s'''
		data = {'address': '994D00,028BG', \
				'city': '510131/510100/510183', \
				'span': '1', \
				'opt': 'sf30', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('18: ',res)
		self.assertEqual('wd', res['result']['src'])

	def test_19(self):
		data = {'address': '湖南省--长沙市-雨花区--', \
				'opt': 'sf30', \
				'city':'', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('19: ',res)
		self.assertEqual(0, res['status'])

	def test_20(self):
		data = {'address': '河池市凤山县++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*************************&&&&&&&&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', \
				'opt': 'sf30', \
				'city':'河池市', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)
		self.assertEqual(0, res['status'])

	def test_21(self):
		data = {'address': '狮山镇工业园B区科韵北路1号{车间(A区）（B区）}', \
				'opt': 'sf30', \
				'city': '佛山市', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('21: ',res)
		self.assertEqual(0, res['status'])


	def test_22(self):
		data = {'address': '松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期2栋2单元', \
				'opt': 'sf30', \
				'city': '深圳市', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('22: ',res)
		self.assertEqual(1, res['status'])



	def test_23(self):
		data = {'address': '', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('23: ',res)
		self.assertEqual(1, res['status'])


	def test_24(self):
		data = {'address': '香港特别行政区駱克道160-174號越秀大廈21F2102号HEIDELBERG  YUE  XIU  ENTERPRISE  CONSU', \
				'city':'香港特别行政区',\
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('24: ',res)
		self.assertEqual(0, res['status'])


	def test_25(self):
		data = {'address': 'DE##EwA9TkQX2%2BH%2BllV%2B6CDVsifehLFqlyzox7VYzvNS5W%2FBZQR22I53oN7cuLKZE9nWCStBFg%3D%3D', \
				'city':'深圳', \
				'span': '1', \
				'opt':'sf30',\
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestPOST(url, data)
		p.append(data)
		r.append(res)
		print('25: ',res)
		self.assertEqual(0, res['status'])

	def test_26(self):
		data = {'address': '软件产业基地', \
				'opt': 'sf60', \
				'city': '深圳', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('26: ',res)
		self.assertEqual('sf', res['result']['src'])
		
	def test_27(self):
		data = {'address': '苏州河', \
				'opt': 'sf60', \
				'city': '苏州', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('27: ',res)
		self.assertEqual('sf', res['result']['src'])
		
	def test_28(self):
		data = {'address': '深圳福田区海上世界', \
				'opt': 'sf30', \
				'span': '1', \
				'city': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('28: ',res)
		self.assertEqual('yy', res['result']['src'])

	def test_29(self):
		data = {'address': '非洲', \
				'opt': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('29: ',res)
		self.assertEqual(0, res['status'])
		
	def test_30(self):
		data = {'address': 'DE##EwA9TkQX2%2BH%2BllV%2B6CDVsifehLFqlyzox7VYzvNS5W%2FBZQR22I53oN7cuLKZE9nWCStBFg%3D%3D', \
				'city':'深圳', \
				'opt':'sf30',\
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('30: ',res)
		self.assertEqual(1, res['status'])

	def test_31(self):
		data = {'address': 'DE##EwA9TkQX2%2BH%2BllV%2B6CDVsifehLFqlyzox7VYzvNS5W%2FBZQR22I53oN7cuLKZE9nWCStBFg%3D%3D', \
				'city':'', \
				'opt':'sf30',\
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestPOST(url, data)
		p.append(data)
		r.append(res)
		print('31: ',res)
		self.assertEqual(0, res['status'])
		
	def test_32(self):
		data = {'address': 'http://gis-rss.intsit.sfdc.com.cn:1080/geo', \
				'opt': '', \
				'city': '755aM001', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('32: ',res)
		self.assertEqual(0, res['status'])
		
	def test_33(self):
		data = {'address': '深圳万里工业区“万”', \
				'opt': 'sf30', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('33: ',res)
		self.assertEqual(0, res['status'])
		
	def test_34(self):
		data = {'address': '	€£¢ªÊË®£赟赓檿™®℃∴〆々★', \
				'opt': 'sf30', \
				'city': '440204', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('34: ',res)
		self.assertEqual(1, res['status'])
		
	def test_35(self):
		data = {'address': '深圳福田区海上世界', \
				'opt': 'sf30', \
				'span': '0', \
				'city': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('35: ',res)
		self.assertEqual(0, res['status'])
	
	def test_36(self):
		data = {'address': '深圳市^蛇口^海上世界^海上世界', \
				'opt': 'sf30', \
				'city': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('36: ',res)
		self.assertEqual(0, res['status'])
		
	def test_37(self):
		data = {'address': '深圳市^蛇口^海上世界^海上世界', \
				'opt': 'sf30', \
				'city': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('37: ',res)
		self.assertEqual(0, res['status'])

	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r,"get")



if __name__ == "__main__":

	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(gis_TPP))
	runner = unittest.TextTestRunner()
	runner.run(suite)




	# suite = unittest.TestSuite()
	# suite.addTest(gis_geo1("test_5"))
	# runner = unittest.TextTestRunner()
	# runner.run(suite)




