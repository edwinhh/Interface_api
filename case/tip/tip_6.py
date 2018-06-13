import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

url=geturl("tip")
#url=geturl("tip")
#url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_6(TestAbstract):
    def test_1(self):
        data = {'q': '湖北省武汉市武昌区解放路457号附3号', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '解放路457号附3号', \
                'opt': 'sf30', \
                'city': '武汉', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '解放路457号附3号', \
                'opt': 'sf30', \
                'city': '湖北省', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '解放路457号附3号', \
                'opt': 'sf30', \
                'city':'湖北省武汉市',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '湖北省解放路457号附3号', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    

    def test_6(self):
        data = {'q': '解放路457号附3号', \
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
    suite.addTest(unittest.makeSuite(tip_6))
    runner = unittest.TextTestRunner()
    runner.run(suite)