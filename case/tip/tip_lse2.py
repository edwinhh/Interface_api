import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url=geturl("tip")
url=geturl("tip")
#url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_13342(TestAbstract):
    def test_1(self):
        data = {'q': '江苏省苏州市张家港市人民中路近市政府民服务中心', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '江苏省苏州市张家港市人民中路近市政府民服务中心', \
                'opt': 'sf30', \
                'city': '江苏省苏州市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '江苏省苏州市张家港市人民中路近市政府民服务中心', \
                'opt': 'sf30', \
                'city': '320000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '江苏省苏州市张家港市人民中路近市政府民服务中心', \
                'opt': 'sf30', \
                'city':'810112',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '江苏省苏州市张家港市人民中路近市政府民服务中心', \
                'opt': 'sf30', \
                'city': '苏州市张家港市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    

    def test_6(self):
        data = {'q': '江苏省苏州市张家港市人民中路近市政府民服务中心', \
                'opt': 'sf30', \
                'city': '苏州', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_7(self):
        data = {'q': '江苏省苏州市张家港市人民中路近市政府民服务中心', \
                'opt': 'sf30', \
                'city': '江苏省张家港市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_8(self):
        data = {'q': '江苏省苏州市张家港市人民中路近市政府民服务中心', \
                'opt': 'sf30', \
                'city': '张家港市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_9(self):
        data = {'q': '广东省深圳市南山区南园村新二坊18栋', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_10(self):
        data = {'q': '天津市,鼓楼西街富力城天霖园,西马路与南城街交口天霖园', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'q': '天津市鼓楼西街富力城天霖园西马路与南城街交口天霖园', \
                'opt': 'sf30', \
                'city': '天津', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_12(self):
        data = {'q': '天津市天霖园西马路与南城街交口天霖园', \
                'opt': 'sf30', \
                'city': '120000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_13(self):
        data = {'q': '', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ', res)

    def test_14(self):
        data = {
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)

    def test_15(self):
        data = {
                'opt': 'sf30', \
                'city': '江苏省|苏州市|张家港市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'q': '<scrpit>alert("山西")</scrpit>', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'q': '%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0', \
                'opt': 'sf30', \
                'city': '%E6%B7%B1%E5%9C%B3&', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'q': '！@#￥%……：“', \
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

    def test_19(self):
        data = {'q': '山西省长治市襄垣县侯堡镇珂颐市场南晶楼对面一单元601室', \
                'opt': 'sf30', \
                'city': '<scrpit>alert(长治市)</scrpit>', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)

    def test_20(self):
        data = {'q': '山西省人民医院', \
                'opt': '', \
                'city': '山西', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_21(self):
        data = {'q': '人民医院', \
                'opt': 'sf30', \
                'city': '140000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_22(self):
        data = {'q': '人民医院', \
                'opt': 'sf30', \
                'city': '太原', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_23(self):
        data = {'q': '山西省长治市襄垣县侯堡镇珂颐市场南晶楼对面一单元601室', \
                'opt': 'sf30', \
                'city': '广州市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_24(self):
        data = {'q': '山西省长治市', \
                'opt': 'sf30', \
                'city': '440300', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_25(self):
        data = {'q': ' 山西省 长治市  襄垣县 侯堡镇 珂颐市场 南晶楼对面 一单元601室 ', \
                'opt': 'sf30', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_26(self):
        data = {'q': ' 山西省山西晋中晋中市祁县 ', \
                'opt': 'sf30', \
                'city': '祁县', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_26(self):
        data = {'q': '"山西省祁县祁县"', \
                'opt': 'sf30', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_27(self):
        data = {'q': '祁县山西省', \
                'opt': 'sf30', \
                'city': '140000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_28(self):
        data = {'q': '山西省……^长治市^  襄垣县^侯堡镇^珂颐市场^南晶楼对面', \
                'opt': 'sf30', \
                'city': '长治', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_29(self):
        data = {'q': ' ……山西省|长治市|襄垣县|侯堡镇|珂颐市场 ', \
                'opt': 'sf30', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_30(self):
        data = {'q': '\\晋祠 ', \
                'opt': 'sf30', \
                'city': '140002', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)



    def test_31(self):
        data = {'q': '\\', \
               'opt': 'sf30', \
                'city': '120000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_32(self):
        data = {'q': '晋祠', \
               'opt': 'sf30', \
                'city': '120000aM001', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_33(self):
        data = {'q': '&&', \
               'opt': 'sf30', \
                'city': '120000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_34(self):
        data = {'q': '"1"="1"', \
               'opt': 'sf30', \
                'city': '120000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_35(self):
        data = {'q': 'http://gis-rss.intsit.sfdc.com.cn:1080/geo', \
               'opt': 'sf30', \
                'city': '120000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_36(self):
        data = {'q': '1080', \
               'opt': 'sf30', \
                'city': '120000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_37(self):
        data = {'q': '%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%BD%97%E6%B9%96%E5%8C%BA%E7%AC%8B%E5%B2%97%E8%A1%97%E9%81%93%E5%AE%9D%E5%B2%97%E8%B7%AF%E5%A4%A7%E5%8D%8E%E5%A4%A7%E5%8E%A6&', \
               'opt': 'sf30', \
                'city': '120000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip_13342))
    runner = unittest.TextTestRunner()
    runner.run(suite)