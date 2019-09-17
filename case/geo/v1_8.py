import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url=geturl("geo")
ak=getak("ak")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class v1_8(TestAbstract):
    def test_1(self):
        data = {'address': '上海市宝山区杨泰路99弄', \
                'opt': 'sf60', \
                'city':'上海',\
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'address': '广东省广州市番禺区化龙镇坎头街12巷', \
                'opt': 'sf60', \
                'city': '广州市', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'address': '上海市宝山区杨泰路99弄', \
                'opt': 'sf60', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'address': '广东省广州市番禺区化龙镇坎头街12巷', \
                'opt': 'sf60', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('4: ', res)

    def test_5(self):
        data = {'address': '辽宁省锦州市经济技术开发区玉山路20号', \
                'opt': 'sf60', \
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_12(self):
        data = {'address': '成都高新经济开发区', \
                'city':'',\
                'opt': 'sf60', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('12: ', res)

    def test_6(self):
        data = {'address': '济南市科技园', \
                 'opt': 'sf60', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ', res)

    def test_7(self):
        data = {'address': '苏州市音乐厅', \
                'opt': 'sf60', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('7: ', res)

    def test_8(self):
        data = {'address': '深圳市软件产业基地', \
                'opt': 'sf60', \
                'city': '深圳', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('8: ', res)

    def test_9(self):
        data = {'address': '', \
                'opt': 'sf60', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('9: ', res)

    def test_10(self):
        data = {'address': '苏州市音乐厅', \
                'opt': 'sf60', \
                'city': '苏州', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'address': '洛阳市人民检察院', \
                'opt': 'sf60', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_13(self):
        data = {'address': '!@#$%^&*  _+":L<', \
                'opt': 'sf60', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ', res)

    def test_14(self):
        data = {
                'opt': 'sf60', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)

    def test_15(self):
        data = {
                'opt': 'sf60', \
                'city': '河南省|驻马店市|新蔡县', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'address': '<scrpit>alert("深圳")</scrpit>', \
                'opt': 'sf60', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'address': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': 'sf60', \
                'city': '%E6%B7%B1%E5%9C%B3&', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'address': '海上世界', \
                'opt': 'sf60', \
                'city': '广东省|深圳市|南山区', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'address': '海上世界', \
                'opt': 'sf60', \
                'span':'1',\
                'city': '广东省|深圳市|福田区', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)



    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(v1_8))
    runner = unittest.TextTestRunner()
    runner.run(suite)