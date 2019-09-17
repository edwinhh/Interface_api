# -*- coding: utf-8 -*-
import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *


url = 'http://gis-int.intsit.sfdc.com.cn:1080/geo/std'
#url=geturl("geo")
ak=getak("ak")

name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class v4_02(TestAbstract):
	def test_1(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'755', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('1: ',res)
		print (type(res))
		self.assertEqual(0,res['status'])
		self.assertEqual('yy', res['result']['src'])

	def test_2(self):
		data = {'address': '北京', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('2: ',res)
		self.assertEqual(1,json.loads(res)['status'])

	def test_3(self):
		data = {'address': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('3: ',res)

	def test_4(self):
		data = {'address': '美国', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)

		p.append(data)
		r.append(res)
		print('4: ',res)

	def test_5(self):
		data = {'address': '<scrpit>alert()</scrpit>', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('5: ',res)

	def test_6(self):
		data = {'address': '中国广东省深圳市南山区海德3道3号', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('6: ',res)

	def test_7(self):
		data = {'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('7: ',res)

	def test_8(self):
		data = {'address': '  !@#$%^&*:":"', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('8: ',res)

	def test_9(self):
		data = {'address': '  深圳市南山区海德3道3号', \
				'opt': 'gd2', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('9: ',res)
		# self.assertEqual(1,res['status'])

	def test_10(self):
		data = {'address': '  深圳市南山区海德3道3号', \
				'city': '420100', \
				'city': '北京', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('10: ',res)
		self.assertEqual(1,res['status'])

	def test_11(self):
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt': 'sf3', \
				'cc': '1', \
				'city':'四川', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('11: ',res)

	def test_12(self):
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'city':'四川', \
				'normal':'0', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('12: ',res)

	def test_13(self):
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt': '', \
				'cc': 'a', \
				'city':'511002', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('13: ',res)

	def test_14(self):
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt': 'sf30', \
				'cc': '', \
				'city':'四川', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('14: ',res)

	def test_15(self):
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt': 'sf30', \
				'cc': '1', \
				'city':'四川', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('15: ',res)

	def test_16(self):
		data = {'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('16: ',res)

	def test_17(self):
		data = {'address':'北京北京市西城区新街口北大街59号万丰珠宝交易中心5010蔡晶收18612256180 \
					北京北京市西城区新街口北大街59号万丰珠宝交易中心5010蔡晶收18612256180', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'
				}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('17: ',res)

	def test_18(self):
		'''city字段x s s'''
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt': 'sf3', \
				'cc': '1', \
				'city':'<scrpit>alert</scrpit>', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('18: ',res)

	def test_19(self):
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt': 'sf30', \
				'cc': '1', \
				'city':'四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('19: ',res)

	def test_20(self):
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt': 'sf3', \
				'cc': '1', \
				'city':'@#$%^YJKM<>?\n""', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)

	def test_20(self):
		data = {'address': '广东省', \
				'opt': 'sw2', \
				'cc': '1', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)

	def test_20(self):
		data = {'address': '广东省中山市小榄镇民安北路', \
				'opt': 'sw2', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)


	def test_21(self):
		data = {'address': '江苏省苏州市张家港市人民中路近市政府民服务中心', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)

	def test_22(self):
		data = {'address': '四川省成都市双流县天府新区剑南大道南段牧华路三段中信城左岸二栋二单元1506', \
				'city':'',\
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('22: ',res)

	def test_23(self):
		data = {'address': '赣州市经济技术开发区迎宾大道74号', \
				'city':'赣州市', \
				'opt': '', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('23: ',res)



	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r,"get")






if __name__ == "__main__":

	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(v4_02))
	runner = unittest.TextTestRunner()
	runner.run(suite)




	# suite = unittest.TestSuite()
	# suite.addTest(gis_geo1("test_5"))
	# runner = unittest.TextTestRunner()
	# runner.run(suite)




