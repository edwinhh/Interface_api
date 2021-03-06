#-*- coding: UTF-8 -*-
'''
Created on 2017年3月24日

@author: 01367593
'''
import gevent

import gevent.monkey

gevent.monkey.patch_all()

from gevent import pool

import os
import time
import requests
import json
#import  chardet

def to_str(bytes_or_str):
        if isinstance(bytes_or_str, str):
            return bytes_or_str.decode('utf-8')
        return bytes_or_str

class InterfaceChk(object):
    '''
    classdocs
    '''


    def __init__(self, u):
        '''
        Constructor
        '''
        self.u = u
        pass

    def GetTmplate(self,tempPath = 'conf/Sample.csv'):
        self.sampleList = []
        sampleList = open(tempPath).readlines()
        for ii in sampleList:
            keylist = ii.strip('\r\n').split(',')
            if(keylist[1] == 'R'):
                self.address= keylist[0].split("|")
            elif(keylist[1] == 'B'):
                self.city = keylist[0].split("|")
            elif(keylist[1] == 'A'):
                self.append = keylist[0].split("|")
        
    def GetConf(self, keyWdsPath='conf/keywordSample.csv',opt=''):
        print('start: '+keyWdsPath)
        self.keyWdsPath = keyWdsPath
        self.Cnt = 0
        self.keyWds = []
        x = open(keyWdsPath).readlines()
        y = x[0].strip().split(',')

        #2018-5-23 19:40:54 增加对模版的匹配
        bAddreeExist = False
        bCity        = False


        if(len(set(y).intersection(set(self.address) ) ) == 1):
            self.address = list(set(y).intersection(set(self.address)))[0]
            self.addr_inex = y.index(self.address)
            bAddreeExist = True


        int_city = set(y).intersection(set(self.city))
        if(len(set(y).intersection(set(self.city))) >= 1):
            self.city = list(set(y).intersection(set(self.city)))[0]
            self.city_inex = y.index(self.city)
            bCity = True

        if( not (bCity and bAddreeExist)):
            print("City and addreess is not exist ,please check the data file head")
            return -1

        self.append_out = {}
        if(len(self.append) > 0):
            data_append = set(y).intersection(set(self.append))
            for aa in data_append:
                pos = y.index(aa)
                self.append_out.update({aa:pos})


        for l in x[1:]:
            #解决地址中带有"" 2018-8-31 19:29:49 且地址为首行
            if (l[self.addr_inex].find("\"") != -1):
                self.keyWds.append({self.address: l[self.addr_inex], self.city: l[self.city_inex].strip("\r\n"),'ak': '你的ak', 'opt': opt})
                continue

            m = l.strip().split(',')
            try:
                if(len(self.append_out) == 0):
                    self.keyWds.append({self.address:m[self.addr_inex],self.city:m[self.city_inex].strip(),'ak':'你的ak','opt':opt})
                elif(len(self.append_out) > 0):
                    dict_para = {}
                    for kk,vv in list(self.append_out.items()):
                        dict_para[kk] = m[vv]

                    dict_para[self.city]    = m[self.city_inex]
                    dict_para[self.address] = m[self.addr_inex]
                    dict_para['ak'] = 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'
                    dict_para['opt'] = opt
                    for kk, vv in list(self.append_out.items()):
                        dict_para[kk] = m[vv]
                    self.keyWds.append(dict_para)
            except Exception as e:
                print(e)




        
    def GetResults(self, opt='', cnt = 0):
        if cnt==0:
            resultsF = open('result/HITgeo_'+opt+'_'+os.path.split(self.keyWdsPath)[-1],'w')
        else:
            resultsF = open('result/HITgeo_'+opt+'_'+str(cnt)+'_'+os.path.split(self.keyWdsPath)[-1],'w')

        if(len(self.append_out) == 0):
            resultsF.write(('norm_address,city,status,src,match_level,xcoord,ycoord,src_address,regcode,adcode,type,precision,query_adcode,query_address,err,msg\n').encode('gb18030'))
        else:
            resultsF.write(('id,norm_address,city,status,src,match_level,xcoord,ycoord,src_address,regcode,adcode,type,precision,query_adcode,query_address,err,msg\n').encode(
                'gb18030'))

        p = pool.Pool(20)
        hitFunc = self.HitGeo
        if cnt==0:
            results = p.map(hitFunc,self.keyWds)
        else:
            results = p.map(hitFunc,self.keyWds[:cnt])
        for i in range(len(results)):
            try:
                h = results[i]

                x = []
                for k, v in list(self.append_out.items()):
                    x.append(h.get(k, "").encode("utf-8"))

                for fld in  ["norm_address", "city", 'status','src','match_level','xcoord','ycoord','src_address','regcode','adcode','type','precision', "query_adcode", "query_address"]:
                    if fld  == "norm_address":
                        fld = "address"
                    if fld.startswith("query_"):
                        if "query" not in h:
                            x.append("")
                        else:
                            x.append(h["query"].get(fld[len("query_"):], ""))
                        continue

                    if(fld in h):
                        if(not isinstance(h[fld],str)):
                            x.append((str(h[fld])).encode('utf-8'))
                        else:
                            x.append(to_str(h[fld]))
                    else:
                        x.append('')

                if(h['status'] == '1'):
                    x.append(h['msg'])
                    x.append(str(h['err']))
                else:
                    x.append('')
                    x.append('')

                strappend = ','.join(x)
                strres = strappend.encode("utf-8") + "\n"
                #2018-5-25 11:57:00
                # strid = h["id"]


                # strres = ""
                # if(len(strid) > 0):
                #     strres = strid + self.keyWds[i][self.address] + "," + self.keyWds[i][self.city] + "," + strappend.encode('utf-8') + "\n"
                # else:
                #     strres =  self.keyWds[i][self.address] + "," + self.keyWds[i][self.city] + "," + strappend.encode('utf-8') + "\n"
                resultsF.write(strres)
            except Exception as e:
                print(e)
 
    def HitGeo(self, paras):
        if not self.Cnt%1000:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'  '+str(self.Cnt))
        self.Cnt+=1
        # 输入文件city不为空
        parasGeo = {'city':paras[self.city],'address':paras[self.address],'opt':paras['opt'],'ak':paras['ak']}
        # 输入文件city为空
        # parasGeo = {'address':paras[self.address],'opt':paras['opt'],'ak':paras['ak']}
        input = {"address": paras["address"], "city": paras["city"]}
        for k, v in list(self.append_out.items()):
            input[k] = paras[k]
        #print parasGeo
        for _ in range(5):
            try:
                r = requests.get(self.u,parasGeo)
                # print(r.url)
                assert r.status_code==200
                c = json.loads(r.content)
                #print c
                if c['status']== '1':
                    input["status"] = -2
                    return input
                result = c['result']
                result.update({'status':str(c['status'])})
                result.update(input)
                
                return result
            except Exception as e:
                pass
        input["status"] = -1
        return input

    
if __name__ == '__main__':
    u = 'http://gis-int.intsit.sfdc.com.cn:1080/geo/api?'
    srcPath = 'SIT'
    opt = 'sf30'
    ic = InterfaceChk(u)
    for x in os.listdir(srcPath):
        ic.GetTmplate()
        ic.GetConf(os.path.join(srcPath,x),opt = opt)
        ic.GetResults(opt = opt)
