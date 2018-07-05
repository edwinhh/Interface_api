import os
import time
import re

file='e:/project/Interface_api-master/20171128'
dir='e:/项目/输入提示/c++/log/'
filelist=[]
def log(file):
    sum=0
    total=0
    now=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    result='result_cost'+now+'.txt'
    p=open(dir+result,'a+',encoding='utf-8')
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
tip(dir)
