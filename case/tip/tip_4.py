import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

url=geturl("tip")
#url=geturl("tip")
#url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_4(TestAbstract):
    def test_1(self):
        data = {'q': '青岛市市南区香港西路27号', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '市南区香港西路27号', \
                'opt': 'sf30', \
                'city': '青岛市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '市南区香港西路27号', \
                'opt': 'sf30', \
                'city': '370200', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '市南区香港西路27号', \
                'opt': 'sf30', \
                'city':'山东省青岛市',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '山东省市南区香港西路27号', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    

    def test_6(self):
        data = {'q': '市南区香港西路27号', \
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
    suite.addTest(unittest.makeSuite(tip_4))
    runner = unittest.TextTestRunner()
    runner.run(suite)