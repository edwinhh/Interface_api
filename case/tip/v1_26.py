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


class v_126(TestAbstract):

    def test_01(self):
        data = {'q': '3005 Layman Court', \
                'city': '', \
                'country':'USA',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestsget(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)
        # self.assertNotIn('陕西西玛特机电设备有限公司',res['result'])
        #self.assertEqual('sw-tcp',res['result']['POISrc'])


    def test_02(self):
        data = {'q': '3005 Layman Court', \
                'city': '', \
                'country':'',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)
        # self.assertEqual('sw-tcp', res['result']['POISrc'])


    def test_03(self):
        data = {'q': '3005 Layman Court', \
                'city': '深圳', \
                'country':'USA',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_04(self):
        data = {'q': '海上世界', \
                'city': '深圳', \
                'country':'CN',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_05(self):
        data = {'q': '3005 Layman Court', \
                'city': '', \
                'country':'USA',\
                'opt':'sf30',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        # n.append(sys._getframe().f_code.co_name)
        # self.assertEqual('sw-tcp', res['result']['POISrc'])

    def test_06(self):
        data = {'q': '3005 Layman Court', \
                'city': '', \
                'country':'',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_07(self):
        data = {'q': '3005 Layman Court', \
                'country':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_08(self):
        data = {'q': '香港大学', \
                'city': '香港', \
                'country':'CN',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)


    def test_09(self):
        data = {'q': '香港大学', \
                'city': '香港', \
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    # self.assertEqual(1,res['status'])


    def test_10(self):
        data = {'q': '香港大学', \
                'city': '香港特区', \
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)



    def test_11(self):
        data = {'q': '香港大学', \
                'city': '香港', \
                'opt':'sf30',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_12(self):
        data = {'q': '<span><script><a>深 圳 福 田 中 心 </a></script></span>', \
                'opt': '', \
                'district': '广州', \
                'country': 'CN', \
                'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_13(self):
        data = {'q': "/tip?q=%E5%B7%A5%E4%B8%9A%E5%A4%A7%E9%81%93%E4%B8%AD381&city=%E5%B9%BF%E5%B7%9E%E5%B8%82&ak=a4fbd3a08ecc4f9e41bc9b06421ef3b5&opt=", \
                'district': ' 清风镇', \
                'country': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_14(self):
        data = {'q': '', \
                'city':'', \
                'country': '', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_15(self):
        data = {'q': '', \
                'country': 'US', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_16(self):
        data = {'q': '', \
                'city':'中国', \
                'country': 'US', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)


    def test_17(self):
        data = {
            'q': '北京大学', \
            'city': '北京', \
            'country': 'CN', \
            'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_18(self):
        data = {
            'country': 'CN', \
            'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)
        
        
    def test_19(self):
        data = {
            'q': '/*/*/*', \
            'city': '北京', \
            'country': 'CN', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_20(self):
        data = {
            'q': '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \
                 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', \
            'city': '*********************************************************************************************************************************', \
            'country': '//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)
        
        
    def test_21(self):
        data = {
            'q': '/*/*/*', \
            'city': '                                                                                                             \
                                                                                                  ', \
            'country': '                                                        ', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    @classmethod
    def tearDownClass(clz):
        reporttxt(name,url, p, r,n)




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(v_126))
    runner = unittest.TextTestRunner()
    runner.run(suite)
