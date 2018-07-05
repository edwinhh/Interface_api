# -*- coding: utf-8 -*-
#python3
import os
import time
import re
import sys


file='e:/project/Interface_api-master/201801312_utf8.txt'

def log(file):
    sum=0
    total=0
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    result='result'+now+'.txt'
    p=open(result,'w+',encoding='utf-8')
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if "LOG_SEARCH" in line:
                r1 = re.findall("keywords:\S+",line)
                r2 = re.findall("city:\S+", line)
                if r1 :
                    q=r1[0].split(':')[1]
                    if r2:
                        city=r2[0].split(':')[1]
                    else:
                        city=""
                    print(q)
                    #print("\t")
                    print(city)
                    print('\n')
                    p.write(q)
                    p.write(",")
                    p.write(city)
                    p.write('\n')

            else:
                continue
        p.close()


log(file)
