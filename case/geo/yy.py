import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url=geturl("geo")
ak=getak("ak")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]

class yy(TestAbstract):
    def test_1(self):
        data = {'address': '广东省深圳市南山区南园村新二坊18栋', \
                'opt': 'yy2', \

                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'address': '山东省潍坊市奎文区东风东街世纪泰华泰华中心22楼2205', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'address': '潮白河孔雀城英国宫4期春晓园', \
                'city': '131028', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'address': '燕郊开发区神威北路与燕灵路交汇处鑫乐汇购物广场 ', \
                'opt': '', \
                'city': '131082', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('4: ', res)

    def test_5(self):
        data = {'address': '辽宁省大连市高新园区数码路北段77号软景中心公寓楼一层大堂南门', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_12(self):
        data = {'address': '北京紫禁城', \
                'city':'010',\
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('12: ', res)

    def test_6(self):
        data = {'address': '上海外滩', \
                 'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ', res)

    def test_7(self):
        data = {'address': '新疆曼哈顿', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('7: ', res)

    def test_8(self):
        data = {'address': '三亚市榆亚路红郊社区1组内园中巷116号', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('8: ', res)

    def test_9(self):
        data = {'address': '非洲', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        self.append = p.append(data)
        r.append(res)
        print('9: ', res)

    def test_10(self):
        data = {'address': '深圳万里工业区“万”', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'address': '山东省东营区西四路66号粮食局1楼', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_13(self):
        data = {'address': '', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ', res)

    def test_14(self):
        data = {
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)

    def test_15(self):
        data = {
                'opt': '', \
                'city': '河南省|驻马店市|新蔡县', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'address': '<scrpit>alert("深圳")</scrpit>', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'address': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': '', \
                'city': '%E6%B7%B1%E5%9C%B3&', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'address': '！@#￥%……：“', \
                'opt': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'address': '福建省福州市平潭县916路翠园路口E➕1服装店二楼慕伦格尔美容院', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_20(self):
        data = {'address': '北京北京市朝阳区望京街10号方恒时代B座8层805室 北京博达昌正科技发展有限公司', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_21(self):
        data = {'address': '广东省广州市白云区均禾街道大布路口A区6号B3栋二楼    祥控电子', \
                'opt': '', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)




    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(yy))
    runner = unittest.TextTestRunner()
    runner.run(suite)



# 广东省深圳市南山区南园村新二坊18栋
# 广东省深圳市南山区南园村新二坊4号一楼鞋店
# 山东省潍坊市奎文区东风东街世纪泰华泰华中心22楼2205
# 广东省深圳市南山区南园村新四坊6号203
# 山东省东营区胜利建安公司对面友锋汽修
# 山西省太原市小店区南坪头村3号三毛物流大院
# 三亚市榆亚路红郊社区1组内园中巷116号
# 山西省太原市小店区国信嘉园15-604
# 山东省东营区西四路66号粮食局1楼
# 广东省潮州市潮安区庵埠镇振兴路37号