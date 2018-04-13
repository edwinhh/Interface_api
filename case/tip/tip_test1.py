import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *
import traceback
import time


#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
url1='http://10.202.95.115:9090/tip'
url2='http://10.202.95.116:9090/tip'
name = os.path.basename(__file__).split('.')[0]
p1=[]
r1=[]
p2=[]
r2=[]

file="e:/项目/输入提示/c++/HK1.txt"


class tip_test(TestAbstract):



    def __init__(self):
        self.__dict__ = {}
        self.num=0
        self.datas1=[]
        self.datas2=[]
        self.lista =[]


    def readcsv(self,file):
        with open(file, 'r', encoding='utf-8')as f:
            for line in f.readlines():
                self.num+=1
                temp=line.strip().split(",")

                data1 = {'q': temp[0], \
                        'opt': 'sf30', \
                        'city': "香港", \
                        'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
                self.datas1.append(data1)

                data2 = {'q': temp[0], \
                         'opt': '', \
                         'city': "香港", \
                         'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
                self.datas2.append(data2)

        for i in range(self.num):
            self.lista.append("test_" + str(i + 1))




    def __getattr__(self, attr):
        def test(url,data,p,r):
            res = self.requestGET(url, data)
            p.append(data)
            r.append(res)
            # try:
            #     assert 0 == res['status']
            # except AssertionError as ae:  # 明确抛出此异常
            #     # 抛出 AssertionError 不含任何信息，所以无法通过 ae.__str__()获取异常描述
            #     print('[AssertionError]', ae, ae.__str__())
            #     print('[traceback]')
            #     traceback.print_exc()
            #     print('assert except')



        self.__dict__[attr] =test
        return test




    # @classmethod
    # def tearDownClass(clz):
    #     reporttxt(name, url, p, r)


if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(geo_test))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    x = tip_test()
    x.readcsv(file)

    _= [getattr(x, i) for i in x.lista]
    j = 0
    for i in list(x.__dict__.keys()):


        if i in ['lista','num','datas1','datas2']:
            continue
  
        print("i=", i)
        x.i(url1, x.datas1[j],p1,r1)
        x.i(url1, x.datas2[j],p2,r2)
        j += 1

    reporttxt(name, url1, p1, r1)
    time.sleep(1)
    reporttxt(name, url2, p2, r2)


