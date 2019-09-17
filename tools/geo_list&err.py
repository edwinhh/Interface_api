import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *
import traceback
from functools import partial
from pathos.multiprocessing import ProcessingPool
import threading

#读取dir指定路径下的白名单数据文本，并在e:\project\Interface_api-master\report 目录下生产四份结果文本
#Error_白名单的数据.csv  是请求返回status=1的集合
#白名单的数据.csv  是数据文本请求集合
#src.txt 是返回数据源走c++源的请求集合
#white.txt是将请求的地址和对应的adcode按照adcode，address格式生产文本，方便后续验证

url='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'
#url='http://10.203.33.36:8080/geo/api'
#url='http://10.203.120.62:8080/geo/api'

name = os.path.basename(__file__).split('.')[0]
test=1
adcode="e:/项目/地理编码/数据/adcode.csv"
dir="e:/项目/地理编码/数据/数据对比/"
filelist=[]

class geo_Mutest(TestAbstract):

    def __init__(self):
        self.num=0
        self.datas=[]
        self.my=[]
        self.p1 = []
        self.r1 = []

    def file_name(self,file_dir):
        for root, dirs, files in os.walk(file_dir):
            # print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录
            # print(files) #当前路径下所有非目录子文件
            filelist.append(files)
    def readadcode(self,file):
        with open(adcode, 'r', encoding='utf_8')as f:
            for line in f.readlines():
                self.num+=1
                temp=line.strip().split(",")
                if self.num==1:
                    continue
                else:
                    dic[temp[1]]=temp[0]
        
    def adcode (self,city):
        temp=city.split("|")
        if len(temp)==1:
            s=temp[0]
        if len(temp)==2:
            s=temp[1]
        if len(temp)==3:
            s=temp[2]
        if len(temp)==4:
            s=temp[3]
        k1=""
        v1=""
        for k, v in dic.items():
            if s in k:
                k1=k
                v1=v
        return k1,v1
    
    def reportadcode (self,res):
        res=json.loads(res)
        if res["status"]==0:
            adcode=res["result"]["adcode"]
            return adcode
        else:
            return 0
    
    def geocoder(self,my):
       my = json.loads(my)
       if len(my["geocoder"]):
           city=my["geocoder"][0]["city"]
           district=my["geocoder"][0]["district"]
           return city,district
       else:
           return 0
           
    
    def reportgeocder(self,res,city):
        #res = json.loads(res)
        if res["status"] == 0:
            adname = res["result"]["adname"]
            temp = city.split("|")
            if len(temp)==2 and temp[1] == adname[1] and temp[0] == adname[0]:
                    return 1
            if len(temp) ==3 and temp[2] == adname[2] and temp[1] == adname[1] and temp[0] == adname[0]:
                    return 1
            else:
                    return 0
            
            
    def reportadname(self,my,res):
        #res=json.loads(res)
        if res["status"]==0:
            adname=res["result"]["adname"]
        if adname[2]==my[1] and adname[1]==my[0]:
            return 1
        else:
            return 0

    def readcsv(self, file):
        with open(file, 'r', encoding='utf_8')as f:
            for line in f.readlines():
                #print(line)
                if len(line) == 1 or line.startswith('#'):
                    continue
                self.num += 1
                temp = line.strip().split(",")
                #print(temp)
                #temp = line.strip()
            
                data = {'address': temp[0], \
                         'opt': "ma1", \
                         'city': temp[1], \
                         'span': "1", \
                         'ak': 'bba16126b28f4d54b922cd45ea739efb'}

                self.datas.append(data)

    def openfile(self,file):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        file2 = os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + now+"_"+file
        #os.mknod(rfile)
        #with open(file2, 'w+', encoding='utf_8')as f
        f=open(file2, 'a', encoding='utf_8')
        return f
    

    def openerror(self,file):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        file3 = os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + now+"_Error_"+file
        #os.mknod(rfile)
        #with open(file2, 'w+', encoding='utf_8')as f
        err = open(file3, 'a', encoding='utf_8')
        return err

    def src(self, url, res, req):
        # res = []
        # req= []
        node = {}
        k = 0
        now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        src =os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + "src_"+ now+".txt"
        p = open(src, 'w', encoding='utf-8')
    
        for i in range(len(res)):
            if req[i]["status"]==0:
                if req[i]["result"]["src"] == "yy" or req[i]["result"]["src"] == "sf" or req[i]["result"]["src"] == "sw" or req[i]["result"]["src"] == "gf":
                    k = k + 1
                    temp = []
                    for key in res[i]:
                        temp.append(key + "=" + res[i][key])
                    parameters = "&".join(temp)
                    case = url + "?" + parameters
                    p.write(str(k))
                    p.write('\n')
                    p.write(case)
                    p.write('\n')
                    p.write(str(req[i]))
                    p.write('\n\n')

    def online(self, url, res, req):
        # res = []
        # req= []
        node = {}
        k = 0
        now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        online = os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + "online_" + now + ".txt"
        p = open(online, 'w', encoding='utf-8')
    
        for i in range(len(res)):
            if req[i]["status"] == 0:
                if req[i]["result"]["src"] == "bd" or req[i]["result"]["src"] == "gd" or req[i]["result"]["src"] == "tc":
                    k = k + 1
                    temp = []
                    for key in res[i]:
                        temp.append(key + "=" + res[i][key])
                    parameters = "&".join(temp)
                    case = url + "?" + parameters
                    p.write(str(k))
                    p.write('\n')
                    p.write(case)
                    p.write('\n')
                    p.write(str(req[i]))
                    p.write('\n\n')

    def white(self, url, res, req):
        # res = []
        # req= []
        node = {}
        k = 0
        now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        white = os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + "white_" + now + ".txt"
        p = open(white, 'w', encoding='utf-8')
    
        for i in range(len(res)):
            if req[i]["status"] == 0:
                if "w-" in req[i]["result"]["src"] :
                    k = k + 1
                    temp = []
                    for key in res[i]:
                        temp.append(key + "=" + res[i][key])
                    parameters = "&".join(temp)
                    case = url + "?" + parameters
                    p.write(str(k))
                    p.write('\n')
                    p.write(case)
                    p.write('\n')
                    p.write(str(req[i]))
                    p.write('\n\n')
                    
    def whitetxt(self, res, req):
        # res = []
        # req= []
        node = {}
        k = 0
        now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        whitetxt = os.path.dirname(os.path.dirname(__file__)) + '/report' + '/' + "whitetxt" + ".txt"
        p = open(whitetxt, 'w', encoding='utf-8')
    
        for i in range(len(res)):
                k = k + 1
                temp = []
                if req[i]["status"] == 0:
                    p.write(str(res[i]['address']))
                    p.write(',')
                    #print(req[i]['result'])
                    p.write(str(req[i]['result']['adcode']))
                    p.write('\n')
                    
    def report(self,f,err, url, data, res):
            
            #f.write(str(i + 1))
            f.write('\t')
            # f.write(n[i])
            f.write('\n')
            j = 1
            k=1
            for i in range(len(res)):
                k = k + 1
                #print (type(res[i]))
                #res1 = json.loads(res[i])
                if res[i]["status"] == 0:
                    temp = []
                    for key in data[i]:
                        temp.append(key + "=" + data[i][key])
                    parameters = "&".join(temp)
                    case = url + "?" + parameters
                    f.write(str(j))
                    f.write('\n')
                    f.write(case)
                    f.write('\n\n')
                    # f.write(str(data[i]))
                    # f.write('\n')
                    f.write(str(res[i]))
                    f.write('\n')
                    

                    
                else:
                    temp = []
                    for key in data[i]:
                        temp.append(key + "=" + data[i][key])
                    parameters = "&".join(temp)
                    case = url + "?" + parameters
                    #err.write(str(k))
                    err.write('\n')
                    err.write(case)
                    err.write('\n\n')
                    # f.write(str(data[i]))
                    # f.write('\n')
                    err.write(str(res[i]))
                    err.write('\n')
                    j=j+1
                
                    


    def geo1(self,data,url):
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

    def geo(self,data,url):
        global test
        for i in data:
            res1 = self.requestGET(url, i)
            p.append(i)
            r.append(res1)
            myr.append(res1)
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
    for root, dirs, files in os.walk(dir):
        filelist.append(files)

    e1 = time.time()
    for fo in filelist[0]:
        if "~" in fo:
            continue

        p = []
        r = []
        dic = {}
        my = []
        myp = []
        myr = []
        x = geo_Mutest()
        x.file_name(dir)
        x.readcsv(dir+fo)
        # f = x.openfile(fo)
        # err=x.openerror(fo)
        splist1=x.splist(x.datas,k)
        

        thread_list = []  # 线程存放列表
        for i in range(k):
            #print(splist1[i])
            t = threading.Thread(target=x.geo, args=(splist1[i],url))
            t.setDaemon(True)
            thread_list.append(t)

        for t in thread_list:

            t.start()

        for t in thread_list:
            t.join()

        #x.report(f,err, url, p, r)
        #f.close()
        #x.src(url, p, r)
        x.online(url, p, r)
        x.white(url, p, r)
        #x.whitetxt(p,r)
    e2 = time.time()
    print ("并行执行时间：", e2 - e1)





