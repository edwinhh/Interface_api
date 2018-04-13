import os
import time
import re

file='e:/project/Interface_api-master/geocoder-2018-03-29.log'

def log(file):
    sum=0
    total=0
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    result='result_geo'+now+'.txt'
    p=open(result,'w+')
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if "query_type" in line:
                total+=1
                r = re.findall("address:\S+",line)
                v = re.findall("adcode:\S+", line)
                address=r[0].split(':')[1]
                if len(v):
                    adcode=v[0].split(':')[1]
                else:
                    adcode=""
                print(address,adcode)
                p.write(str(address))
                p.write(',')
                p.write(str(adcode))
                p.write('\n')
                # sum+=1



log(file)
