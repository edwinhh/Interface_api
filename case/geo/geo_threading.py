import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *
import traceback
from functools import partial
from pathos.multiprocessing import ProcessingPool
import threading

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
# url='http://10.202.52.102:8080/geo'
# name = os.path.basename(__file__).split('.')[0]
# p=[]
# r=[]
url='http://10.202.52.103:8080/geo'
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]
test=1

file="e:/项目/地理编码/数据/new1.txt"
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
            
            #f.write(str(i + 1))
            f.write('\t')
            # f.write(n[i])
            f.write('\n')
            for i in range(len(data)):
                temp = []
                for key in data[i]:
                    temp.append(key + "=" + data[i][key])
                parameters = "&".join(temp)
                case = url + "?" + parameters
                f.write(str(i+1))
                f.write('\n')
                f.write(case)
                f.write('\n\n')
                # f.write(str(data[i]))
                # f.write('\n')
                f.write(str(res[i]))
                f.write('\n\n')


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
        global test
        for i in data:
            res = self.requestGET(url, i)
            p.append(i)
            r.append(res)
            print(test)
            test=test+1

        # try:
        #     assert 0 == res['status']
        # except AssertionError as ae:  # 明确抛出此异常
        #         # 抛出 AssertionError 不含任何信息，所以无法通过 ae.__str__()获取异常描述
        #     print('[AssertionError]', ae, ae.__str__())
        #     print('[traceback]')
        #     traceback.print_exc()
        #     print('assert except')

    def splist(self,ls,n):
        if not isinstance(ls, list) or not isinstance(n, int):
            return []
        ls_len = len(ls)
        if n <= 0 or 0 == ls_len:
            return []
        if n > ls_len:
            return []
        elif n == ls_len:
            return [[i] for i in ls]
        else:
            j = int(ls_len / n)
            k = int(ls_len % n)
            ### j,j,j,...(前面有n-1个j),j+k
            # 步长j,次数n-1
            ls_return = []
            for i in range(0, (n - 1) * j, j):
                ls_return.append(ls[i:i + j])
                # 算上末尾的j+k
            ls_return.append(ls[(n - 1) * j:])
            return ls_return




if __name__ == "__main__":

    k=8
    x = geo_Mutest()
    x.readcsv(file)
    f = x.openfile()
    splist=x.splist(x.datas,k)



    e1 = time.time()
    thread_list = []  # 线程存放列表
    for i in range(k):
        t = threading.Thread(target=x.geo2, args=(splist[i],url))
        t.setDaemon(True)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    e2 = time.time()
    print ("并行执行时间：", e2 - e1)
    x.report(f, url, p, r)





