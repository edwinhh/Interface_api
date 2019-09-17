import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *
url=geturl("geo")
ak=getak("ak")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class geo_core(TestAbstract):
    def test_1(self):
        data = {'address': '臼塔街380-2€辽宁中医药大学杏林学院张', \
                'opt': '', \
                'city': '辽宁省|沈阳市|浑南区', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)

    def test_2(self):
        data = {'address': '	€£¢ªÊË®£赟赓檿™®℃∴〆々★', \
                'opt': '', \
                'city': '440204', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_3(self):
        data = {'address': '广东省+++++++++深圳市++++++', \
                'opt': '', \
                'city': '320703', \
                'span' :'1',\
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'address': '/////、、、、、、、、河池市凤山县-----------------------------------------------------------------------------------******************************=================================================================', \
                'span': '1', \
                'opt': '', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('4: ', res)

    def test_5(self):
        data = {'address': '深圳市,愣》鹕绞心虾Ｇㄉ秸蚬ひ翟癇区科韵北路1号{车间(A区）（B区）}|', \
                'opt': '', \
                
                'city': '', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    def test_6(self):
        data = {'address': '松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期5栋2单元松山湖锦绣山河二期55栋2单元', \
                'opt': '', \
                
                'city': '深圳市', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('12: ', res)

    def test_7(self):
        data = {'address': '海上世界', \
                'opt': '', \
                
                'city': '深圳市|东莞市', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ', res)

    def test_8(self):
        data = {'address': '', \
                'opt': '', \
                
                'city': '深圳市|', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('7: ', res)

    def test_9(self):
        data = {'address': '中国新疆', \
                'opt': '', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('8: ', res)

    def test_10(self):
        data = {'address': '非洲', \
                'opt': '', \
                
                'city': '深圳市|', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('9: ', res)

    def test_11(self):
        data = {'address': '深圳万里工业区“万”', \
                'opt': '', \
                
                'city': '深圳市', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_12(self):
        data = {'address': '深圳万里工业区“万”', \
                'opt': '', \
                
                'city': '深圳市|光明区', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_13(self):
        data = {
                'opt': '', \
                
                'city': '深圳市|光明区', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ', res)

    def test_14(self):
        data = {
                'opt': '', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)

    def test_15(self):
        data = {
                'opt': '', \
                'city': '河南省|驻马店市|新蔡县', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'address': '<scrpit>alert("深圳")</scrpit>', \
                'opt': '', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'address': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': '', \
                
                    'city': '%E6%B7%B1%E5%9C%B3&', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'address': '！@#￥%……：“', \
                'opt': '', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'address': '深圳万安村', \
                'opt': 'tc1', \
                
                'city': '<scrpit>alert(city)</scrpit>', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)

    def test_20(self):
        data = {'address': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': '', \
                
                'city': '%E6%B7%B1%E5%9C%B3&', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_21(self):
        data = {'address': '潮白河孔雀城英国宫4期春晓园', \
                'opt': '', \
                'city': '131028', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_22(self):
        data = {'address': '湖南省--长沙市-雨花区--', \
                'opt': '', \
                
                'city': '131028', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    

    def test_23(self):
        data = {'address': '广东省广东省广东省深圳市蛇口海上世界', \
                'opt': '', \
                'city': '', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_24(self):
        data = {'address': '广东省深圳市深圳市蛇口蛇口海上世界', \
                'opt': '', \
                'city': '', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_25(self):
        data = {'address': '深圳市^蛇口^海上世界^海上世界', \
                'opt': '', \
                'city': '', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_26(self):
        data = {'address': ' 深圳市 蛇口 海上世界 海上世界 ', \
                'opt': '', \
                'city': '', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_27(self):
        data = {'address': '海上世界 ', \
                'opt': '', \
                'city': '755', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


   

    def test_28(self):
        data = {'address': '\\', \
               'opt': '', \
                'city': '深圳', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_29(self):
        data = {'address': '盛世传媒', \
               'opt': '', \
                'city': '755aM001', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_30(self):
        data = {'address': '&&', \
               'opt': '', \
                'city': '755aM001', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_31(self):
        data = {'address': '"1"="1"', \
               'opt': '', \
                'city': '755aM001', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_32(self):
        data = {'address': 'http://gis-rss.intsit.sfdc.com.cn:1080/geo', \
               'opt': '', \
                'city': '755aM001', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_33(self):
        data = {'ak':ak, \
                'address': '广东省&#39;) UNION ALL SELECT 31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,CHR(113)||CHR(98)||CHR(106)||CHR(98)||CHR(113)||CHR(89)||CHR(111)||CHR(113)||CHR(120)||CHR(106)||CHR(87)||CHR(90)||CHR(86)||CHR(81)||CHR(112)||CHR(108)||CHR(103)||CHR(85)||CHR(114)||CHR(85)||CHR(82)||CHR(113)||CHR(98)||CHR(75)||CHR(98)||CHR(122)||CHR(90)||CHR(100)||CHR(114)||CHR(76)||CHR(118)||CHR(77)||CHR(70)||CHR(75)||CHR(108)||CHR(98)||CHR(106)||CHR(108)||CHR(103)||CHR(82)||CHR(113)||CHR(112)||CHR(114)||CHR(86)||CHR(112)||CHR(113)||CHR(122)||CHR(112)||CHR(122)||CHR(113),31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31 FROM DUAL-- mfte广州市番禺区西三村新兴二巷15号三.四层', \
               'opt': '', \
                'city': ''
                }
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_34(self):
        data = {'address': '%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%BD%97%E6%B9%96%E5%8C%BA%E7%AC%8B%E5%B2%97%E8%A1%97%E9%81%93%E5%AE%9D%E5%B2%97%E8%B7%AF%E5%A4%A7%E5%8D%8E%E5%A4%A7%E5%8E%A6&', \
               'opt': '', \
                'city': '755', \
                
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        



    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r,"get")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(geo_core))
    runner = unittest.TextTestRunner()
    runner.run(suite)