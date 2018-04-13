import os
import time
import re
file='e:/project/Interface_api-master/pid_20175.txt'

def pid(file):
    sum = 0
    total = 0
    pid = []

    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    result='result'+now+'.txt'
    p=open(result,'w+',encoding='utf-8')
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():

            if "PID" in line:
                sum+=1
                continue
            if "进程退出了" in line:
                continue
            if "-"  in line:
                continue
            if not len(line.strip()):
                continue
            else:
                a = []
                a.append(line.strip().split("\t")[0])
                a.append(line.strip().split("\t")[1])
                a.append(line.strip().split("\t")[2])
                a.append(sum)
                pid.append(a)
        for i in pid:
            if int(i[0])>10090:
                print(i)




pid(file)

