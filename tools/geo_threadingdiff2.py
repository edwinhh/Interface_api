import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *
import traceback
from functools import partial
from pathos.multiprocessing import ProcessingPool
import threading
import time,copy


#做新旧对比，将文档每行具体地址通过,拆分为参数，然后多线程执行
p1=[]
r1=[]
p2=[]
r2=[]
t1=[]
t2=[]
filelist=[]
test=1

#url2='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'

#url1='http://10.202.52.103:8080/geo'
url1='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'
url2='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'

name = os.path.basename(__file__).split('.')[0]

file="e:/项目/地理编码/数据/104错误.csv"
#file="e:/项目/地理编码/数据/cx2.csv"

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
                        'opt': "ma1", \
                        'city': temp[1],\
                         'ak': 'bba16126b28f4d54b922cd45ea739efb'}
                         
                data2 = {'address': temp[0], \
                        'opt': "sf30", \
                        'city': temp[1], \
                         'ak': 'bba16126b28f4d54b922cd45ea739efb'}
                
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
                #self.datas2.append(data2)
                

    def openfile(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        #file2 = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/report' + '/' + name + "_" + now + ".txt"
        file2 = os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + name + "_" + now + ".txt"
        filelist.append(file2)
        #os.mknod(rfile)
        #with open(file2, 'w+', encoding='utf_8')as f
        f=open(file2, 'a', encoding='utf_8')
        return f

    def report(self,f, url, data, res,time):
            
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
                f.write(str(res[i]))
                f.write('\n')
                f.write("耗时：")
                f.write(str(time[i]))
                f.write('\n\n')

  

    def err(self, url, oldres, newreq, newres):
        reqnew = []
        resnew = []
        resold = []
        node = {}
        k=0
        now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        diff = "e:/project/Interface_api-master/report/" + "err_" + now + ".txt"
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
            #print (oldres[i]["status"])
            if newres[i]["status"] == 1 and oldres[i]["status"] == 0:
                k=k+1
                temp = []
                for key in newreq[i]:
                    temp.append(key + "=" + newreq[i][key])
                parameters = "&".join(temp)
                case = url + "?" + parameters
                p.write(str(k))
                p.write('\n')
                p.write(case)
                p.write('\n')
                p.write(str(newres[i]))
                p.write('\n')
                print("old:")
                p.write(str(oldres[i]))
                p.write('\n\n')
                
    def empty(self, url, oldres, newreq, newres):
        reqnew = []
        resnew = []
        resold = []
        node = {}
        k=0
        now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        empty = "e:/project/Interface_api-master/report/" + "empty_" + now + ".txt"
        p = open(empty, 'w', encoding='utf-8')

        for i in range(min(len(oldres), len(newres))):
            # if json.loads(oldres[i])["status"] == 0:
            #     print (json.loads(oldres[i])["result"]["src"])
            
            # print ("&")
            # print (type(json.loads(oldres[i])["status"]))
            if newres[i]["status"] == 0 and oldres[i]["status"] == 0:
                if newres[i]["result"]["src"] == "empty" and oldres[i]["result"]["src"] != "empty":
                    k=k+1
                    temp = []
                    for key in newreq[i]:
                        temp.append(key + "=" + newreq[i][key])
                    parameters = "&".join(temp)
                    case = url + "?" + parameters
                    p.write(str(k))
                    p.write('\n')
                    p.write(case)
                    p.write('\n')
                    p.write(str(newres[i]))
                    p.write('\n\n')



    # def geo1(self,data,url1):
    #     global test
    #
    #     for i in data:
    #         tp = []
    #         tr = []
    #         i.update({'ak':'a4fbd3a08ecc4f9e41bc9b06421ef3b5'})
    #         res = self.requestGET(url1, i)
    #         tp.append(i)
    #         tr.append(res)
    #         p1.append(tp[0])
    #         r1.append(tr[0])
	#
    #         print(test)
    #         test += 1


        # try:
        #     assert 0 == res['status']
        # except AssertionError as ae:  # 明确抛出此异常
        #         # 抛出 AssertionError 不含任何信息，所以无法通过 ae.__str__()获取异常描述
        #     print('[AssertionError]', ae, ae.__str__())
        #     print('[traceback]')
        #     traceback.print_exc()
        #     print('assert except')

    def tmnew(self, url, newtime,oldtime, newreq, newres):
        reqnew = []
        resnew = []
        resold = []
        dic = {}
        k=0
        
        now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        diff = "e:/project/Interface_api-master/report/" + "timenew_" + now + ".txt"
        p = open(diff, 'w', encoding='utf-8')
        
        for i in range(min(len(newres), len(newres))):
            #print(type(i))
            if newtime[i]>oldtime[i]:
                dic[newtime[i]-oldtime[i]]=i
            timedic = sorted(dic.items(), key=lambda d: d[0], reverse=True)
        

            
        for key in timedic:
            k = k + 1
            temp = []
            for i in newreq[key[1]]:
                temp.append(i + "=" + newreq[key[1]][i])
                #for key in newreq[i]:
                #temp.append(key + "=" + newreq[i][key])
            parameters = "&".join(temp)
            case = url + "?" + parameters
            p.write(str(k))
            p.write('\n')
            p.write(case)
            p.write('\n')
            p.write(str(newres[key[1]]))
            p.write('\n')
            p.write("规范化耗时:")
            p.write(str(newtime[key[1]]))
            p.write('\n')
            p.write("非规范化耗时:")
            p.write(str(oldtime[key[1]]))
            p.write('\n\n')

    def tmold(self, url, newtime, oldtime, newreq, newres):
        reqnew = []
        resnew = []
        resold = []
        dic = {}
        k = 0
        now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        diff = "e:/project/Interface_api-master/report/" + "timeold_" + now + ".txt"
        p = open(diff, 'w', encoding='utf-8')
    
        for i in range(min(len(newres), len(newres))):
            # print(type(i))
            if newtime[i] < oldtime[i]:
                dic[oldtime[i]-newtime[i]]= i
            timedic = sorted(dic.items(), key=lambda d: d[0], reverse=True)
    
        for key in timedic:
            k = k + 1
            temp = []
            for i in newreq[key[1]]:
                temp.append(i + "=" + newreq[key[1]][i])
                # for key in newreq[i]:
                # temp.append(key + "=" + newreq[i][key])
            parameters = "&".join(temp)
            case = url + "?" + parameters
            p.write(str(k))
            p.write('\n')
            p.write(case)
            p.write('\n')
            p.write(str(newres[key[1]]))
            p.write('\n')
            p.write("规范化耗时:")
            p.write(str(newtime[key[1]]))
            p.write('\n')
            p.write("非规范化耗时:")
            p.write(str(oldtime[key[1]]))
            p.write('\n\n')

    
    def geo2(self,data,url2):
        global test
        
        for i in data:
            tp1 = []
            tr1 = []
            tp2 = []
            tr2 = []
            te1= []
            te2 = []
            i.update({'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'})
            temp=copy.deepcopy(i)
            tp1.append(temp)
            e1=time.time()
            res1 = self.requestGET(url1, i)
            e2 = time.time()
            te1.append(e2-e1)

            i.update({'ak': 'dd28da5cdde84c62acf758a7fabe4362'})
            tp2.append(i)
            e3 = time.time()
            res2 = self.requestGET(url1, i)
            e4 = time.time()
            te2.append(e4 - e3)
            e1 = time.time()
            tr1.append(res1)
            tr2.append(res2)
            p1.append(tp1[0])
            r1.append(tr1[0])
            t1.append(te1[0])
            p2.append(tp2[0])
            r2.append(tr2[0])
            t2.append(te2[0])
            print(test)
            test += 1

    # def report(name, url, p, r,t):
    #     now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    #     wb = Workbook()
    #     ws1 = wb.create_sheet(title=name)
    #     # 给第一行、第一列赋值，此处不同版本，起始行号可能不同
    #     ws1.cell(row=1, column=1).value = url
    #     print(len(p))
    #     for rowNum in range(1, len(p) + 1):
    #         ws1.cell(row=rowNum, column=2).value = str(p[rowNum - 1])
    #         ws1.cell(row=rowNum, column=3).value = str(r[rowNum - 1])
    #     wb.save(name + now + ".xlsx")

  


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
    splist=x.splist(x.datas1,k)



    
    thread_list1 = []  # 线程存放列表
    e1 = time.time()
    for i in range(k):
        t = threading.Thread(target=x.geo2, args=(splist[i],url1))
        t.setDaemon(True)
        thread_list1.append(t)

    for t in thread_list1:
        t.start()

    for t in thread_list1:
        t.join()

    e2 = time.time()
    

    # e3 = time.time()
    # for i in range(k):
    #     t = threading.Thread(target=x.geo2, args=(splist[i],url1))
    #     t.setDaemon(True)
    #     thread_list2.append(t)
	#
    # for t in thread_list2:
    #     t.start()
	#
    # for t in thread_list2:
    #     t.join()
	#
    # e4 = time.time()
    # print ("url1执行时间：", e2 - e1)
    # print ("url2执行时间：", e4 - e3)
    # print(p1)
    # print('\n')
    # print(p2)
    # for i in p:
    #     print(i[0])
    #     print(i[1])
    f1 = x.openfile()
    x.report(f1, url1, p1, r1,t1)
    time.sleep(1)
    f2 = x.openfile()
    x.report(f2, url2, p2, r2,t2)
    x.err(url2,r1,p2,r2)
    x.tmnew(url2,t2,t1,p2,r2)
    x.tmold(url2, t2, t1, p2, r2)
    #x.empty(url2, r1, p2, r2)






