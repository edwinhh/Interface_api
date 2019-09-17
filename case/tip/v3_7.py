import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *


url=geturl("tip")
#url='https://218.17.248.243:40115/tip'
#url='http://gis-ass-tip.intsit.sfdc.com.cn:1080/tip'
#url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]
n=[]
dic={}


class t_37(TestAbstract):

    def test_01(self):
        data = {'q': "学校", \
                'city': '仙桃市', \
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestsget(url, data)
        p.append(data)
        r.append(res)
        print(res)
        n.append(sys._getframe().f_code.co_name)
        #self.assertNotIn('陕西西玛特机电设备有限公司',res['result'])
        #self.assertEqual('sw-tcp',res['result']['POISrc'])


    def test_02(self):
        data = {'q': '学校', \
                'city': '定州市', \
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)
        #n.append(sys._getframe().f_code.co_name)
        # self.assertEqual('sw-tcp', res['result']['POISrc'])


    def test_03(self):
        data = {'q': '学校', \
                'city': '昆玉市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)
        #n.append(sys._getframe().f_code.co_name)

    def test_04(self):
        data = {'q': '香港大学', \
                'city': '香港', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)
        #n.append(sys._getframe().f_code.co_name)

    def test_05(self):
        data = {'q': '湖北省荆门市京山县', \
                'city': '荆门市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)
        # n.append(sys._getframe().f_code.co_name)
        # self.assertEqual('sw-tcp', res['result']['POISrc'])

    def test_06(self):
        data = {'q': '青海省海西蒙古族藏族自治州茫崖市', \
                'city': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)
        #n.append(sys._getframe().f_code.co_name)

    def test_07(self):
        data = {'q': '桂林市荔浦市', \
                'city': '桂林市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)
        #n.append(sys._getframe().f_code.co_name)

    def test_08(self):
        data = {'q': '江西省|鹰潭市|余江区', \
                'city': '鹰潭', \
                'district': '余江区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)


    def test_09(self):
        data = {'q': '河南省济源市', \
                'city': '', \
                'district': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)

    # self.assertEqual(1,res['status'])


    def test_10(self):
        data = {'q': '医院', \
                'city': '辛集市', \
                'district': '坪山区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)



    def test_11(self):
        data = {'q': "政府", \
                'opt': '', \
                'city': '石河子市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)

    def test_12(self):
        data = {'q': '河南省济源县', \
                'city': '', \
                'district': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)
        n.append(sys._getframe().f_code.co_name)

    def test_13(self):
        data = {'q': "/tip?q=%E5%B7%A5%E4%B8%9A%E5%A4%A7%E9%81%93%E4%B8%AD381&city=%E5%B9%BF%E5%B7%9E%E5%B8%82&ak=a4fbd3a08ecc4f9e41bc9b06421ef3b5&opt=", \
                'district': ' 神农架林区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)

    def test_14(self):
        data = {'q': '香港大学', \
                'city': '香港市', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)
        n.append(sys._getframe().f_code.co_name)

    def test_15(self):
        data = {'q': '香港大学', \
                'city': '香港特别行政区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)
        n.append(sys._getframe().f_code.co_name)

    def test_16(self):
        data = {
            'q': '澳门大学', \
            'city': '澳门市', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)


    def test_17(self):
        data = {
            'q': '澳门大学', \
            'city': '澳门特别行政区', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)

    def test_18(self):
        data = {
            'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print(res)


    @classmethod
    def tearDownClass(clz):
        reporttxt(name,url, p, r,"get")




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(t_37))
    runner = unittest.TextTestRunner()
    runner.run(suite)
