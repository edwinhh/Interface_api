import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

url = 'http://GIS-RSS-PROXY.intsit.sfdc.com.cn:1080/tip'
#url='http://10.202.95.115:9090/tip'
#url='http://10.202.95.116:9090/tip'
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_8(TestAbstract):
    def test_1(self):
        data = {'q': '昆明市莲华街道教场中路314号', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '莲华街道教场中路314号', \
                'opt': 'sf30', \
                'city': '昆明', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '莲华街道教场中路314号', \
                'opt': 'sf30', \
                'city': '530100', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '莲华街道教场中路314号', \
                'opt': 'sf30', \
                'city':'云南省昆明市',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '云南省莲华街道教场中路314号', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    

    def test_6(self):
        data = {'q': '莲华街道教场中路314号', \
                 'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)







    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip_8))
    runner = unittest.TextTestRunner()
    runner.run(suite)