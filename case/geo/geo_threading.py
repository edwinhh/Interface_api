import os,sys,unittest,time,json
from lib.test_abstract import TestAbstract
from lib.wxls import *
import traceback
from functools import partial
from pathos.multiprocessing import ProcessingPool
import threading

#不做对比，将省市区街道作为city和adress

#url = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'
# url='http://10.202.52.102:8080/geo'
# name = os.path.basename(__file__).split('.')[0]
# p=[]
# r=[]
url='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'
name = os.path.basename(__file__).split('.')[0]
p=[]
r=[]
test=1
dic={}
my=[]
myp=[]
myr=[]
dir="e:/项目/地理编码/数据/数据对比/"
file="香港派件-20190225.csv"
adcode="e:/项目/地理编码/数据/adcode.csv"
#file="e:/项目/地理编码/数据/test.csv"


class geo_Mutest(TestAbstract):



    def __init__(self):
        self.num=0
        self.datas=[]
        self.my=[]
        self.p1 = []
        self.r1 = []

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
           
    
    # def reportgeocder(self,my,city):
    #     # my=self.geocoder(my)
    #     if my:
    #         temp = city.split("|")
    #         if temp[2]==my[1] and temp[1]==my[0]:
    #             return 1
    #         else:
    #             return 0
    
    def reportgeocder(self,res,city):
        res = json.loads(res)
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
        res=json.loads(res)
        if res["status"]==0:
            adname=res["result"]["adname"]
        if adname[2]==my[1] and adname[1]==my[0]:
            return 1
        else:
            return 0
            
    
    
        

    def readcsv(self, file):
        with open(file, 'r', encoding='utf_8')as f:
            for line in f.readlines():
                my=[]
                self.num += 1
                # temp=line.strip().split(",")
            
                # address = line.replace('\n', '').replace('\t', '')
                # city = line.replace('\n', '').replace('\t', '|')
                if len(line)==1 or line.startswith('#'):
                    continue
                address=line.strip().split(",")[1]
                city = line.strip().split(",")[2]
            
                data = {'address': address, \
                        'opt': '', \
                        'city': city, \
                        'ak':"bba16126b28f4d54b922cd45ea739efb"}
                my.append(data)
                
                mydata = {'address': address, \
                        'opt': '', \
                        'city': city, \
                        'ak':"bba16126b28f4d54b922cd45ea739efb"}
                my.append(mydata)
                self.datas.append(my)

    def openfile(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        file2 = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/report' + '/' + name + "_" + now +file+".txt"
        #os.mknod(rfile)
        #with open(file2, 'w+', encoding='utf_8')as f
        f=open(file2, 'a', encoding='utf_8')
        return f

    def report(self,f, url, data, res,myr):
            
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
                f.write('\n')
                # my=self.geocoder(myr[i])
                # if my:
                #     f.write("geocoder返回city:")
                #     f.write(my[0])
                #     f.write('\n')
                #     f.write("geocoder返回district:")
                #     f.write(my[1])
                #     f.write('\n')
                #     if self.reportgeocder(res[i],data[i]['city']):
                #         f.write("city与adname对比:相同\n")
                #     else:
                #         f.write("city与adname对比:不相同\n")
                #     adname=self.reportadname(my,res[i])
                #     if adname:
                #         f.write("geocoder与adname对比:相同\n")
                #     else:
                #         f.write("geocoder与adname对比:不相同\n")
                # f.write('\n')
                # adcode2 = self.reportadcode(res[i])
                # # if adcode2:
                # #     adcode1 = self.adcode(data[i]['city'])[1]
                # #     f.write("adcode:")
                # #     f.write(adcode1)
                # #     f.write('\n')
                # #     f.write("adcode对比:")
                # #     if adcode1==adcode2:
                # #         f.write("一致")
                # #     else:
                # #         f.write("不相同")
                #
                # f.write('\n\n')


    def geo(self,data,url):
        global test
        for i in data:
            res1 = self.requestGET(url, i[0])
            #res2 = self.requestGET(url, i[1])
            p.append(i[0])
            r.append(res1)
           # myr.append(res2)
            print(test)
            test=test+1
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
            res1 = self.requestGET(url, i[0])
            res2 = self.requestGET(url, i[1])
            p.append(i[0])
            r.append(res1)
            myr.append(res2)
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
    x.readcsv(dir+file)
    f = x.openfile()
    x.readadcode(adcode)
    splist1=x.splist(x.datas,k)


    e1 = time.time()
    thread_list = []  # 线程存放列表
    for i in range(k):
        t = threading.Thread(target=x.geo, args=(splist1[i],url))
        t.setDaemon(True)
        thread_list.append(t)

    for t in thread_list:
        t.start()


    for t in thread_list:
        t.join()

    e2 = time.time()
    print ("并行执行时间：", e2 - e1)

    x.report(f, url, p, r,myr)





