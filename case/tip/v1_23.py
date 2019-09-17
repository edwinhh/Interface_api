import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url=geturl("tip")
#url='http://gis-ass-tip.intsit.sfdc.com.cn:1080/tip'
url=geturl("tip")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]
dic={}


class tip1_23(TestAbstract):

    def test_1(self):
        data = {'q': '章贡区迎宾大道74号', \
                'opt': '', \
                'city': '赣州', \
                'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

    #self.assertEqual(0,res['status'])

    def test_2(self):
        data = {'q': '深 圳 福 田 中 心 <script><a>alert(1)</a></script> 城', \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
    # self.assertEqual(1,res['status'])


    def test_3(self):
        data = {'q': '<a style = “TEST:e-xpression(alert(/深 圳 福 田 中 心/))”></a>', \
                'opt': '', \
                'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)



    def test_4(self):
        data = {'q': "<input type=\"text\" value=\"深圳市\" onclick=\"javascript:alert('handsome boy')\">", \
                'opt': '', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'q': '<span><script><a>深 圳 福 田 中 心 </a></script></span>', \
                'opt': '', \
                'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
                'ak': '94c9162319557b6e9102f0aeb4b3bf5d'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_6(self):
        data = {'q': "/tip?q=%E5%B7%A5%E4%B8%9A%E5%A4%A7%E9%81%93%E4%B8%AD381&city=%E5%B9%BF%E5%B7%9E%E5%B8%82&ak=a4fbd3a08ecc4f9e41bc9b06421ef3b5&opt=", \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_6(self):
        data = {'q': '<span>&lt;script&gt;alert(&#39;handsome boy&#39;)&lt;/script&gt</span>', \
                'opt': '', \
                'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_7(self):
        data = {
                'cb': 'jQuery19108708458041159374_150753396075545778<script>alert(1)</script>&_=1507533960756', \
                'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}

        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)




    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r,"get")




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip1_23))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    suite=unittest.TestResult()
