import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *
import traceback
from functools import partial
from pathos.multiprocessing import ProcessingPool
from multiprocessing import Pool

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
# url='http://10.202.52.102:8080/geo'
# name = os.path.basename(__file__).split('.')[0]
# p=[]
# r=[]
url='http://10.202.52.103:8080/geo'
name = os.path.basename(__file__).split('.')[0]

p=[]

r=[]

file="e:/项目/地理编码/数据/new3.txt"
#file="e:/项目/地理编码/数据/test.csv"


class geo_Mutest(TestAbstract):



    def __init__(self):
        self.num=0
        self.datas=[]
        self.p1 = []
        self.r1 = []

    def readcsv(self,file):
        with open(file, 'r', encoding='utf_8')as f:
            for line in f.readlines():
                self.num+=1
                temp=line.strip().split(",")

                data = {'address': temp[0], \
                        'opt': 'sf30', \
                        'city': "", \
                        'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
                self.datas.append(data)

    def openfile(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        file2 = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/report' + '/' + name + "_" + now + ".txt"
        #os.mknod(rfile)
        #with open(file2, 'w+', encoding='utf_8')as f
        f=open(file2, 'a', encoding='utf_8')
        return f

    def report(self,f, url, data, res):
            temp=[]
            print(data)
            print(res)
            #f.write(str(i + 1))
            f.write('\t')
            # f.write(n[i])
            f.write('\n')
            for key in data:
                temp.append(key + "=" + data[key])
            parameters = "&".join(temp)
            case = url + "?" + parameters
            f.write(case)
            f.write('\n\n')
            f.write(str(data))
            f.write('\n')
            f.write(str(res))
            f.write('\n\n\n')


    def geo(self,data,url):
        res = self.requestGET(url, data)
        self.p1.append(data)
        self.r1.append(res)
        p.append(data)
        r.append(res)
        
        #print(res)
        #kl.append(data)
        return res
        #self.report(self,f, url, data, res)

        # try:
        #     assert 0 == res['status']
        # except AssertionError as ae:  # 明确抛出此异常
        #         # 抛出 AssertionError 不含任何信息，所以无法通过 ae.__str__()获取异常描述
        #     print('[AssertionError]', ae, ae.__str__())
        #     print('[traceback]')
        #     traceback.print_exc()
        #     print('assert except')

    def geo2(self,data,url):
        res = self.requestGET(url, data)
        #print(len(p))
        p.append(data)
        r.append(res)

        # try:
        #     assert 0 == res['status']
        # except AssertionError as ae:  # 明确抛出此异常
        #         # 抛出 AssertionError 不含任何信息，所以无法通过 ae.__str__()获取异常描述
        #     print('[AssertionError]', ae, ae.__str__())
        #     print('[traceback]')
        #     traceback.print_exc()
        #     print('assert except')




if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(geo_test))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    k=5
    x = geo_Mutest()
    x.readcsv(file)
    f = x.openfile()
    



    #
    #
    s = time.time()
    # for i in x.datas:
    #     x.geo(i)
    # e=time.time()
    # print(p)
    # reporttxt(name,url, p, r)
    # print("执行时间：",e-s)




    uu=[]
    for i in range(len(x.datas)):
        uu.append(url)
    z=zip(x.datas,uu)

    pool = Pool(k)  # 创建拥有5个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数

    #px= partial(x.geo, url=url)
    e1 = time.time()
   # pool.map(x.geo,x.datas,uu)
    for i in x.datas:
        pool.apply_async(x.geo2,(i,url))


    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    e2 = time.time()
    

    print ("并行执行时间：", e2 - e1)
    # print("p:",len(p))
    # x.report(f, url,x.p1, x.r1)geo_Mutest.py
    x.report(f, url,p,r)
    # reporttxt(name, url, p, r)





