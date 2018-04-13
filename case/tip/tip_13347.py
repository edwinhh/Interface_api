import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://GIS-RSS-PROXY.intsit.sfdc.com.cn:1080/tip'
url='http://10.202.95.115:9090/tip'
#url='http://10.202.95.116:9090/tip'
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_13347(TestAbstract):
    def test_1(self):
        data = {'q': '香港特别行政区新成路20号B世紀窗簾寢室用品', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '大三巴牌坊', \
                'opt': 'sf30', \
                'city': '澳门', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '大三巴牌坊', \
                'opt': 'sf30', \
                'city': '820000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '澳门大三巴牌坊', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '香港特别行政区南区广东道', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    

    def test_6(self):
        data = {'q': '福建泉州市安海镇前埔工业区福建晋工机械有限公司', \
                 'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_7(self):
        data = {'q': '福建泉州市', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_8(self):
        data = {'q': '安海镇前埔工业区福建晋工机械有限公司', \
                'opt': 'sf30', \
                'city':'泉州',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_9(self):
        data = {'q': '安海镇前埔工业区福建晋工机械有限公司', \
                'opt': 'sf30', \
                'city': '350000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_10(self):
        data = {'q': '广西壮族自治区海洋环境监测中心“站”', \
                'opt': 'sf30', \
                'city': '广西壮族自治区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_11(self):
        data = {'q': '广西壮族自治区海洋环境监测中心站', \
                'opt': 'sf30', \
                'city': '北海', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_13(self):
        data = {'q': '', \
                'opt': 'sf30', \
                'city': '450000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_14(self):
        data = {
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_15(self):
        data = {
                'opt': 'sf30', \
                'city': '广西自治区|北海市|银海区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'q': '<scrpit>alert("长沙")</scrpit>', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'q': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': 'sf30', \
                'city': '430000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'q': '！@#￥%……：“', \
                'opt': 'sf30', \
                'city': '湖南', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'q': '韶山北路139号湖南文化大厦', \
                'opt': 'sf30', \
                'city': '<scrpit>alert(长沙)</scrpit>', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)

    def test_20(self):
        data = {'q': '韶山北路139号湖南文化大厦', \
                'opt': '', \
                'city': '湖南', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_21(self):
        data = {'q': '长沙市韶山北路139号湖南文化大厦', \
                'opt': 'sf30', \
                'city': '430002', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_22(self):
        data = {'q': '阅欣路3号宁夏回族自治区环境检测中心站', \
                'opt': 'sf30', \
                'city': '银川市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_23(self):
        data = {'q': '阅欣路3号宁夏回族自治区环境检测中心站', \
                'opt': 'sf30', \
                'city': '640000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_24(self):
        data = {'q': '银川市阅欣路3号宁夏回族自治区环境检测中心站', \
                'opt': 'sf30', \
                'city': '宁夏自治区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_25(self):
        data = {'q': '宁夏  银川市阅 欣路3号  宁夏回族自治区   环境检测中心站', \
                'opt': 'sf30', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_26(self):
        data = {'q': ' 西藏那曲安多, 辽宁中路6号西藏那曲地区科协 ', \
                'opt': 'sf30', \
                'city': '那曲', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_38(self):
        data = {'q': '"西藏那曲安多辽宁中路6号西藏那曲地区科协"', \
                'opt': 'sf30', \
                'city': '540000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_27(self):
        data = {'q': '辽宁中路6号西藏那曲地区科协', \
                'opt': 'sf30', \
                'city': '西藏', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_28(self):
        data = {'q': '观景路^100号^新疆师范大学^温泉校区', \
                'opt': 'sf30', \
                'city': '乌鲁木齐市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_29(self):
        data = {'q': '观景路|100号|新疆师范大学|温泉校区 ', \
                'opt': 'sf30', \
                'city': '650000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_30(self):
        data = {'q': '\\人民医院 ', \
                'opt': 'sf30', \
                'city': '新疆', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)



    def test_31(self):
        data = {'q': '\\', \
               'opt': 'sf30', \
                'city': '新疆', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_32(self):
        data = {'q': '盛世传媒', \
               'opt': 'sf30', \
                'city': '650000aM001', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_33(self):
        data = {'q': '&&', \
               'opt': 'sf30', \
                'city': '650000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_34(self):
        data = {'q': '"1"="1"', \
               'opt': 'sf30', \
                'city': '650000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_35(self):
        data = {'q': 'http://gis-rss.intsit.sfdc.com.cn:1080/geo', \
               'opt': 'sf30', \
                'city': '650000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_36(self):
        data = {'q': '1080', \
               'opt': 'sf30', \
                'city': '650000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_37(self):
        data = {'q': '%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%BD%97%E6%B9%96%E5%8C%BA%E7%AC%8B%E5%B2%97%E8%A1%97%E9%81%93%E5%AE%9D%E5%B2%97%E8%B7%AF%E5%A4%A7%E5%8D%8E%E5%A4%A7%E5%8E%A6&', \
               'opt': 'sf30', \
                'city': '伊犁', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip_13347))
    runner = unittest.TextTestRunner()
    runner.run(suite)