import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

url=geturl("tip")
#url=geturl("tip")
#url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_2(TestAbstract):
    def test_1(self):
        data = {'q': '长治市襄垣县侯堡镇珂颐市场南晶楼对面一单元601室', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '侯堡镇珂颐市场南晶楼对面一单元601室', \
                'opt': 'sf30', \
                'city': '长治襄垣县', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '侯堡镇珂颐市场南晶楼对面一单元601室', \
                'opt': 'sf30', \
                'city': '140000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '侯堡镇珂颐市场南晶楼对面一单元601室', \
                'opt': 'sf30', \
                'city':'山西省长治市',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '山西省长治市襄垣县侯堡镇珂颐市场南晶楼对面一单元601室', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    

    def test_6(self):
        data = {'q': '珂颐市场南晶楼对面一单元601室', \
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
    suite.addTest(unittest.makeSuite(tip_2))
    runner = unittest.TextTestRunner()
    runner.run(suite)