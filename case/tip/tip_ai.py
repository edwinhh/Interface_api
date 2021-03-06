import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *
url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_ai(TestAbstract):
    def test_1(self):
        data = {'q': '软件产业基地', \
                'opt': '', \
                'city': '深圳市', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'q': '<scrpit>alert("深圳")</scrpit>', \
                'opt': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'q': '深圳软件产业基地', \
                'opt': '', \
                'city': '', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'q': '深圳软件产业基地', \
                'opt': '', \
                'city': '广州', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('4: ', res)

    def test_5(self):
        data = {'q': '深圳软件产业基地', \
                'opt': '', \
                'city': '广东', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_12(self):
        data = {'q': '深圳软件产业基地', \
                'opt': '', \
                'city': '深圳', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('12: ', res)

    def test_6(self):
        data = {'q': '深圳海上世界', \
                'opt': '', \
                
                'city': '东莞市', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ', res)

    def test_7(self):
        data = {'q': '', \
                'opt': '', \
                
                'city': '深圳市', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('7: ', res)

    def test_8(self):
        data = {'q': '中国新疆', \
                'opt': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('8: ', res)

    def test_9(self):
        data = {'q': '非洲', \
                'opt': '', \
                
                'city': '深圳市', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('9: ', res)

    def test_10(self):
        data = {'q': '深圳万里工业区“万”', \
                'opt': '', \
                'city': '深圳市', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'q': '深圳万里工业区“万”', \
                'opt': '', \
                'city': '深圳', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

  
    def test_14(self):
        data = {
                'opt': '', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)


    def test_16(self):
        data = {'q': '<scrpit>alert("深圳")</scrpit>', \
                'opt': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'q': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': '', \
                
                'city': '', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'q': '！@#￥%……：“', \
                'opt': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'q': '深圳万安村', \
                'opt': '', \
                
                'city': '深圳', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)

   
    def test_22(self):
        data = {'q': '燕郊开发区神威北路与燕灵路交汇处鑫乐汇购物广场', \
                'opt': '', \
                
                'city': '深圳', \
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_23(self):
        data = {'q': '广东省深圳市南山区南园村新二坊18栋', \
                'opt': '', \
                'city': '广州市', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_24(self):
        data = {'q': '四川省成都市武侯区濯锦路长城半岛城邦2期1栋3003', \
                'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_25(self):
        data = {'q': '深圳市南山区海德3道3号', \
                'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_26(self):
        data = {'q': '福建厦门海沧区厦门市路桥管理有限公司海沧大桥管理中心路桥管理有限公司', \
                'opt': '', \
                'city': '厦门市', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_26(self):
        data = {'q': '广东省广东省广东省深圳市蛇口海上世界', \
                'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_27(self):
        data = {'q': '广东省深圳市深圳市蛇口蛇口海上世界', \
                'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_28(self):
        data = {'q': '深圳市^蛇口^海上世界^海上世界', \
                'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_29(self):
        data = {'q': ' 深圳市 蛇口 海上世界 海上世界 ', \
                'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

   
    def test_32(self):
        data = {'q': '天津市南开大学', \
                'opt': '', \
                'city': '天津', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_33(self):
        data = {'q': '北京北京大学', \
                'opt': '', \
                'city': '北京', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_34(self):
        data = {'q': '星都国际总部基地', \
               'opt': '', \
                'city': '昆明', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_35(self):
        data = {'q': '盛世传媒', \
               'opt': '', \
                'city': '440305', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_36(self):
        data = {'q': '盛世传媒', \
               'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_37(self):
        data = {'q': '盛世传媒', \
               'opt': '', \
                'city': '深圳', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)



   

    def test_40(self):
        data = {'q': '\\', \
               'opt': '', \
                'city': '深圳', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_41(self):
        data = {'q': '盛世传媒', \
               'opt': '', \
                'city': '755aM001', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_42(self):
        data = {'q': '&&', \
               'opt': '', \
                'city': '755aM001', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_42(self):
        data = {'q': '"1"="1"', \
               'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_43(self):
        data = {'q': 'http://gis-rss.intsit.sfdc.com.cn:1080/geo', \
               'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_44(self):
        data = {'q': '1080', \
               'opt': '', \
                'city': '', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_45(self):
        data = {'q': '%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%BD%97%E6%B9%96%E5%8C%BA%E7%AC%8B%E5%B2%97%E8%A1%97%E9%81%93%E5%AE%9D%E5%B2%97%E8%B7%AF%E5%A4%A7%E5%8D%8E%E5%A4%A7%E5%8E%A6&', \
               'opt': '', \
                'city': '深圳', \
                
                'ak': '1b20896414c79752d47e27839b3f5f63'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        



    @classmethod
    def tearDownClass(clz):
        reporttxt(name,url, p, r,"get")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip_ai))
    runner = unittest.TextTestRunner()
    runner.run(suite)