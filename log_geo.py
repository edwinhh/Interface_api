import os
import time
import re
import json
dir="e:/项目/地理编码/数据/cx省市区调整/"
dir1="e:/project/Interface_api-master/report"
file="node-geo-old-out-9.log"
old="e:/project/Interface_api-master/report/geo_new1.txt"
new="e:/project/Interface_api-master/report/geo_old1.txt"

# file1="node-geo2018-05-03-14-46-50.txt"
# errfile="e:/project/Interface_api-master/report/geo_threadingURL_error_2018-05-03-14_38_14.txt"
# filediff="diff.txt"

def log(file):
    sum=0
    total=0
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    result='node-geo'+now+'.txt'
    p=open(dir+result,'w+')
    p.write("#address,adcode")
    p.write('\n')
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if "query_type" in line:
                total+=1
                r = re.findall("address:\S+,",line)
                v = re.findall("adcode:\S+,user_id", line)
                v1=v[0].split(',')[0]
                address1=r[0].split(':')[1]
                
                address = address1.split(',')[0]
                if len(v1):
                    adcode=v1.split(':')[1]
                else:
                    adcode=""
                p.write(str(address))
                p.write(',')
                p.write(str(adcode))
                p.write('\n')
                # sum+=1

def err(old,new):
    reqnew=[]
    resnew=[]
    resold=[]
    node={}
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    diff = "e:/project/Interface_api-master/report/"+"diff_"+now+".txt"
    p = open(diff, 'w',encoding='utf-8')
    # p.write("#address,node_adcode")
    # p.write("\n")
    with open(old,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if '"status"' in line:
                # r = line.split("?")[1].split("&")[0].split("=")[1]
                resnew.append(line)
            if "http://" in line:
                reqnew.append(line)

    with open(new, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if '"status"' in line:
                # r = line.split("?")[1].split("&")[0].split("=")[1]
                resold.append(line)
    for i in range(min(len(resnew),len(resold))):
        if json.loads(resnew[i])["status"]==1 and json.loads(resold[i])["status"]==0:
            p.write(reqnew[i])
            p.write('\n')

    
    
        
    # for i in err:
    #     k=i.strip().replace(" ","")
    #     with open(filenode, 'r', encoding='utf-8') as f:
    #         for line in f.readlines():
    #             if len(line) == 1 or line.startswith('#'):
    #                 continue
    #             address=line.split(",")[0]
    #             if address == k:
    #                 node[k]=address

    # for k,v in node.items():
    #     p.write(k)
    #     p.write(",")
    #     p.write(v)
    #     p.write("\n")
    # print (len(node))
    # print (len(err))

        
                
                # address1=r[0].split('=')[1]
                # print (r[0])
                #address = address1.split(',')[0]
            

log(dir+file)
#err(old,new)
