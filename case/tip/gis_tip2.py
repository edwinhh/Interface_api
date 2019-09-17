# -*- coding: utf-8 -*-
import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

url=geturl("tip")

#url=geturl("tip")

name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip2(TestAbstract):


	def test_1(self):
		data = {'q': '深圳市南山区海德3道3号深圳市南山区海德3道3号', \
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('1: ',res)
		#self.assertEqual(0,res['status'])

	def test_2(self):
		data = {'q': '软件产业基地', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('2: ',res)
		# self.assertEqual(1,res['status'])

	def test_3(self):
		data = {'q': '中国', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('3: ',res)

	def test_4(self):
		data = {'q': '！@#￥%……&<M>\n""', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('4: ',res)

	def test_5(self):
		data = {'q': '美国四川广东', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('5: ',res)

	def test_6(self):
		data = {'q': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('6: ',res)


	def test_7(self):
		data = {'q': '&', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('7: ',res)

	def test8(self):
		data = {
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('8: ',res)

	def test_9(self):
		data = {'q': '四川', \
				'city': '755', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('9: ',res)

	def test_10(self):
		data = {'q': '深圳市南山区海德3道3号', \
				'city': '755', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('10: ',res)

	def test_11(self):
		data = {'q': '深圳市南山区海德3道', \
				'city': '深圳', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('11: ',res)


	def test_12(self):
		data = {'q': '深圳市南山区海德3道', \
				'city': '&', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('12: ',res)

	def test_13(self):
		data = {'q': '深圳市南山区海德3道', \
				'city': '高德高德高德高德高德高德高德高德高德高德高德高德高德高德高德高德', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('13: ',res)

	def test_14(self):
		data = {'q': '深圳市南山区海德3道', \
				'city': '', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('14: ',res)

	def test_15(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('15: ',res)

	def test_16(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				'opt': 'sf0', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('16: ',res)

	def test_17(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('17: ',res)

	def test_18(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('18: ',res)

	def test_19(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				'opt': 'sa2', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('19: ',res)

	def test_20(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)

	def test_21(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('21: ',res)

	def test_22(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('22: ',res)

	def test_23(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				
				'city': '755', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('23: ',res)

	def test_24(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				'opt': '！@#￥%……&*（‘这是什么', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('24: ',res)

	def test_25(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				'opt': '', \
				'city': '755', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('25: ',res)

	def test_26(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				'city': '755', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('26: ',res)

	def test_27(self):
		data = {'q': '1- - - -', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('27: ',res)

	def test_28(self):
		data = {'q': '广东省广州市花都区建设北路71永发商务中心', \
				
				'city': '广州市', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('28: ',res)

	def test_29(self):
		data = {'q': '广东省广州市白云区白云区白云湖街夏茅综合管理队', \
				
				'city': '广州市', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('29: ',res)

	def test_30(self):
		data = {'q': '广东省 广州市荔湾区海中北路海中七路交叉口兆丰种苗', \
				
				'city': '广州市', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('30: ',res)

	def test_31(self):
		data = {'q': '环市东路326-1号', \

				'city': '广州市', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('31: ',res)

	def test_32(self):
		data = {'q': '海', \
				
				'city': '广州市', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('32: ',res)

	def test_33(self):
		data = {'q': '上海浦东', \
				'city': '上海', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('33: ',res)

	def test_34(self):
		data = {'q': '东莞市东莞大学', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('34: ',res)

	def test_35(self):
		data = {'q': '北京海淀区', \
				'city': '北京', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('35: ',res)

	def test_36(self):
		data = {'q': '杭州西湖', \
				'city': '杭州', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('36: ',res)

	def test_36(self):
		data = {'q': '民安北路', \
				'city': '中山市', \
				'opt':'bd1',\
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('36: ',res)

	def test_37(self):
		data = {'q': '东街新华书店', \
				'city': '河南信阳息县', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('37: ',res)

	def test_38(self):
		data = {'q': '深圳福田中心<script>alert(1)</script>城', \
				'city': '深圳', \
				'opt': '', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('38: ',res)

	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r,"get")




if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(tip2))
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








