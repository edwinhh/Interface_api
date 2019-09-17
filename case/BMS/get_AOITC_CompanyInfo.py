# -*- coding: utf-8 -*-
import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *


#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url=geturl("bms")
url+="/search"
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]

#市场分析件量
class get_AOI_QuantityData(TestAbstract):
	def test_1(self):
		data = {
  				"app": "bdp-uss",
  				"searchId": 955,
  				"params": {
    			"from": 0,
    			"size": 10
  					}
				}
		res = self.requestspost(url, data)
		p.append(data)
		r.append(res)
		print('1: ',res)
		#self.assertIn('w', res['result']['src'])

	# def test_2(self):
	# 	data = {'address': '东滨路108栋317A', \
	# 			'cityCode':'440100'}
	# 	res = self.requestGET(url, data)
	# 	p.append(data)
	# 	r.append(res)
	# 	print('2get: ',res)
	#
	# def test_3(self):
	# 	data = {'address': '', \
	# 			'cityCode':''}
	# 	res = self.requestGET(url, data)
	# 	p.append(data)
	# 	r.append(res)
	# 	print('3: ',res)
	#
	# def test_4(self):
	# 	data = {'address': '广东省深圳市南山区南山区南大道1039-5号枫叶城市酒店天信巾心三楼319D室', \
	# 			'cityCode': ''}
	# 	res = self.requestGET(url, data)
	#
	# 	p.append(data)
	# 	r.append(res)
	# 	print('4: ',res)
	#
	# def test_5(self):
	# 	data = {'address': '', \
	# 			'cityCode':'440100'}
	# 	res = self.requestGET(url, data)
	# 	p.append(data)
	# 	r.append(res)
	# 	print('5: ',res)
	#
	# def test_6(self):
	# 	data = {'address': '!@#$%^&*  （），。、(),./', \
	# 			'cityCode':'440100'}
	# 	res = self.requestGET(url, data)
	# 	p.append(data)
	# 	r.append(res)
	# 	print('6: ',res)
	#
	#
	#
	# def test_7(self):
	# 	data = {'address': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
	# 			'cityCode':'511000'}
	# 	res = self.requestGET(url, data)
	# 	p.append(data)
	# 	r.append(res)
	# 	print('11: ',res)
	#
	#
	# def test_8(self):
	# 	data = {'address': '***E\D---------------++++++++++++++++++++++++++++++++++++++++\+', \
	# 			'cityCode': '511000'}
	# 	res = self.requestGET(url, data)
	# 	p.append(data)
	# 	r.append(res)
	# 	print('8: ',res)
	#
	#
	# def test_9(self):
	# 	data = {'address':'北京北京市西城区新街口北大街59号万丰珠宝交易中心5010蔡晶收18612256180 \
	# 				北京北京市西城区新街口北大街59号万丰珠宝交易中心5010蔡晶收18612256180', \
	# 			'cityCode': '110000'
	# 			}
	# 	res = self.requestPOST(url, data)
	# 	p.append(data)
	# 	r.append(res)
	# 	print('9: ',res)
	#
	# def test_10(self):
	# 	'''city字段x s s'''
	# 	data = {'address': '香港大学', \
	# 			'cityCode': '810000'}
	# 	res = self.requestPOST(url, data)
	# 	p.append(data)
	# 	r.append(res)
	# 	print('10: ',res)

	

	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r,"post")






if __name__ == "__main__":

	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(get_AOI_QuantityData))
	runner = unittest.TextTestRunner()
	runner.run(suite)




	# suite = unittest.TestSuite()
	# suite.addTest(gis_geo1("test_5"))
	# runner = unittest.TextTestRunner()
	# runner.run(suite)




