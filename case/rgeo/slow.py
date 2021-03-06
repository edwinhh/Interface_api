import unittest
import sys

sys.path.append('e:/project/Interface_api-master')

from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-rss-rgeo.intsit.sfdc.com.cn:1080/rgeo'
#url='http://10.202.43.106:8080/rgeo'
url=geturl('rgeo')
name = os.path.basename(__file__).split('.')[0]

p = []
r = []


class rgeo_5(TestAbstract):
    def test_1(self):
        data = {'x': '114.123492', \
                'y': '22.648358', \
                'opt':'sf1',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'x': '114.131266', \
                'y': '22.545732', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'x': '114.690661', \
                'y': '22.962536', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'x': '114.126238', \
                'y': '22.884564', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('4: ', res)

    def test_5(self):
        data = {'x': '114.203831', \
                'y': '22.703257', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('5: ', res)

    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)

if __name__ == "__main__":
    print(os.path.basename(os.path.basename(__file__)))

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(rgeo_5))
    runner = unittest.TextTestRunner()
    runner.run(suite)