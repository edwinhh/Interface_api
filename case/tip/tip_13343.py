import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url=geturl("tip")
url=geturl("tip")
#url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class tip_13343(TestAbstract):
    def test_1(self):
        data = {'q': '内蒙古自治区呼伦贝尔市鄂伦春自治旗龙华路与文化路交汇北远华五金综合商店', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    def test_2(self):
        data = {'q': '浙江嘉欣中山西路2710号丝绸工业园', \
                'opt': '', \
                'city': '嘉兴市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'q': '浙江嘉欣中山西路2710号丝绸工业园', \
                'opt': '', \
                'city': '330000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_4(self):
        data = {'q': '浙江嘉欣中山西路2710号丝绸工业园', \
                'opt': '', \
                'city':'嘉兴',\
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '浙江万里学院基础学院', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
 

    

    def test_6(self):
        data = {'q': '安徽省阜阳沪千人造板制造有限公司', \
                 'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_7(self):
        data = {'q': '安徽省工业园区纬一东路2号阜阳沪千人造板制造有限公司', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_8(self):
        data = {'q': '中国安徽黄山', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_9(self):
        data = {'q': '内蒙古蒙泰煤电集团公司', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_10(self):
        data = {'q': '内蒙古鄂尔多斯市蒙泰煤电“集团公司”', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'q': '鄂尔多斯市蒙泰煤电', \
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
                'city': '内蒙古|鄂尔多斯|', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'q': '<scrpit>alert("内蒙古自治区")</scrpit>', \
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
        data = {'q': '内蒙古自治区人民医院', \
                'opt': '', \
                'city': '<scrpit>alert(内蒙古自治区)</scrpit>', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)

    def test_20(self):
        data = {'q': '人民医院', \
                'opt': '', \
                'city': '内蒙古自治区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_21(self):
        data = {'q': '内蒙古自治区人民医院', \
                'opt': '', \
                'city': '150000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_22(self):
        data = {'q': '包头人民医院', \
                'opt': '', \
                'city': '150001', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_23(self):
        data = {'q': '内蒙古自治区人民医院', \
                'opt': '', \
                'city': '鄂尔多斯', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_24(self):
        data = {'q': '半岛城邦2期1栋', \
                'opt': '', \
                'city': '150001||150000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_25(self):
        data = {'q': '内蒙古自治区  兰察布   东街冶金研究院', \
                'opt': '', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_26(self):
        data = {'q': ' 兰察布东街 ', \
                'opt': '', \
                'city': '呼和浩特', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)



    def test_27(self):
        data = {'q': '内蒙古|自治区||冶金研究院||邮编', \
                'opt': '', \
                'city': '内蒙古', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_28(self):
        data = {'q': '内蒙古^自治区^冶金研究院^^邮编', \
                'opt': '', \
                'city': '150000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_29(self):
        data = {'q': ' 内蒙古|自治区|冶金研究院||邮编 ', \
                'opt': '', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_30(self):
        data = {'q': '\\冶金研究院', \
                'opt': '', \
                'city': '150000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)



    def test_31(self):
        data = {'q': '"\\"', \
               'opt': '', \
                'city': '150000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_32(self):
        data = {'q': '盛世传媒', \
               'opt': '', \
                'city': '150000aM001', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_33(self):
        data = {'q': '&&', \
               'opt': '', \
                'city': '150000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_34(self):
        data = {'q': '"1"="1"', \
               'opt': '', \
                'city': '150000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_35(self):
        data = {'q': 'http://gis-rss.intsit.sfdc.com.cn:1080/geo', \
               'opt': '', \
                'city': '150000', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_36(self):
        data = {'q': '1080', \
               'opt': '', \
                'city': '1500001', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    def test_37(self):
        data = {'q': '%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%BD%97%E6%B9%96%E5%8C%BA%E7%AC%8B%E5%B2%97%E8%A1%97%E9%81%93%E5%AE%9D%E5%B2%97%E8%B7%AF%E5%A4%A7%E5%8D%8E%E5%A4%A7%E5%8E%A6&', \
               'opt': '', \
                'city': '"150000"', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r, "get")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip_13343))
    runner = unittest.TextTestRunner()
    runner.run(suite)