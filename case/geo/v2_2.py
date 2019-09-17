import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url=geturl("geo")
ak=getak("ak")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class v2_2(TestAbstract):
    def test_1(self):
        data = {'address': '广东省深圳市福田区，顺丰自取。755AC点部', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'address': '西门路信箱1站755U', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'address': '广东省深圳市福田区，顺丰自取。', \
                'city':'深圳|南山区',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'address': '755U', \
                'city':'西安市/咸阳市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        start=time.time()
        res = self.requestGET(url, data)
        end=time.time()
        p.append(data)
        r.append(res)
        print('4: ', res)
        print('time: ', end-start)

    def test_5(self):
        data = {'address': '994D002,712CT,P631CSA,991J,991E', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('5: ', res)

    def test_6(self):
        data = {'address': ' 994D002，994D002', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ', res)



    def test_7(self):
        data = {'address': '四川省 成都市/资阳市/眉山市 成都市人民南路二段18号川信大厦994D002层', \
                'city':'成都市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('7: ', res)

    def test_8(self):
        data = {'address': '028BG', \
                'city':'眉山市/资阳市/成都市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('8: ', res)

    def test_9(self):
        data = {'address': '994D00,028BG', \
                'city': '510131/510100/510183', \
                'span': '1', \
                 'opt': 'sf30', \
                 'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('9: ', res)

    def test_10(self):
        data = {'address': '994D002,712CT,P631CSA,991J,991E', \
                'city':'成都市/资阳市/眉山市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'address': '994D002,712CT,P631CSA,991J,991E', \
                'city':'成都市/资阳市/眉山市', \
                'exact':'1', \
                'cb':'__cx1',\
                'opt': 'gd2', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_13(self):
        data = {'address': '994D002,712CT,P631CSA,991J,991E', \
                'city':'成都市/资阳市/眉山市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ', res)

    def test_14(self):
        data = {'address': '四川省 成都市/资阳市/眉山市 成都市人民南路二段18号川信大厦36层', \
                'city': '', \
                'span': '1', \
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)

    def test_15(self):
        data = {
                'opt': 'gd2', \
                'city': '河南省|驻马店市|新蔡县', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'address': '<scrpit>alert("深圳")</scrpit>', \
                'opt': 'gd2', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'address': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': 'gd2', \
                'city': '%E6%B7%B1%E5%9C%B3&', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'address': '！@#￥%……：“', \
                'opt': 'gd2', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'address': '深圳万安村', \
                'opt': 'gd2', \
                'city': '<scrpit>alert(city)</scrpit>', \
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
    suite.addTest(unittest.makeSuite(v2_2))
    runner = unittest.TextTestRunner()
    runner.run(suite)