import os
import time
import re

file='e:/project/Interface_api-master/20171128'

def log(file):
    sum=0
    total=0
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    result='result_cost'+now+'.txt'
    p=open(result,'w+')
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if "cost" in line:
                total+=1
                r = re.findall("cost:\S+,",line)
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


log(file)
