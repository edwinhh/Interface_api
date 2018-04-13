import os
import time
import re

file='e:/project/Interface_api-master/xianggang.csv'

def log(file):
    sum=0
    total=0
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    result='result'+now+'.txt'
    p=open(result,'w+')
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            adress=line.split(",")[1]
            print(adress)
            p.write(adress)
            p.write('\n')
            sum+=1





log(file)
