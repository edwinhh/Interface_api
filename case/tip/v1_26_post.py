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


class v_128(TestAbstract):

    def test_01(self):
        data = {'q': '+++DE##+++EwA9TjBxH4ST6diRQfux75dxSntj0hLkP7ERDKZB+OnOK5nsNOMUqXjaI04s2ClJTAQxMiDWycqwHFMBG5BqxrwyDeFtG1xCu0clnmxRE8JyNL+', \
                'city': '8nFvi2MANn4ED+6RvkVTJYA', \
                # 'country':'USA',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)
        print('1: ', res)
        # self.assertNotIn('陕西西玛特机电设备有限公司',res['result'])
        #self.assertEqual('sw-tcp',res['result']['POISrc'])


    def test_02(self):
        data = {'q': '3005 Layman Court', \
                'city': '', \
                'country':'',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestPOST(url, data)
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
        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_04(self):
        data = {'q': '海上世界', \
                'city': '深圳', \
                'country':'CN',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_05(self):
        data = {'q': '3005 Layman Court', \
                'city': '', \
                'country':'USA',\
                'opt':'sf30',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestPOST(url, data)
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
        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_07(self):
        data = {'q': '3005 Layman Court', \
                'country':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_08(self):
        data = {'q': '香港大学', \
                'city': '香港', \
                'country':'CN',\
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)


    def test_09(self):
        data = {'q': '香港大学', \
                'city': '香港', \
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    # self.assertEqual(1,res['status'])


    def test_10(self):
        data = {'q': '香港大学', \
                'city': '香港特区', \
                'opt':'',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)



    def test_11(self):
        data = {'q': '香港大学', \
                'city': '香港', \
                'opt':'sf30',\
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestPOST(url, data)
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

        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_13(self):
        data = {'q': "/tip?q=%E5%B7%A5%E4%B8%9A%E5%A4%A7%E9%81%93%E4%B8%AD381&city=%E5%B9%BF%E5%B7%9E%E5%B8%82&ak=a4fbd3a08ecc4f9e41bc9b06421ef3b5&opt=", \
                'district': ' 清风镇', \
                'country': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_14(self):
        data = {'q': '', \
                'city':'', \
                'country': '', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_15(self):
        data = {'q': '', \
                'country': 'US', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_16(self):
        data = {'q': '', \
                'city':'中国', \
                'country': 'US', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestPOST(url, data)
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

        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_18(self):
        data = {
            'country': 'CN', \
            'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)


    def test_19(self):
        data = {
            'q': '/*/*/*', \
            'city': '北京', \
            'country': 'CN', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestPOST(url, data)
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
        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)


    def test_21(self):
        data = {
            'q': '/*/*/*', \
            'city': '  \                                                                                                                                                                ', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestPOST(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

        def test_22(self):
            data = {'q': '天津市河北区润园里', \
                    'city': '', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('22get: ', res)

        #
        def test_23(self):
            data = {'q': '', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('23: ', res)

        def test_24(self):
            data = {'q': '美国', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)

            p.append(data)
            r.append(res)
            print('24: ', res)

        def test_25(self):
            data = {'q': '<scrpit>alert()</scrpit>', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('25: ', res)

        def test_26(self):
            data = {'q': '!@#$%^&*  （），。、(),./', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('26: ', res)

        def test_27(self):
            data = {'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('27: ', res)

        def test_28(self):
            data = {'q': '  !@#$%^&*:":"', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('28: ', res)

        def test_29(self):
            data = {'q': '  深圳市南山区海德3道3号', \
                    'opt': '', \
                    'ak': '14e9ee810854c40f5ae9414f2a62c8cc'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('29: ', res)

        # self.assertEqual(1,res['status'])

        def test_30(self):
            data = {'q': '  深圳市南山区海德3道3号', \
                    'city': '420100', \
                    'city': '北京', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('30: ', res)
            #		self.assertEqual(1,json.loads(res)['status'])

        def test_31(self):
            data = {'q': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
                    'opt': 'sf3', \

                    'city': '四川', \

                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('31: ', res)

        def test_32(self):
            data = {'q': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
                    'city': '四川', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('32: ', res)

        def test_33(self):
            data = {'q': '四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
                    'opt': '', \
                    'city': '511002', \
                    'normal': '1', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('33: ', res)

        def test_34(self):
            data = {'q': '#####', \
                    'opt': '', \

                    'city': '四川', \
                    'normal': '1', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('34: ', res)

        def test_35(self):
            data = {'q': '***\#\#\#\E\D---------------++++++++++++++++++++++++++++++++++++++++\+', \
                    'opt': '', \
                    'cc': '1', \
                    'city': '四川', \
                    'normal': '1', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('35: ', res)

        def test_36(self):
            data = {'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('36: ', res)

        def test_37(self):
            data = {'q': '北京北京市西城区新街口北大街59号万丰珠宝交易中心5010蔡晶收18612256180 \
    					北京北京市西城区新街口北大街59号万丰珠宝交易中心5010蔡晶收18612256180', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'
                    }
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('37: ', res)

        def test_38(self):
            '''city字段x s s'''
            data = {'q': '香港大学', \
                    'opt': '', \
                    'city': '香港', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('38: ', res)

        def test_39(self):
            data = {'q': '香港大学', \
                    'opt': '', \
                    'city': '香港', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('39: ', res)

        def test_40(self):
            data = {'q': 'ED四川省内江市市中区城西街道六段锦英伦别恋B幢2单元随和家宴堂', \
                    'opt': 'sf3', \
                    'cc': '1', \
                    'city': '@#$%^YJKM<>?\n""', \
                    'normal': '1', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('40: ', res)

        def test_41(self):
            data = {'q': 'ED?\##', \
                    'opt': 'sf3', \
                    'cc': '1', \
                    'city': '##@#$%^YJKM<>?\n""', \
                    'normal': '1', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('41: ', res)

        def test_42(self):
            data = {'q': '四川省成都市双流县天府新区剑南大道南段牧华路三段中信城左岸二栋二单元1506', \
                    'city': '', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('42: ', res)

    def test_43(self):
            data = {'q': 'DE##EwA9Ti6DRGg2yLcz5mY67Pii726vd4nTO2J%2Bx7TpNbiDrHzL', \
                    'city': '', \
                    'opt': '', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestPOST(url, data)
            p.append(data)
            r.append(res)
            print('43: ', res)

    @classmethod
    def tearDownClass(clz):
        reporttxt(name,url, p, r,n)




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(v_128))
    runner = unittest.TextTestRunner()
    runner.run(suite)
