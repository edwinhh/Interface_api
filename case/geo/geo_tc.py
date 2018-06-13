import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url=geturl("geo")
#url='http://10.202.52.103:8080/geo'
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class geo_tc(TestAbstract):
    def test_1(self):
        data = {'address': '广东省深圳市龙岗区南湾街道樟树布新圹东六巷10号英子正骨推拿馆', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'address': '顺丰快递点自提', \
                'opt': 'tc2', \
                'city': '河南省|驻马店市|新蔡县', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'address': '广东省', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'address': '广州市中山大学', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('4: ', res)

    def test_5(self):
        data = {'address': '杭州西湖', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_12(self):
        data = {'address': '北京紫禁城', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('12: ', res)

    def test_6(self):
        data = {'address': '上海外滩', \
                 'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ', res)

    def test_7(self):
        data = {'address': '新疆曼哈顿', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('7: ', res)

    def test_8(self):
        data = {'address': '中国新疆', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('8: ', res)

    def test_9(self):
        data = {'address': '非洲', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('9: ', res)

    def test_10(self):
        data = {'address': '深圳万里工业区“万”', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'address': '深圳万安村', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_13(self):
        data = {'address': '', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ', res)

    def test_14(self):
        data = {
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)

    def test_15(self):
        data = {
                'opt': 'tc2', \
                'city': '河南省|驻马店市|新蔡县', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'address': '<scrpit>alert("深圳")</scrpit>', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'address': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': 'tc2', \
                'city': '%E6%B7%B1%E5%9C%B3&', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'address': '！@#￥%……：“', \
                'opt': 'tc2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'address': '深圳万安村', \
                'opt': 'tc1', \
                'city': '<scrpit>alert(city)</scrpit>', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)

    def test_20(self):
        data = {'address': '广东省深圳市南山区a8音乐大厦', \
                'opt': 'tc2', \
                'city': '深圳市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('20: ', res)

    def test_21(self):
        data = {'address': '潮白河孔雀城英国宫4期春晓园', \
                'opt': 'tc2', \
                'city': '131028', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_22(self):
        data = {'address': '燕郊开发区神威北路与燕灵路交汇处鑫乐汇购物广场', \
                'opt': 'tc2', \
                'city': '131028', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_23(self):
        data = {'address': '广东省深圳市南山区南园村新二坊18栋', \
                'opt': 'tc2', \
                'city': '广州市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_24(self):
        data = {'address': '四川省成都市武侯区濯锦路长城半岛城邦2期1栋3003', \
                'opt': 'tc2', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_25(self):
        data = {'address': '深圳市南山区海德3道3号', \
                'opt': 'tc2', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_26(self):
        data = {'address': '福建厦门海沧区厦门市路桥管理有限公司海沧大桥管理中心路桥管理有限公司', \
                'opt': 'tc2', \
                'city': '厦门市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_26(self):
        data = {'address': '广东省广东省广东省深圳市蛇口海上世界', \
                'opt': 'tc2', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_27(self):
        data = {'address': '广东省深圳市深圳市蛇口蛇口海上世界', \
                'opt': 'tc2', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_28(self):
        data = {'address': '深圳市^蛇口^海上世界^海上世界', \
                'opt': 'tc2', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_29(self):
        data = {'address': ' 深圳市 蛇口 海上世界 海上世界 ', \
                'opt': 'tc2', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_30(self):
        data = {'address': '海上世界 ', \
                'opt': 'tc2', \
                'city': '755', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_31(self):
        data = {'address': '重庆市解放路', \
                'opt': 'tc2', \
                'city': '重庆市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_32(self):
        data = {'address': '天津市南开大学', \
                'opt': 'tc2', \
                'city': '天津', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_33(self):
        data = {'address': '北京北京大学', \
                'opt': 'tc2', \
                'city': '北京', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)



    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(geo_tc))
    runner = unittest.TextTestRunner()
    runner.run(suite)