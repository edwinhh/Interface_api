import unittest

from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-rss-rgeo.intsit.sfdc.com.cn:1080/rgeo'
#url='http://10.202.43.107:8080/rgeo'
url='http://10.203.32.186:8080/rgeo/api'
name = os.path.basename(__file__).split('.')[0]
p = []
r = []

class rgeo_1(TestAbstract):
    def test_1(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': 'sf1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': 'bd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)

class rgeo_2(TestAbstract):
    def test_1(self):
        data = {'x': '120.568292', \
                'y': '31.310205', \
                'opt': 'sf1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'x': '120.568292', \
                'y': '31.310205', \
                'opt': 'bd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'x': '120.568292', \
                'y': '', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)

class rgeo_3(TestAbstract):
    def test_1(self):
        data = {'x': '', \
                'y': '23.20', \
                'opt': 'sf1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'x': '113.30', \
                'y': '23.20', \
                'opt': 'bd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_3(self):
        data = {'x': '113.30', \
                'y': '23.20', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)

class rgeo_4(TestAbstract):
    def test_1(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': 'sf1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_3(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': 'bd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)

class rgeo_5(TestAbstract):
    def test_1(self):
        data = {'x': '77.037386', \
                'y': '38.898658', \
                'opt': 'sf1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'x': '77.037386', \
                'y': '38.898658', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'x': '77.037386', \
                'y': '38.898658', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'x': '114.071307', \
                'y': '22.648358', \
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

    def test_6(self):
        data = {'x': '114.131266', \
                'y': '22.545732', \
                'opt':'sf1',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ', res)



    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)

if __name__ == "__main__":
    #
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(rgeo_1))
    runner = unittest.TextTestRunner()
    runner.run(suite)