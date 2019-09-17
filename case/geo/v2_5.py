import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import *

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url=geturl("geo")
ak=getak("ak")
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]


class v2_5(TestAbstract):
    def test_1(self):
        data = {'address': '广东省广州市天河区东莞庄路110号工业和信息化部电子第五研究所', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_2(self):
        data = {'address': '浙江省杭州市拱墅区，绍兴新村，6，1。502室', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_3(self):
        data = {'address': '香港大学', \
                'city':'香港',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)

        

    def test_4(self):
        data = {'address': '贵州省贵阳市南明区遵义路30号', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


    def test_5(self):
        data = {'address': '贵州省贵阳市南明区遵义社区服务中心贵阳龙洞堡国际机场集团公司数据室', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        

    def test_6(self):
        data = {'address': '浙江省杭州市拱墅区嘉兴工业园区启潮路199号B159', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        
    def test_7(self):
        data = {'address': '贵州省贵阳市南明区遵义县南白镇马家湾湘源国际负一层9号', \
                'city':'贵阳',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)
        
    def test_8(self):
        data = {'address': '贵州省贵阳市南明区遵义巷76号', \
                'city':'',\
                'span':'1',\
                'opt': 'sf30', \
                'ak':ak}
        res = self.requestGET(url, data)
        p.append(data)
        r.append(res)


   



    @classmethod
    def tearDownClass(clz):
        reporttxt(name, url, p, r)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(v2_5))
    runner = unittest.TextTestRunner()
    runner.run(suite)