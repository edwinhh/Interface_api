import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

url=geturl("tip")
#url=geturl("tip")
#url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_7(TestAbstract):
    def test_1(self):
        data = {'q': '厦门市曾厝垵社20号', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '曾厝垵社20号', \
                'opt': '', \
                'city': '厦门', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '曾厝垵社20号', \
                'opt': '', \
                'city': '350200', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '曾厝垵社20号', \
                'opt': '', \
                'city':'福建省厦门市',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '福建省厦门市曾厝垵社20号', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 


    def test_6(self):
        data = {'q': '曾厝垵社20号', \
                 'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)







    @classmethod
    def tearDownClass(clz):
        reporttxt(name,url, p, r,"get")


    @classmethod
    def tearDownClass(clz):
        reporttxt(name,url, p, r,"get")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip_7))
    runner = unittest.TextTestRunner()
    runner.run(suite)