import os
import time
import re

file1='e:/项目/IPS/地址纠正服务/440300_test.csv'
file2='e:/项目/IPS/地址纠正服务/110000_test - 副本.csv'
log_tipcor='d:/user/01371178/桌面\log/system.log'
dir='e:/项目/IPS/地址纠正服务/'
filelist=[]
def log(file):
    sum=0
    total=0
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    result='result_cost'+now+'.txt'
    p=open(dir+result,'a+',encoding='utf-8')
    with open(log_tipcor,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if "time" in line:
                total+=1
                r = re.findall("time:\S+,",line)
                print(r)
                v=r[0].split(',')
                i=v[0].split(':')
                if int(i[1])>1000 :
                    print(line)
                    p.write(line)
                    p.write('\n')
                    sum+=1

            else:
                continue
        print('sum=%d' %(sum))
        print('per=%f%%' % (sum/total*100))
        p.write('sum=')
        p.write(str(sum))
        p.write('\n')
        p.write('per=')
        p.write(str(sum/total*100))
        p.write('%')
        p.close()

def tipcor(file):
    sum=0
    total=0
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    result='result_cost'+now+'.txt'
    p=open(dir+result,'a+',encoding='utf-8')
    with open(log_tipcor,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if "time" in line:
                total+=1
                r = re.findall('"time":\S+,"data"',line)
                #print(r)
                
                t=r[0].split(',')[0]
                v=t.split(':')[1]
                print(v)
                if int(v)>2500:
                    p.write(line)
                    p.write('\n')
                else:
                    continue
        p.close()
        #         i=v[0].split(':')
        #         if int(i[1])>1000 :
        #             print(line)
        #             p.write(line)
        # #             p.write('\n')
        # #             sum+=1
		#
        #     else:
        #         continue
        # print('sum=%d' %(sum))
        # print('per=%f%%' % (sum/total*100))
        # p.write('sum=')
        # p.write(str(sum))
        # p.write('\n')
        # p.write('per=')
        # p.write(str(sum/total*100))
        # p.write('%')
        # p.close()

def log_2(file1,file2):
    sum=0
    total=0
    p=open(file2,'a+',encoding='utf-8')
    with open(file1,'r',encoding='utf-8') as f:
        for line in f.readlines():
            adcode=line.split(',')[0].strip()
            adress= line.split(',')[1].strip()
            t=adress+","+adcode
            p.write(t)
            p.write("\n")
    p.close()
        
    

        
def tip(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            filelist.append(os.path.join(root, file))
    
    sum = 0
    total = 0
    tip_q = []
    tip_c=[]
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    result = 'tip' + '.txt'
    print (dir+result)
    p = open(dir+result, 'a', encoding='utf-8')
    p.write("#q,city")
    p.write('\n')
    for fo in filelist:
        with open(fo, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if "opt:my_tip_tcp" in line:
                    total += 1
                    q = re.findall("name:\S+,", line)
                    c = re.findall("city:\S+,", line)
                    if q:
                        q1 = q[0].split(':')[1].split(',')[0]
                    else:
                        q1=""
                    if c:
                        c1 = c[0].split(':')[1].split(',')[0]
                    else:
                        c1=""
                    tip_q.append(q1)
                    tip_c.append(c1)
                        # print ("q:",q1)
                        # print ("c:",c1)
    #         ak = list(set(ak))

    # for i in range(len(tip_c)):
    #     print (tip_q[i])
    #     print (tip_c[i])
    for i in range(len(tip_q)):
        p.write(tip_q[i])
        p.write(',')
        p.write(tip_c[i])
        p.write('\n')
        print (i)
#tip(dir)
#log_2(file1,file2)
tipcor(log_tipcor)
