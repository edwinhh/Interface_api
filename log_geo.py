import os
import time
import re
import json
dir="e:/项目/地理编码/数据/cx省市区调整/"
dir1="e:/project/Interface_api-master/testlog/"
dir2="e:/project/Interface_api-master/"
file="node-geo-out-1__2018-05-24_16-23-25.log"
# old="e:/project/Interface_api-master/report/geo_new1.txt"
# new="e:/project/Interface_api-master/report/geo_old1.txt"

# file1="node-geo2018-05-03-14-46-50.txt"
# errfile="e:/project/Interface_api-master/report/geo_threadingURL_error_2018-05-03-14_38_14.txt"
# filediff="diff.txt"
filelist=[]
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


def ak(dir1):
    for root, dirs, files in os.walk(dir1):
        for file in files:
            filelist.append(os.path.join(root, file))
 
    sum = 0
    total = 0
    ak=[]
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    result = 'ak' + '.txt'
    p = open(dir + result, 'w+')
    p.write("#ak")
    p.write('\n')
    for fo in filelist:
        with open(fo, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if "url_s" in line:
                    total += 1
                    r = re.findall(",ak=\S+", line)

                    if r:
                        r1 = r[0].split(',')[1]
                        r2=r1.split('=')[1]
                        ak.append(r2)
            ak=list(set(ak))
    for i in ak:
        p.write(str(i))
        p.write('\n')




def err(old,new):
    reqnew=[]
    resnew=[]
    resold=[]
    node={}
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    diff = "e:/project/Interface_api-master/"+"ak_"+now+".txt"
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
            

#log(dir+file)
ak(dir1)
#err(old,new)
