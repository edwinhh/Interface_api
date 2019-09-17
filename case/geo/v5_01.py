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


class v5_01(TestAbstract):
	def test_1(self):
		data = {'address': '湖北省天门市天门市黄潭镇致富南路18号', \
				'city':'728', \
				'opt': '', \
				'ak':'70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('1: ',res)
		print (type(res))
		#self.assertEqual(0,res['status'])
		#self.assertEqual('yy', res['result']['src'])

	def test_2(self):
		data = {'address': '甘肃省酒泉市肃州区雄关路转十号基地', \
				'city':'937', \
				'opt': '', \
				'ak':'70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('2: ',res)
		self.assertEqual(1,res['status'])

	def test_3(self):
		data = {'address': '海南省澄迈县澄迈县金江镇文明路227号', \
				'city':'898', \
				'opt': '', \
				'ak':'70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('3: ',res)

	def test_4(self):
		data = {'address': '新疆维吾尔自治区五家渠市五家渠市人民路街道人民北路138号中国银行农业银行', \
				'city':'994', \
				'ak':'70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)

		p.append(data)
		r.append(res)
		print('4: ',res)

	def test_5(self):
		data = {'address': '湖北省天门市天门市黄潭镇致富南路18号', \
				'city':'429004/429005/429006', \
				'ak':'70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('5: ',res)

	def test_6(self):
		data = {'address': '甘肃省酒泉市肃州区雄关路转十号基地', \
				'city':'620200/620900', \
				'ak':'70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('6: ',res)

	def test_7(self):
		data = {'address': '海南省澄迈县澄迈县金江镇文明路227号', \
				'city':'460100/460400/469002/469005/469021/469022/469023/469024/469025/469026/469030', \
				'ak':'70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('7: ',res)

	def test_8(self):
		data = {'address': '新疆维吾尔自治区五家渠市五家渠市人民路街道人民北路138号中国银行农业银行', \
				'city':'652300/659004', \
				'ak':'70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('8: ',res)

	def test_9(self):
		data = {'address': '陕西省西安市长安区兴隆社区二区13号楼', \
				'city': '851/2F029', \
				'ak': '70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('9: ',res)
		# self.assertEqual(1,res['status'])


	def test_10(self):
		data = {'address': '陕西省西安市长安区兴隆社区二区13号楼', \
				'city': '440100/440300', \
				'ak': '70231a4fa9c047d381cc55c8ff75e0bf'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('10: ',res)
	

	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r,"get")






if __name__ == "__main__":

	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(v5_01))
	runner = unittest.TextTestRunner()
	runner.run(suite)




	# suite = unittest.TestSuite()
	# suite.addTest(gis_geo1("test_5"))
	# runner = unittest.TextTestRunner()
	# runner.run(suite)




