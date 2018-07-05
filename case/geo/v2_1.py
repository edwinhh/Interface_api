import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url=geturl("geo")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class v2_1(TestAbstract):
    def test_1(self):
        data = {'address': '广东省深圳市福田区，顺丰自取。755AC点部', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'address': '西门路信箱1站755U', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'address': '四川省 成都市/资阳市/眉山市 成都市人民南路二段18号川信大厦36层', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'address': '陕西省 西安市/咸阳市 未央区明光路南段阳光北郡小区', \
                'city':'西安市/咸阳市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        start=time.time()
        res = self.requestGET(url, data)
        end=time.time()
        p.append(data)
        r.append(res)
        print('4: ', res)
        print('time: ', end-start)

    def test_5(self):
        data = {'address': '成龙大道888号', \
                'city':'028',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('5: ', res)

    def test_6(self):
        data = {'address': '成华区青龙街道荆竹中路199号华润翠林华庭6-103电联', \
                'city':'028',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ', res)



    def test_7(self):
        data = {'address': '四川省 成都市/资阳市/眉山市 成都市人民南路二段18号川信大厦36层', \
                'city':'成都市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('7: ', res)

    def test_8(self):
        data = {'address': '成都市人民南路二段18号川信大厦36层', \
                'city':'成都市/资阳市/眉山市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('8: ', res)

    def test_9(self):
        data = {'address': '成都市人民南路二段18号川信大厦36层', \
                'city': '510131/510100/510183', \
                'span': '1', \
                 'opt': 'sf30', \
                 'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('9: ', res)

    def test_10(self):
        data = {'address': '', \
                'city':'成都市/资阳市/眉山市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'address': '北京北京市北京市浙江省诸暨市暨阳街道艮塔西路61号2幢', \
                'city':'||', \
                'exact':'1', \
                'cb':'__cx1',\
                'opt': 'gd2', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_13(self):
        data = {'address': '陕西省 西安市/咸阳市 未央区明光路南段阳光北郡小区', \
                'city':'/咸阳市/西安市',\
                'span':'1',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ', res)

    def test_14(self):
        data = {'address': '四川省 成都市/资阳市/眉山市 成都市人民南路二段18号川信大厦36层', \
                'city': '', \
                'span': '1', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)

    def test_15(self):
        data = {
                'opt': 'gd2', \
                'city': '河南省|驻马店市|新蔡县', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'address': '<scrpit>alert("深圳")</scrpit>', \
                'opt': 'gd2', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'address': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': 'gd2', \
                'city': '%E6%B7%B1%E5%9C%B3&', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'address': '！@#￥%……：“', \
                'opt': 'gd2', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'address': '深圳万安村', \
                'opt': 'gd2', \
                'city': '<scrpit>alert(city)</scrpit>', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)



    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(v2_1))
    runner = unittest.TextTestRunner()
    runner.run(suite)