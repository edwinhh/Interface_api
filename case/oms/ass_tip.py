# -*- coding: utf-8 -*-
import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *
sys.path.append('e:/project/Interface_api-master')
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://GIS-RSS-PROXY.intsit.sfdc.com.cn:1080/tip'
#url='http://gis-ass-tip.intsit.sfdc.com.cn:1080/tip'
url='http://10.202.73.142:8080/tip'
#url='http://10.117.156.14:8080/tip'
#url='http://10.202.95.115:9090/tip'

name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class ass_tip(TestAbstract):


	def test_1(self):
		data = {'q': '深圳东海王大厦', \
				'opt':'sch1',\
				'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		
		#self.assertEqual(0,res['status'])

	def test_2(self):
		data = {'q': '  深圳 观澜街道 观光路鹏星行奔驰4s店对面', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		
		# self.assertEqual(1,res['status'])

	def test_3(self):
		data = {'q': '深圳龙城街道黄阁路天安数码城2栋B座1201-1', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_4(self):
		data = {'q': '！@#￥%……&<M>\n""', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		

	def test_5(self):
		data = {'q': '美国四川广东', \
				'city':'四川',\
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_6(self):
		data = {'q': '', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		


	def test_7(self):
		data = {'q': '&', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test8(self):
		data = {
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		print('8: ',res)

	def test_9(self):
		data = {'q': '四川', \
				'city': '755', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_10(self):
		data = {'q': '深圳市南山区海德3道3号', \
				'city': '755', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_11(self):
		data = {'q': '深圳市南山区海德3道', \
				'city': '深圳', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)



	def test_12(self):
		data = {'q': '深圳市南山区海德3道', \
				'city': '&', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_13(self):
		data = {'q': '深圳市南山区海德3道', \
				'opt': 'sch1', \
				'city': '高德高德高德高德高德高德高德高德高德高德高德高德高德高德高德高德', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_14(self):
		data = {'q': '深圳市南山区海德3道', \
				'city': '', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_15(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				'opt': 'sch1', \
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
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_18(self):
		data = {'q': '江苏省深圳市龙岗区宝岭花园北区a栋', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_19(self):
		data = {'q': '\\', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_20(self):
		data = {'q': '&', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_21(self):
		data = {'q': '1080', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_22(self):
		data = {'q': '"1"=="1"', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_23(self):
		data = {'q': '深圳市龙岗区宝岭花园北区a栋', \
				'opt': 'sch1', \
				'city': '755', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_24(self):
		data = {'q': '深圳市龙岗区宝岭花园宝岭花园北区a栋a栋b栋', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_25(self):
		data = {'q': '深圳市深圳市深圳市龙岗区宝岭花园北区a栋', \
				'opt': 'sch1', \
				'city': '755', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_26(self):
		data = {'q': '深圳市龙岗区龙岗区龙岗区龙岗区宝岭花园北区a栋', \
				'opt': 'sch1', \
				'city': '755', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_27(self):
		data = {'q': '1- - - -', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_28(self):
		data = {'q': '广东省广州市花都区建设北路71永发商务中心', \
				'opt': 'sch1', \
				'city': '广州市', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_29(self):
		data = {'q': '广东省广州市白云区白云区白云湖街夏茅综合管理队', \
				'opt': 'sch1', \
				'city': '广州市', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	
	def test_30(self):
		data = {'q': '广东省 广州市荔湾区海中北路海中七路交叉口兆丰种苗', \
				'opt': 'sch1', \
				'city': '广州市', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_31(self):
		data = {'q': '环市东路326-1号', \
				'opt': 'sch1', \
				'city': '090211212121212121212', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_32(self):
		data = {'q': '海', \
				'opt': 'sch1', \
				'city': '广州市', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_33(self):
		data = {'q': '上海浦东', \
				'opt': 'sch1', \
				'city': '上海', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_34(self):
		data = {'q': '东莞市东莞大学', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_35(self):
		data = {'q': '北京海淀区', \
				'opt': 'sch1', \
				'city': '北京', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_36(self):
		data = {'q': '杭州西湖', \
				'city': '杭州', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_36(self):
		data = {'q': '民安北路', \
				'city': '中山市', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_37(self):
		data = {'q': '东街新华书店', \
				'city': '河南信阳息县', \
				'opt': 'sch1', \
				'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_38(self):
		data = {'q': '深圳福田中心<script>alert(1)</script>城', \
				'opt': 'sch1', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_39(self):
		data = {'q': '深圳福田中心<script>alert(1)</script>城', \
				'opt': 'sch1', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_40(self):
		data = {'q': '北京北京大学', \
				'opt': 'sch1', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_41(self):
		data = {'q': '天津南开大学', \
				'opt': 'sch1', \
				'city':'天津',\
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_42(self):
		data = {'q': '交通大学', \
				'opt': 'sch1', \
				'city': '上海', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_43(self):
		data = {'q': '重庆解放路', \
				'opt': 'sch1', \
				'city': '重庆', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_44(self):
		data = {'q': '广东省,深圳市,龙岗区,南湾街道,吉园路', \
				'opt': 'sch1', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	

	def test_45(self):
		data = {'q': '深圳福田中心<script>alert(1)</script>城', \
				'opt': 'sch1', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_46(self):
		data = {'q': '大望村131号,1,广东省,深圳市,罗湖区,东湖街道,梧桐山', \
				'opt': 'sch1', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)


	def test_47(self):
		data = {'q': '罗湖区东湖街道梧桐山大望村131号', \
				'opt': 'sch1', \
				'city':'广东省深圳市',\
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
	
	def test_48(self):
		data = {'q': '汉中市,河东店,sw-tcp,河东店镇', \
				'opt': 'sch1', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		

	def test_49(self):
		data = {'q': '广州市金钟金钟横路', \
				'opt': 'sch1', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		


	def test_50(self):
		data = {'q': '邯郸市,稽山公寓', \
				'opt'
				: 'sch1', \
				'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
		res = self.requestGET(url, data)
		p.append(data)
		r.append(res)
		


	@classmethod
	def tearDownClass(clz):
		reporttxt(name,url, p, r,"get")


if __name__ == "__main__":
#
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(ass_tip))
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








