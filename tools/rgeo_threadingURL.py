import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *
import traceback
from functools import partial
from pathos.multiprocessing import ProcessingPool
import threading
import time
import json


#将文档每行具体url链接拆分为参数，然后多线程执行
#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
# url='http://10.202.52.102:8080/geo'
# name = os.path.basename(__file__).split('.')[0]
# p=[]
# r=[]
p1=[]
r1=[]
filelist=[]
test=1
url1='http://10.203.32.185:8080/rgeo/api'
#url='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'

name = os.path.basename(__file__).split('.')[0]


file="e:/项目/逆地理编码/rgeo_e_test.csv"

#file="e:/项目/地理编码/数据/test.csv"


class geo_Mutest(TestAbstract):

    def __init__(self):
        self.num=0
        self.datas=[]


    def readcsv(self,file):
        with open(file, 'r', encoding='utf_8')as f:
            for line in f.readlines():
                self.num+=1
                if len(line)==1 or line.startswith('#') or len(line)==0:
                    continue
                if "?" in line:
                    p1=line.strip().split("?")
                    if p1[1]:
                        temp=p1[1].split("&")
                        x=temp[0].split("=")
                        y=temp[2].split("=")

                data = {'x': x[1], \
                        'opt': 'sf1', \
                        'y': y[1], \
                         'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}


                
                # data1 = {'address': temp[0], \
                #         'opt': '', \
                #         'city': "香港", \
                #          'span':"1", \
                #          'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
                # data2 = {'address': temp[0], \
                #         'opt': '', \
                #         'city': "香港", \
                #          'span':"1", \
                #          'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
                self.datas.append(data)

        f.close()
                

    def openfile(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        file2 = os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + name + "_" + now + ".txt"
        #os.mknod(rfile)
        #with open(file2, 'w+', encoding='utf_8')as f
        f=open(file2, 'a', encoding='utf_8')
        return f

    def openerror(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        file3 = os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + name + "_" +"error_"+now+ ".txt"
        #os.mknod(rfile)
        #with open(file2, 'w+', encoding='utf_8')as f
        err = open(file3, 'a', encoding='utf_8')
        return err
    
    def report(self, f,err, url, data, res):

        for i in range(len(res)):
            res1=json.loads(res[i])
            if res1["status"]==1:
                temp = []
                for key in data[i]:
                    temp.append(key + "=" + data[i][key])
                parameters = "&".join(temp)
                case = url + "?" + parameters
                err.write('\n')
                err.write(case)
                err.write('\n')
                err.write(str(res[i]))
                err.write('\n\n')
            # f.write(str(data[i]))
            # f.write('\n')
            #     err.write(str(res1))
            #     err.write('\n\n')
            else:
                temp = []
                for key in data[i]:
                    temp.append(key + "=" + data[i][key])
                parameters = "&".join(temp)
                case = url + "?" + parameters
                f.write(str(i + 1))
                f.write('\n')
                f.write(case)
                f.write('\n\n')
                # f.write(str(data[i]))
                # f.write('\n')
                f.write(str(res[i]))
                f.write('\n\n')


    
    def geo(self,data,url):
        global test
        
        for i in data:
            tp = []
            tr = []
            res = self.requestGET(url, i)
            tp.append(i)
            tr.append(res)
            p1.append(tp[0])
            r1.append(tr[0])
            print(test)
            test += 1
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
    splist=x.splist(x.datas,k)

    e1 = time.time()
    thread_list = []  # 线程存放列表
    for i in range(k):
        t = threading.Thread(target=x.geo, args=(splist[i], url1))
        t.setDaemon(True)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    e2 = time.time()
    print ("并行执行时间：", e2 - e1)
    # print(p1)
    # print('\n')
    # print(p2)
    # for i in p:
    #     print(i[0])
    #     print(i[1])
    f1= x.openfile()
    err1=x.openerror()
    x.report(f1,err1,url1, p1, r1)






