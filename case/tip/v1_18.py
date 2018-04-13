import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

sys.path.append('e:/project/Interface_api-master')

#url = 'http://GIS-RSS-PROXY.intsit.sfdc.com.cn:1080/tip'
#url='http://10.202.95.115:9090/tip'
url='http://gis-rss-core-hint.sit.sf-express.com:5580/tip'
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]
dic={}


class tip1_18(TestAbstract):

    def test_1(self):
        data = {'q': '深圳', \
                'opt': 'sf2', \
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ',res)
    #self.assertEqual(0,res['status'])

    def test_2(self):
        data = {'q': '杭州', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ',res)
    # self.assertEqual(1,res['status'])

    def test_3(self):
        data = {'q': '上海', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ',res)

    def test_4(self):
        data = {'q': '北京"', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('4: ',res)

    def test_5(self):
        data = {'q': '深圳大学"', \
                'opt': '', \
                'city': '755', \
                'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('5: ',res)

    def test_6(self):
        data = {'q': '深圳海岸城"', \
                'opt': '', \

                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ',res)


    def test_7(self):
        data = {'q': '深圳海岸城"', \
                'opt': 'sf2', \
                'city': '重庆', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('7: ',res)

    def test8(self):
        data = {'q': '美国加州"', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('8: ',res)

    def test_9(self):
        data = {'q': '广州', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('9: ',res)

    def test_10(self):
        data = {'q': '广州"', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ',res)

    def test_11(self):
        data = {'q': '', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ',res)


    def test_12(self):
        data = {'q': '<scrpit>alert</scrpit>', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('12: ',res)

    def test_13(self):
        data = {'q': '&', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ',res)

    def test_14(self):
        data = {'q': '深圳蛇口', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ',res)

    def test_15(self):
        data = {'q': '广州', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ',res)

    def test_16(self):
        data = {'q': '罗布泊', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ',res)

    def test_17(self):
        data = {'q': '广东省', \
                'opt': 'sw3', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ',res)

    def test_18(self):
        data = {'q': '广东省', \
                'opt': 'sa2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ',res)





    @classmethod
    def tearDownClass(clz):
        reporttxt(name,url, p, r)




if __name__ == "__main__":
    #
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip1_18))
    runner = unittest.TextTestRunner()
    runner.run(suite)