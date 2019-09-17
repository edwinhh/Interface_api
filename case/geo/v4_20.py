# -*- coding: utf-8 -*-
import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *


#url = 'http://gis-int.intsit.sfdc.com.cn:1080/geo/std'
url=geturl("geo")
ak=getak("ak")

name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class v4_20(TestAbstract):
	def test_1(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'755', \
				'opt': 'my0', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('1: ',res)
		print (type(res))
		#self.assertEqual(0,res['status'])
		#self.assertEqual('yy', res['result']['src'])

	def test_2(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'755', \
				'opt': 'my1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('2: ',res)
		self.assertEqual(1,res['status'])

	def test_3(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'755', \
				'opt': 'my2', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('3: ',res)

	def test_4(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'755', \
				'opt': 'sa0', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)

		p.append(data)
		r.append(res)
		print('4: ',res)

	def test_5(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'755', \
				'opt': 'sa1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('5: ',res)

	def test_6(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'755', \
				'opt': 'sa2', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('6: ',res)

	def test_7(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'755', \
				'opt': 'sf50', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('7: ',res)

	def test_8(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'city':'755', \
				'opt': 'sf60', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('8: ',res)

	def test_9(self):
		data = {'address': '  深圳市南山区海德3道3号', \
				'opt': 'ts', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('9: ',res)
		# self.assertEqual(1,res['status'])

	def test_10(self):
		data = {'address': '  深圳市南山区海德3道3号', \
				'opt': 'ts', \
				'city': '北京', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('10: ',res)
		self.assertEqual(1,res['status'])

	def test_11(self):
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt': 'ts', \
				'city':'四川', \
				'normal':'1', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('11: ',res)

	def test_12(self):
		data = {'address': '  深圳市南山区海德3道3号', \
				'opt': '', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('12: ',res)

	def test_13(self):
		data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt': '', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('13: ',res)

	def test_14(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': 'mc1', \
				'ak':'73c0ad6b812c4c738f19a7278ff41971'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('14: ',res)

	def test_15(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': 'mc1', \
				'ak':'289eb7959c8c4909af668dea415b21b4'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('15: ',res)

	def test_16(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'6eeefc8dcc7c42869bd4f84a746f428d'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('16: ',res)

	def test_17(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'bba16126b28f4d54b922cd45ea739efb'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('17: ',res)

	def test_18(self):
		'''city字段x s s'''
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'20ac2e1414a04405abbfcef551c679c8'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('18: ',res)

	def test_19(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'d09d52aab81ec09976523a69206a75e2'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('19: ',res)

	def test_20(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'fe044a34e92c42f5a2996275ff0074d7'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)

	def test_20(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'918facc212c515ef03b5eab323ef5365'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)

	def test_20(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'3847482cb9844067b0e41767e1acf01f'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)


	def test_21(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'6e491612e0a54fa2a4f1940dfb2a3319'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)

	def test_22(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'ff80abd5ec0b427c91087baa9417c09f'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('22: ',res)

	def test_23(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'e6553bd0ce51b08f1aa8cc6cc42de767'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('23: ',res)

	def test_24(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'289eb7959c8c4909af668dea415b21b4'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('24: ',res)

	def test_25(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'73c0ad6b812c4c738f19a7278ff41971'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('25: ',res)
		
	def test_26(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'9bf4fc8ebdcd4a1eaa51b46484a4f645'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('26: ',res)
		
	def test_27(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'cfd8c287490d432f84eecfd8e95608ad'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('27: ',res)
		
	def test_28(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'a244e29144b9467ab9f6584a6912913e'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('28: ',res)
		
	def test_29(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'6e491612e0a54fa2a4f1940dfb2a3319'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('29: ',res)

	def test_30(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'4a881b947aa54c6a944a900351c1afa6'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('30: ',res)
		
	def test_31(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'fcbd1e819d3d463e9dd20a4317414468'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('31: ',res)
		
	def test_32(self):
		data = {'address': '深圳市南山区海德3道3号', \
				'opt': '', \
				'ak':'5353fa7971e545a996fc5c6996443a5e'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('32: ',res)

	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r,"get")






if __name__ == "__main__":

	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(v4_20))
	runner = unittest.TextTestRunner()
	runner.run(suite)




	# suite = unittest.TestSuite()
	# suite.addTest(gis_geo1("test_5"))
	# runner = unittest.TextTestRunner()
	# runner.run(suite)




