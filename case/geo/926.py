import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

url=geturl("geo")

name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class test(TestAbstract):
    def test_1(self):
        data = {'address': '水利局', \
                'opt': 'gd1', \
                'city': '431225', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'address': '顺丰快递点自提', \
                'opt': 'bd1', \
                'city': '河南省|驻马店市|新蔡县', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)



    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test))
    runner = unittest.TextTestRunner()
    runner.run(suite)