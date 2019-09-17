import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url=geturl("tip")
url=geturl("tip")
#url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_13341(TestAbstract):
    def test_1(self):
        data = {'q': '香港特别行政区新成路20号B世紀窗簾寢室用品', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '香港特别行政区新成路20号B世紀窗簾寢室用品', \
                'opt': '', \
                'city': '香港', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '香港特别行政区新成路20号B世紀窗簾寢室用品', \
                'opt': '', \
                'city': '810112', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '香港特别行政区新成路20号B世紀窗簾寢室用品', \
                'opt': '', \
                'city':'810112',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '香港特别行政区南区广东道', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    

    def test_6(self):
        data = {'q': '广东省深圳市', \
                 'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_7(self):
        data = {'q': '深圳市', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_8(self):
        data = {'q': '中国广东深圳', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_9(self):
        data = {'q': '广东省深圳市南山区南园村新二坊18栋', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_10(self):
        data = {'q': '深圳万里工业区“万”', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'q': '深圳万安村', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_13(self):
        data = {'q': '', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ', res)

    def test_14(self):
        data = {
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)

    def test_15(self):
        data = {
                'opt': '', \
                'city': '河南省|驻马店市|新蔡县', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'q': '<scrpit>alert("深圳")</scrpit>', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'q': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': '', \
                'city': '%E6%B7%B1%E5%9C%B3&', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'q': '！@#￥%……：“', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'q': '深圳万安村', \
                'opt': '', \
                'city': '<scrpit>alert(city)</scrpit>', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)

    def test_20(self):
        data = {'q': '广东省深圳市南山区a8音乐大厦', \
                'opt': '', \
                'city': '深圳市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_21(self):
        data = {'q': '广东省深圳市南山区南园村新二坊18栋', \
                'opt': '', \
                'city': '755', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_22(self):
        data = {'q': '海上世界', \
                'opt': '', \
                'city': '755', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_23(self):
        data = {'q': '广东省深圳市南山区南园村新二坊18栋', \
                'opt': '', \
                'city': '广州市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_24(self):
        data = {'q': '半岛城邦2期1栋', \
                'opt': '', \
                'city': '440300', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_25(self):
        data = {'q': '深圳市  南山区 海德 3道 3号', \
                'opt': '', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_26(self):
        data = {'q': ' 深圳市深圳  南山区南山 海德 3道 3号 ', \
                'opt': '', \
                'city': '厦门市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_40(self):
        data = {'q': '"广东省广东省广东省深圳市蛇口海上世界"', \
                'opt': '', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_27(self):
        data = {'q': '广东省深圳市深圳市蛇口蛇口海上世界', \
                'opt': '', \
                'city': '新疆', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_28(self):
        data = {'q': '深圳^蛇口^海上世界^海上世界', \
                'opt': '', \
                'city': '珠海', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_29(self):
        data = {'q': ' 深圳市|蛇口|海上世界|海上世界 ', \
                'opt': '', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_30(self):
        data = {'q': '\\海上世界 ', \
                'opt': '', \
                'city': '755', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)



    def test_31(self):
        data = {'q': '\\', \
               'opt': '', \
                'city': '深圳', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_32(self):
        data = {'q': '盛世传媒', \
               'opt': '', \
                'city': '440000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_33(self):
        data = {'q': '&&', \
               'opt': '', \
                'city': '440000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_34(self):
        data = {'q': '"1"="1"', \
               'opt': '', \
                'city': '440000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_35(self):
        data = {'q': 'http://gis-rss.intsit.sfdc.com.cn:1080/geo', \
               'opt': '', \
                'city': '440000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_36(self):
        data = {'q': '1080', \
               'opt': '', \
                'city': '440000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_37(self):
        data = {'q': '%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%BD%97%E6%B9%96%E5%8C%BA%E7%AC%8B%E5%B2%97%E8%A1%97%E9%81%93%E5%AE%9D%E5%B2%97%E8%B7%AF%E5%A4%A7%E5%8D%8E%E5%A4%A7%E5%8E%A6&', \
               'opt': '', \
                'city': '755', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_38(self):
        data = {'q': '香港特别行政区新成路20号B世紀窗簾寢室用品', \
                'opt': '', \
                'city': '香港特别行政区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_39(self):
        data = {'q': '香港特别行政区新成路20号B世紀窗簾寢室用品', \
                'opt': '', \
                'city': '810000', \
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
    suite.addTest(unittest.makeSuite(tip_13341))
    runner = unittest.TextTestRunner()
    runner.run(suite)