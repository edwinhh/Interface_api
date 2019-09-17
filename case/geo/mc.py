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


class mc(TestAbstract):
	def test_1(self):
		data = {'address': '竟陵镇钟惺大道12号天门移动分公司', \
				'city':'天门市', \
				'opt':'mc1',\
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('1post: ',res)
		#self.assertEqual("rh",res['result']['src'])

	def test_2(self):
		data = {'address': '湖北省天门市竟陵镇钟惺大道12号天门移动分公司', \
				'city':'', \
				'opt':'mc1', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('2get: ',res)
		#self.assertEqual("rh", res['result']['src'])

	#
	def test_3(self):
		data = {'address': '河北省定州市大辛庄镇裕华西路728号康泰大厦6层601', \
				'opt':'mc1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('3: ',res)
		#self.assertEqual("rh", res['result']['src'])

	def test_4(self):
		data = {'address': '大辛庄镇裕华西路728号康泰大厦6层601', \
				'city': '定州市', \
				'opt':'mc1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('4: ',res)
		#self.assertEqual("rh", res['result']['src'])
		
		
	def test_5(self):
		data = {'address': '海南省乐东黎族自治县乐东黎族自治县海南 省直辖 乐东县  九所镇山海湾七期(乐东监狱旁景和花园)1号楼1813', \
				'opt': 'mc1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('5: ',res)

	def test_6(self):
		data = {'address': '九所镇山海湾七期(乐东监狱旁景和花园)1号楼1813', \
				'city': '乐东黎族自治县', \
				'opt': 'mc1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('6: ',res)
#
	def test_7(self):
		data = {'address': '乐东自治县|乐东县|乐东', \
				'city': '乐东黎族自治县', \
				'opt': 'mc1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('7: ',res)
#
	def test_8(self):
		data = {'address': ' 河北省辛集市辛集镇兴华路北段鹿城商城北行50米路西', \
				'opt': 'mc1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('8: ',res)
#
	def test_9(self):
		data = {'address': '辛集镇兴华路北段鹿城商城北行50米路西', \
				'city': '辛集市', \
				'opt': 'mc1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('9: ',res)
		# self.assertEqual(1,res['status'])
#
	def test_10(self):
		data = {'address': '新疆维吾尔自治区五家渠市人民路街道新疆五家渠人民路贝鸟语城合院8-1', \
				'city': '', \
				'opt': 'mc1', \
				'ak': ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('10: ',res)
		
#		self.assertEqual(1,json.loads(res)['status'])
#
	def test_11(self):
		def test_10(self):
			data = {'address': '新疆维吾尔自治区五家渠市人民路街道新疆五家渠人民路贝鸟语城合院8-1', \
					'city': '五家渠市', \
					'opt': 'mc1', \
					'ak': ak}
			res = self.requestGET(url, data)
			p.append(data)
			r.append(res)
			print('10: ', res)

		
	def test_12(self):
		data = {'address': '湖北省仙桃市杨林尾镇兴隆村二组65号', \
				'opt':'mc1', \
				'city':'', \
				'normal':'0', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('12: ',res)

	def test_13(self):
		data = {'address': '杨林尾镇兴隆村二组65号', \
				'opt':'mc1', \
				'city':'仙桃市', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('13: ',res)

	def test_14(self):
		data = {'address': '广东省东莞市大朗镇犀牛陂村正坑一区四巷118号', \
				'opt':'mc1', \
				'city':'东莞市', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('14: ',res)

	def test_15(self):
		data = {'address': '广东省中山市古镇镇永昌北街八巷一号', \
				'opt':'mc1', \
				'city':'中山市', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('15: ',res)

	def test_16(self):
		data = {'address': '海南省儋州市那大镇大地小区路口天安财险', \
				'opt':'mc1', \
				'city':'儋州市', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('15: ',res)

	def test_17(self):
		data = {'address':'北京北京市西城区新街口北大街59号万丰珠宝交易中心5010蔡晶收18612256180 \
					北京北京市西城区新街口北大街59号万丰珠宝交易中心5010蔡晶收18612256180', \
				'opt':'mc1', \
				'ak': ak
				}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('17: ',res)

	def test_18(self):
		'''city字段x s s'''
		data = {'address': '香港大学', \
				'opt':'mc1', \
				'city':'香港', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('18: ',res)

	def test_19(self):
		data = {'address': '香港大学', \
				'opt':'mc1', \
				'city':'香港', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('19: ',res)

	def test_20(self):
		data = {'address': 'ED四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
				'opt':'mc1', \
				'cc': '1', \
				'city':'@#$%^YJKM<>?\n""', \
				'normal':'1', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('20: ',res)

	def test_21(self):
		data = {'address': 'ED?\##', \
				'opt':'mc1', \
				'cc': '1', \
				'city':'##@#$%^YJKM<>?\n""', \
				'normal':'1', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('21: ',res)



	def test_22(self):
		data = {'address': '四川省成都市双流县天府新区剑南大道南段牧华路三段中信城左岸二栋二单元1506', \
				'city':'', \
				'opt': 'mc1', \
				'ak':ak}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('22: ',res)

	def test_23(self):
		data = {'address': '赣州市经济技术开发区迎宾大道74号', \
				'city':'赣州市', \
				'opt':'mc1', \
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
	suite.addTest(unittest.makeSuite(mc))
	runner = unittest.TextTestRunner()
	runner.run(suite)




	# suite = unittest.TestSuite()
	# suite.addTest(gis_geo1("test_5"))
	# runner = unittest.TextTestRunner()
	# runner.run(suite)



