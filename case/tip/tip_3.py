import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

url = 'http://GIS-RSS-PROXY.intsit.sfdc.com.cn:1080/tip'
#url='http://10.202.95.115:9090/tip'
#url='http://10.202.95.116:9090/tip'
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_3(TestAbstract):
    def test_1(self):
        data = {'q': '呼伦贝尔市鄂伦春自治旗育才街13号第一照相馆', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '育才街13号第一照相馆', \
                'opt': 'sf30', \
                'city': '呼伦贝尔', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '育才街13号第一照相馆', \
                'opt': 'sf30', \
                'city': '150000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '育才街13号第一照相馆', \
                'opt': 'sf30', \
                'city':'内蒙古自治区呼伦贝尔市鄂伦春自治旗',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '内蒙古自治区呼伦贝尔市鄂伦春自治旗育才街13号第一照相馆', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    

    def test_6(self):
        data = {'q': '鄂伦春自治旗育才街13号第一照相馆', \
                 'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)



    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip_3))
    runner = unittest.TextTestRunner()
    runner.run(suite)