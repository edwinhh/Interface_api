# -*- coding: utf-8 -*-
import unittest

from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-int.intsit.sfdc.com.cn:1080/rgeo/api'
#url='http://10.202.43.107:8080/rgeo'
url=geturl('rgeo')
name = os.path.basename(__file__).split('.')[0]
p = []
r = []


class gis_rgeo(TestAbstract):

    def test_1(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('1: ', res)
        self.assertEqual(1,res['status'])

    def test_2(self):
        data = {'x': '120.568292', \
                'y': '31.31020', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('2: ', res)

    # self.assertEqual(1,res['status'])

    def test_3(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('3: ', res)

    def test_4(self):
        data = {'x': '1', \
                'y': '1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('4: ', res)

    def test_5(self):
        data = {'x': '@#$', \
                'y': '@#$%^', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('5: ', res)

    def test_6(self):
        data = {'x': '', \
                'y': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('6: ', res)

    # opt=bd1

    def test_7(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('7: ', res)

    # self.assertEqual(0,res['status'])

    def test_8(self):
        data = {'x': '120.568292', \
                'y': '31.31020', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('8: ', res)

    # self.assertEqual(1,res['status'])

    def test_9(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('9: ', res)

    def test_10(self):
        data = {'x': '1', \
                'y': '1', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('10: ', res)

    def test_11(self):
        data = {'x': '@#$', \
                'y': '@#$%^', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('11: ', res)

    def test_12(self):
        data = {'x': '', \
                'y': '', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('12: ', res)

        # opt=bd2

    def test_13(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': 'bd2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('13: ', res)

        # self.assertEqual(0,res['status'])

    def test_14(self):
        data = {'x': '120.568292', \
                'y': '31.31020', \
                'opt': 'bd2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('14: ', res)

        # self.assertEqual(1,res['status'])

    def test_15(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': 'bd2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('15: ', res)

    def test_16(self):
        data = {'x': '1', \
                'y': '1', \
                'opt': 'bd2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('16: ', res)

    def test_17(self):
        data = {'x': '@#$', \
                'y': '@#$%^', \
                'opt': 'bd2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('17: ', res)

    def test_18(self):
        data = {'x': '', \
                'y': '', \
                'opt': 'bd2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('18: ', res)

            # opt=gd1

    def test_19(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('19: ', res)

            # self.assertEqual(0,res['status'])

    def test_20(self):
        data = {'x': '120.568292', \
                'y': '31.31020', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('20: ', res)

            # self.assertEqual(1,res['status'])

    def test_21(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('21: ', res)

    def test_22(self):
        data = {'x': '1', \
                'y': '1', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('22: ', res)

    def test_23(self):
        data = {'x': '@#$', \
                'y': '@#$%^', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('23: ', res)

    def test_24(self):
        data = {'x': '', \
                'y': '', \
                'opt': 'gd1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('24: ', res)

 # opt=gd2

    def test_25(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('25: ', res)

            # self.assertEqual(0,res['status'])

    def test_26(self):
        data = {'x': '120.568292', \
                'y': '31.31020', \
                'opt': '', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('26: ', res)

                # self.assertEqual(1,res['status'])

    def test_27(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('27: ', res)

    def test_28(self):
        data = {'x': '1', \
                'y': '1', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('28: ', res)

    def test_29(self):
        data = {'x': '@#$', \
                'y': '@#$%^', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('29: ', res)

    def test_30(self):
        data = {'x': '&&', \
                'y': '&', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('30: ', res)

    def test_30(self):
        data = {'x': '  ', \
                'y': '   ', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('30: ', res)

# opt=sf1

    def test_31(self):
        data = {'x': '<scrpit>alert("深圳")</scrpit>', \
                'y': '', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('31: ', res)

                # self.assertEqual(0,res['status'])

    def test_32(self):
            data = {'x': '海上世界', \
                    'y': '深圳市', \
                    'opt': '', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestGET(url, data)
            p.append(data)
            r.append(res)
            print('32: ', res)

                # self.assertEqual(1,res['status'])

    def test_33(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('33: ', res)

    def test_34(self):
        data = {'x': '1', \
                'y': '1', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('34: ', res)

    def test_35(self):
        data = {'x': '@#$', \
                'y': '@#$%^', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('35: ', res)

    def test_36(self):
        data = {'x': '', \
                'y': '', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('36: ', res)

#opt=sf2
    def test_37(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('37: ', res)

                # self.assertEqual(0,res['status'])

    def test_38(self):
            data = {'x': '120.568292', \
                    'y': '31.31020', \
                    'opt': 'sf2', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestGET(url, data)
            p.append(data)
            r.append(res)
            print('38: ', res)

                # self.assertEqual(1,res['status'])

    def test_39(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('39: ', res)

    def test_40(self):
        data = {'x': '1', \
                'y': '1', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('40: ', res)

    def test_41(self):
        data = {'x': '@#$', \
                'y': '@#$%^', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('41: ', res)

    def test_42(self):
        data = {'x': '', \
                'y': '', \
                'opt': 'sf2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('42: ', res)



#cc=1
    def test_43(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': '', \
                'cc':'1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('43: ', res)

                # self.assertEqual(0,res['status'])

    def test_44(self):
            data = {'x': '120.568292', \
                    'y': '31.31020', \
                    'opt': 'sf2', \
                    'cc': '1', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestGET(url, data)
            p.append(data)
            r.append(res)
            print('44: ', res)

                # self.assertEqual(1,res['status'])

    def test_45(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': 'gd1', \
                'cc': '1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('45: ', res)

    def test_46(self):
        data = {'x': '1', \
                'y': '1', \
                'opt': '', \
                'cc': '1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('46: ', res)

    def test_47(self):
        data = {'x': '@#$', \
                'y': '@#$%^', \
                'opt': 'bd2', \
                'cc': '1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('47: ', res)

    def test_48(self):
        data = {'x': '', \
                'y': '', \
                'opt': '', \
                'cc': '1', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('48: ', res)

   #cc=2
    def test_49(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'opt': '', \
                'cc':'2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('49: ', res)

                # self.assertEqual(0,res['status'])

    def test_50(self):
            data = {'x': '120.568292', \
                    'y': '31.31020', \
                    'opt': 'sf2', \
                    'cc': '2', \
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
            res = self.requestGET(url, data)
            p.append(data)
            r.append(res)
            print('50: ', res)

                # self.assertEqual(1,res['status'])

    def test_51(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': 'gd1', \
                'cc': '2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('51: ', res)

    def test_52(self):
        data = {'x': '1', \
                'y': '1', \
                'opt': '', \
                'cc': '2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('52: ', res)

    def test_53(self):
        data = {'x': '@#$', \
                'y': '@#$%^', \
                'opt': 'bd2', \
                'cc': '2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('53: ', res)

    def test_54(self):
        data = {'x': '', \
                'y': '', \
                'opt': '', \
                'cc': '2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('54: ', res)

#异常处理
    def test_55(self):
        data = {'x': '', \
                'y': '', \
                'opt': '', \
                'cc': '-36', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('55: ', res)

    def test_56(self):
        data = {
                    'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('56: ', res)

    def test_57(self):
        data = {'x': '', \
                'y': '', \
                'opt': '', \
                'cc': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('57: ', res)

    def test_58(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': 'sw-1', \
                'cc': '2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('58: ', res)

    def test_59(self):
        data = {'x': '22.5410116566', \
                'y': '113.97655634968', \
                'opt': '&@!#$', \
                'cc': '2', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('59: ', res)
    
    def test_60(self):
        data = {'x': '0', \
                'y': '0', \
                'ak': 'f3ac165ec3410fff5d2601448134b1b6'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('60: ', res)
#
    def test_61(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'poinum': '100',\
                'ak': 'f3ac165ec3410fff5d2601448134b1b6'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('61: ', res)
        
    def test_62(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'poinum': '0', \
                'ak': 'f3ac165ec3410fff5d2601448134b1b6'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('62: ', res)

    def test_63(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'poinum': '', \
                'ak': 'f3ac165ec3410fff5d2601448134b1b6'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('63: ', res)
        
    def test_64(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'poinum': '%^&*', \
                'ak': 'f3ac165ec3410fff5d2601448134b1b6'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('64: ', res)
        
    def test_65(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'poinum': '你好aab', \
                'ak': 'f3ac165ec3410fff5d2601448134b1b6'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('65: ', res)
        
    def test_66(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'poinum': '1', \
                'ak': 'f3ac165ec3410fff5d2601448134b1b6'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('66: ', res)
        
    def test_67(self):
        data = {'x': '114.036919', \
                'y': '22.604069', \
                'poinum': '10', \
                'ak': 'f3ac165ec3410fff5d2601448134b1b6'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        print('67: ', res)


    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(gis_rgeo))
    runner = unittest.TextTestRunner()
    runner.run(suite)
#
#
#
#
# suite = unittest.TestSuite()
# suite.addTest(gis_geo1("test_5"))
# runner = unittest.TextTestRunner()
# runner.run(suite)
