import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *
import traceback
from functools import partial
from pathos.multiprocessing import ProcessingPool
import threading
import time


#做新旧对比，将文档每行具体地址通过,拆分为参数，然后多线程执行


#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
# url='http://10.202.52.102:8080/geo'
# name = os.path.basename(__file__).split('.')[0]
# p=[]
# r=[]
url1='http://10.202.52.102:8080/geo'
url2='http://10.202.52.103:8080/geo'
# url1='http://10.202.95.115:8899/geo'
# url2='http://10.202.95.115:9091/geo'
name = os.path.basename(__file__).split('.')[0]
p1=[]
r1=[]
p2=[]
r2=[]
filelist=[]
test=1

file="e:/项目/地理编码/数据/cxtest.txt"
#file="e:/项目/地理编码/数据/test.csv"


class geo_Mutest(TestAbstract):



    def __init__(self):
        self.num=0
        self.datas1=[]
        self.datas2 = []

    def readcsv(self,file):
        with open(file, 'r', encoding='utf_8')as f:
            for line in f.readlines():
                if len(line)==1 or line.startswith('#'):
                    continue
                self.num+=1
                temp=line.strip().split(",")


                data1 = {'address': temp[0], \
                        'opt': "sf30", \
                        'city': temp[1], \
                         'span':"1", \
                         'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
                data2 = {'address': temp[0], \
                        'opt': "sf30", \
                        'city': temp[1], \
                         'span':"1", \
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
                self.datas1.append(data1)
                self.datas2.append(data2)
                

    def openfile(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        file2 = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/report' + '/' + name + "_" + now + ".txt"
        filelist.append(file2)
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

                if json.loads(res[i])["status"]==0:
                    f.write("xcoord:")
                    f.write(str(json.loads(res[i])["result"]["xcoord"]))
                    f.write(',')
                    f.write("ycoord:")
                    f.write(str(json.loads(res[i])["result"]["ycoord"]))
                else:
                    f.write("坐标无返回")
                f.write('\n\n')

    def err(self, url, oldres, newreq, newres):
        reqnew = []
        resnew = []
        resold = []
        node = {}
        now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        diff = "e:/project/Interface_api-master/report/" + "diff_" + now + ".txt"
        p = open(diff, 'w', encoding='utf-8')
        # p.write("#address,node_adcode")
        # p.write("\n")
        # with open(old, 'r', encoding='utf-8') as f:
        #     for line in f.readlines():
        #         if '"status"' in line:
        #             # r = line.split("?")[1].split("&")[0].split("=")[1]
        #             resnew.append(line)
        #         if "http://" in line:
        #             reqnew.append(line)
        #
        # with open(new, 'r', encoding='utf-8') as f:
        #     for line in f.readlines():
        #         if '"status"' in line:
        #             # r = line.split("?")[1].split("&")[0].split("=")[1]
        #             resold.append(line)
        # for i in range(min(len(resnew), len(resold))):
        #     if json.loads(resnew[i])["status"] == 1 and json.loads(resold[i])["status"] == 0:
        #         p.write(reqnew[i])
        #         p.write('\n')
        for i in range(min(len(oldres), len(newres))):
            # print (json.loads(newres[i])["status"])
            # print ("&")
            # print (type(json.loads(oldres[i])["status"]))
        
            if json.loads(newres[i])["status"] == "1" and json.loads(oldres[i])["status"] == 0:
                temp = []
                for key in newreq[i]:
                    temp.append(key + "=" + newreq[i][key])
                parameters = "&".join(temp)
                case = url + "?" + parameters
                p.write(case)
                p.write('\n')
                p.write(newres[i])
                p.write('\n\n')

    def geo(self,data,url,p,r):
        global test
        for i in data:
            res = self.requestGET(url, i)
            p.append(i)
            r.append(res)
            # print(test)
            test += 1


        # try:
        #     assert 0 == res['status']
        # except AssertionError as ae:  # 明确抛出此异常
        #         # 抛出 AssertionError 不含任何信息，所以无法通过 ae.__str__()获取异常描述
        #     print('[AssertionError]', ae, ae.__str__())
        #     print('[traceback]')
        #     traceback.print_exc()
        #     print('assert except')
    
    def geo2(self,data,url1,url2):
        global test
        
        for i in data:
            tp = []
            tr = []
            res = self.requestGET(url1, i)
            tp.append(i)
            tr.append(res)
            res = self.requestGET(url2, i)
            tp.append(i)
            tr.append(res)
            p1.append(tp[0])
            r1.append(tr[0])
            p2.append(tp[1])
            r2.append(tr[1])
            print(test)
            test += 1
            



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

    k=16
    x = geo_Mutest()
    x.readcsv(file)
    splist=x.splist(x.datas1,k)



    e1 = time.time()
    thread_list = []  # 线程存放列表
    for i in range(k):
        t = threading.Thread(target=x.geo2, args=(splist[i],url1,url2))
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
    f1 = x.openfile()
    x.report(f1, url1, p1, r1)
    time.sleep(1)
    f2 = x.openfile()
    x.report(f2, url2, p2, r2)
    x.err(url2,r1,p2,r2)






