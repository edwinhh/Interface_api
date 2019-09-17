import os
import time
import re
import json
dir="e:/项目/地理编码/数据/加密/"
dir3="e:/项目/地理编码/数据/temp/system/"
dir1="e:/project/Interface_api-master/testlog/"
dir2="d:/stdout/"
#file="e:/项目/地理编码/数据/包含网点的测试地址数据.csv"
# old="e:/project/Interface_api-master/report/geo_new1.txt"
# new="e:/project/Interface_api-master/report/geo_old1.txt"
file="e:/项目/地理编码/数据/temp/system.log"
file2="e:/项目/输入提示/c++/待验证.txt"
file1='d:/stdout/xae'

# file1="node-geo2018-05-03-14-46-50.txt"
# errfile="e:/project/Interface_api-master/report/geo_threadingURL_error_2018-05-03-14_38_14.txt"
# filediff="diff.txt"
filelist=[]

def geo_file(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            filelist.append(os.path.join(root, file))
            
def log(file):
    sum=0
    total=0
    r1=''
    v1=''
    c2=''
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    filename=os.path.basename(file)
    result='加密'+filename+now+'.txt'
    p=open(dir+result,'w+',encoding='utf-8')
    p.write("#原地址,  加密地址,  city")
    p.write('\n')
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if "加密前地址" in line:
                print (line)
                r = re.findall("加密前地址：\S+",line)
                if len(r):
                    r1 = r[0].split('：')[1]
                
            if "加密后地址" in line:
                print (line)
                total += 1
                v = re.findall("加密后地址：\S+", line)
                if len(v):
                    v0 = v[0].split('：')[1]
                    #print ('v0=',v0)
                    #v1=str(v0).strip('\00H')
                    v1 = str(v0).strip()
                    print ('v1=',v1)
            if "city" in line:
                c = re.findall("city:\S+", line)
                if len(c):
                    c1 = c[0].split(':')[1]
                    if ',' in c1:
                        c2=c1.split(',')[0]
                    else:
                        c2=c1
                else:
                    c2=''
                # print (r1)

                p.write(str(r1))
                p.write(',')
                p.write(v1)
                p.write(',')
                p.write(str(c2))
                p.write('\n')
                sum+=1
    p.close()


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

def readcsv(file):
    temps=[]
    p=open("网点.txt", 'w+',encoding='utf-8')
    with open(file, 'r', encoding='utf-8')as f:
        for line in f.readlines():
            if len(line) == 1 or line.startswith('#'):
                continue
            temp = line.strip().split(",")
            ll1=str(temp[5]).strip('"')
            ll2 = str(temp[3]).strip('"')
            
            ll=ll1+','+ll2
            temps.append(ll)
            
    for i in temps:
        p.write(str(i))
        p.write('\n')
    p.close()
 
def copy1(file):
    filename = os.path.basename(file)
    print (dir + filename)
    p = open(dir3 + "new2"+filename, 'w', encoding='utf-8')
    with open(file, 'r', encoding='utf-8') as f:
        
        for line in f.readlines():
            if len(line) == 1 or line.startswith('#'):
                continue
            else:
                line1=line.split(",")
                p.write(line1[5])
                p.write(',')
                p.write(line1[7].strip())
                # p.write(',')
                # p.write(line1[2])
                p.write('\n')
            p.close

def geo_system(filelist):
    sum=0
    total=0
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    result = 'result_geo' + now + '.txt'
    p = open(dir3 + result, 'a+', encoding='utf-8')
    for file in filelist:
        p.write(file)
        p.write('\n')
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if '"time":' in line:
                    sum+=1
                    r1 = re.findall('"time":\S+,', line)
                    if (len(r1)):
                        v = r1[0].split(',')
                        i = v[0].split(':')
                        if int(i[1]) > 600:

                            total+=1
                            r2 = re.findall('"url":"\S+",', line)
                            u1=r2[0].split(',')
                            u=u1[0].split('":"')
                            
                            s1= re.findall('"sn":"\S+",', line)
                            s=s1[0].split(',')
                      
                            a1=re.findall('"address":"\S+",', line)
                            a=[]
                            if len(a1):
                                a=a1[0].split(',')
                                
                            c1=re.findall('"city":"\S+",', line)
                            c=[]
                            if len(c1):
                                c=c1[0].split(',')
                           
                            p.write('\n')
                            p.write(s[0])
                            p.write('\n')
                            p.write(u[1][0:-1])
                            p.write('\n')
                            if len(a):
                                p.write(a[0])
                            if len(c):
                                p.write(c[0])
    
                            p.write('\n')
                            p.write(v[0])
                            p.write('\n\n')
        
    
                            sum += 1
        
                    else:
                        continue
        print('sum=%d' % (sum))
            # print('per=%f%%' % (sum / total * 100))
    p.write('sum=')
    p.write(str(sum))
    p.write('\n')
    p.write('total=')
    p.write(str(total))
            # p.write('\n')
            # p.write('per=')
            # p.write(str(sum / total * 100))
            # p.write('%')
    p.close()

geo_file(dir3)
geo_system(filelist)

    
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

def readcsv1(file):
    num = 0
    with open(file, 'r', encoding='utf_8')as f:
        for line in f.readlines():
            if len(line) == 1 or line.startswith('#'):
                continue
            num =num+1
            
            temp = line.strip().split("+")
            if len(temp)!=3:
                print (num,len(temp))
                

#log(file1)
#ak(dir1)
# geo_file(dir2)
# for fo in filelist:
#     log(fo)
#copy1(file)
# readcsv1(file2)
#err(old,new)
