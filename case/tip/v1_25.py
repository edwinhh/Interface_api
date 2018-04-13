import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *


url = 'http://GIS-RSS-PROXY.intsit.sfdc.com.cn:1080/tip'
#url='https://218.17.248.243:40115/tip'
#url='http://gis-ass-tip.intsit.sfdc.com.cn:1080/tip'
#url='http://10.202.95.115:9090/tip'
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]
n=[]
dic={}


class v_125(TestAbstract):

    def test_01(self):
        data = {'q': '"未央区明光路159号"', \
                'city': '西安', \
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestsget(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)
        self.assertNotIn('陕西西玛特机电设备有限公司',res['result'])
        #self.assertEqual('sw-tcp',res['result']['POISrc'])


    def test_02(self):
        data = {'q': '富士康', \
                'city': '440309', \
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)
        self.assertEqual('sw-tcp', res['result']['POISrc'])


    def test_03(self):
        data = {'q': '深圳福田中心城', \
                'district': '^&*(', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_04(self):
        data = {'q': '软件产业基地', \
                'district': '福田', \
                'city': '深圳', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_05(self):
        data = {'q': '软件产业基地', \
                'district': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)
        self.assertEqual('sw-tcp', res['result']['POISrc'])

    def test_06(self):
        data = {'q': '东山码头', \
                'district': '大鹏新区', \
                'city': '深圳', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_07(self):
        data = {'q': '葵涌街道三溪西路15号盘发门诊部', \
                'city': '深圳', \
                'district': '大鹏新区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_08(self):
        data = {'q': '白花洞白花园路第二工业区八佰工业园A栋2楼杰力五金制品有限公司', \
                'city': '深圳', \
                'district': '光明新区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)


    def test_09(self):
        data = {'q': '观澜君子布村田心工业区永祺塑胶有限公司', \
                'city': '深圳', \
                'district': '龙华区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    # self.assertEqual(1,res['status'])


    def test_10(self):
        data = {'q': '比亚迪路3009号六角大楼', \
                'city': '深圳', \
                'district': '坪山区', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)



    def test_11(self):
        data = {'q': "第一电台", \
                'opt': 'sf30', \
                'city': '深圳', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_12(self):
        data = {'q': '<span><script><a>深 圳 福 田 中 心 </a></script></span>', \
                'opt': '', \
                'district': '广州', \
                'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
                'ak': '94c9162319557b6e9102f0aeb4b3bf5d'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_13(self):
        data = {'q': "/tip?q=%E5%B7%A5%E4%B8%9A%E5%A4%A7%E9%81%93%E4%B8%AD381&city=%E5%B9%BF%E5%B7%9E%E5%B8%82&ak=a4fbd3a08ecc4f9e41bc9b06421ef3b5&opt=", \
                'district': ' 清风镇', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_14(self):
        data = {'q': '江苏省连云港市东海县白塔镇马小布村电话', \
                'city':'',\
                'opt': 'sf30', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_15(self):
        data = {
                'q': '南开大学', \
                'city': '天津市', \
                'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_16(self):
        data = {
            'q': '外滩', \
            'city': '上海', \
            'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)


    def test_17(self):
        data = {
            'q': '北京大学', \
            'city': '北京', \
            'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
            'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        n.append(sys._getframe().f_code.co_name)

    def test_18(self):
        data = {
            'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
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
    suite.addTest(unittest.makeSuite(v_125))
    runner = unittest.TextTestRunner()
    runner.run(suite)
