#!/usr/bin/python
# -*- coding:gbk -*-
import socket,sys, struct, codecs,os, time, threading
from xml.parsers.expat import *
import xml.etree.cElementTree as ET
import time
from DB.geo_in import *
#2017-11-15 新脚本
#本脚本将进行地理编码
#改动：应要求，加上对表头的支持；加上dataSrc字段的输出


#地理编码缺失库接口、顺丰接口、四维图新接口、高德地图接口   ("10.202.15.197", 20178),("10.202.15.159", 20175), ("10.202.15.197", 20177),("10.202.15.197", 20179)
#server_hosts = [("10.202.15.197", 20178),("10.202.15.159", 20175), ("10.202.15.197", 20177),("10.202.15.197", 20179)]
#server_hosts = [("10.202.15.197", 20178),("10.202.73.175", 8080), ("10.202.15.197", 20177),("10.202.15.197", 20179)]
#server_hosts = [("10.202.73.175", 8080)]
server_hosts = [("10.202.52.102", 20180),("10.202.52.102", 20175), ("10.202.52.102", 20177),("10.202.52.102", 20179)]



# config:address fldno(0 begin)
#在此指定地址所在列
m_FldNo_Address = 1

m_ThreanCount = 8

m_DefaultCity = ""
#SF上线城市列表（深圳4403 上海31 杭州3301 北京11）
# sf_citys=set(["11","31","3301","4403"])#这些城市可调用顺丰地图接口[0]

sf_count = 0
navInfo_count = 0
autoNavi_count = 0
autoNavi_Supplement_count = 0
baidu_Supplement_count = 0
supplement_count = 0

timeStart = None

closedThread = 0#计数器：完成编码任务的接口数

def GetCurTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def xml2Text(obj):
    return obj.text + str(obj.attrib)

def getInfoFromXML(input, line):
    # (match_level,adcode,x,y,src_level,filter,match_type,precision,validAddress,data_Src)
    ret = ("", "", 0, 0, "", "", "", 0, '0','0')

    xml_poi = None
    src_level = ""
    match_level = -1
    match_type = ""
    validAddress = '0'

    try:
        tree = ET.fromstring(input.decode('gb18030').encode('utf8').replace('GBK', 'utf-8'))
        ss = ET.tostring(tree, 'utf8')
        if tree.find("count").text=="0":
            return ret
        else:
            listResult = tree.find("list")
            if listResult.find("poi")!=None:
                min_filter = None
                for i in range(len(listResult)):
                    xml_poi = listResult[i]
                    filter = xml_poi.find('filter').text

                    if min_filter == None:
                        min_filter = filter
                    else:
                        if int(min_filter) <= int(filter):
                            continue
                        else:
                            min_filter = filter

                    src_level = xml_poi.find('level').text
                    (match_type,match_level) = get_geolevel(src_level)
                    precision = get_geoprecision(src_level,filter)
                    data_Src = xml_poi.find('dataSrc').text
                    adcode = xml_poi.find('adcode').text
                    x = float(xml_poi.find('x').text)
                    y = float(xml_poi.find('y').text)

                if tree.find("addrSplitInfo")!=None:
                    as_info = tree.find("addrSplitInfo")
                    valid = False

                    if precision == 2:#地理编码精度合格的地址均为有效地址
                        valid = True
                        validAddress = '1'

                    for i in range(len(as_info)):
                        if valid:
                            break
                        split = as_info[len(as_info)-1-i]
                        level = split.attrib['level']

                        if level in ['11','12','13','14']:
                            valid = True
                            validAddress = '1'
                            break

                return (match_level , adcode , x , y , src_level , filter , match_type , precision , validAddress , data_Src)
            else:
                return ret

    except Exception as e:
        #print 'getInfoFromXML Error: %s' % e
        #print line.decode('utf-8')
        return ret

def initsock(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        linger_struct=struct.pack('ii', 1, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, linger_struct)
        return sock
    except socket.error,e:
        print 'socket error: %s \t port = %d'%(e,port)
        pass

def init_socks(m_DefaultCity):
    global sf_citys,server_hosts
    host_list = server_hosts

    socks = []
    for host, port in host_list:
        sock = initsock(host, port)
        if sock:
            # print 'Initialization Success! port = %d'%port
            socks.append(sock)

    return socks


def uninit_socks(socks):
    # print 'preparing re-connect...'
    for sock in socks:
        if not sock:
            continue
        try:
            sock.close()
        except Exception, e:
            pass


def connect_one(query, line, sock):
    head=0xffffeeee
    cmdtype=0
    length = len(query)+4
    try:
        q = struct.pack('III%ds'%len(query),  head,  length, cmdtype, query)
        sock.send(q)
        header = sock.recv(4)
        length_body = sock.recv(4)
        length,  = struct.unpack('I',  length_body)
        result = ''
        remain = length
        while remain:
            t = sock.recv(remain)
            result += t
            remain -= len(t)
        
        ret=None
        try:
            ret = getInfoFromXML(result,line)
        except Exception as e:
            pass
        return ret
    except socket.error,e:
        print 'socket error: %s' % e
        #print 'error at line: %s' % line.decode('utf-8')

    return None

def connect_multi(query, line, sock_list):
    global g_queryResults, g_mutex, g_count, g_total_count, g_output_file
    global sf_count,navInfo_count,autoNavi_count,autoNavi_Supplement_count,baidu_Supplement_count,supplement_count
    result = None
    i = 0
    for sock in sock_list:
        i += 1
        result = connect_one(query, line, sock)
        if not result:
            return False

        if result[7] == 2:
            break

    if g_mutex.acquire(1):
        try:
            match_level, adcode,  queryXResult, queryYResult, queryLevelResult, filter, match_type, precision, validAddress, dataSrc = result
            #   添加请求来源信息，1代表20175/8080接口，2代表20177接口，3代表20179接口，6代表20178/20180接口
            port = sock.getpeername()[1] #获取端口号
            portNum = 0 #端口代码

            if port == 20175:
                sf_count += 1
                portNum = 1
            if port == 20177 or port == 20181:
                navInfo_count += 1
                portNum = 2
            if port == 20179:
                autoNavi_count += 1
                portNum = 3
            # if port == 4702:
            #     autoNavi_Supplement_count += 1
            #     portNum = 4
            # if port == 4701:
            #     baidu_Supplement_count += 1
            #     portNum = 5
            if port == 20178 or port == 20180:
                supplement_count += 1
                portNum = 6
            queryResult = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s\n" % (line,str(queryXResult), str(queryYResult), queryLevelResult,precision,adcode,match_level,match_type,validAddress,portNum,dataSrc )
            g_queryResults += queryResult
            g_count += 1

            if g_count % 1000 == 0:
                fs = open(g_output_file, "a+")
                fs.write(g_queryResults)
                fs.close()
                g_queryResults = ""

                if g_count % 1000 == 0:
                    print "%s\tcount=%d\tsf=%d\tnavInfo=%d\tautoNavi=%d\ttime remaining: %d s" % (GetCurTime(), g_count,sf_count,navInfo_count,autoNavi_count,(g_total_count - g_count) * (time.time() - timeStart) / g_count)

        except Exception,e:
            print 'connetMulti Error: %s' % e
            #print 'error at line: %s' % line.decode('utf-8')
        g_mutex.release()

    return True


def genquery(keyword, adcode=""):
    # query='user_id:ronghe\nfilter_uprecision:2\nquery_type:GEOCODE\naddress:%s\nadcode:%s\n'% (keyword, adcode)
    query='user_id:ronghe\nret_splitinfo:1\nfilter_uprecision:2\nquery_type:GEOCODE\naddress:%s'%(keyword)
    #query='user_id:ronghe\nret_splitinfo:2\nfilter_uprecision:2\nquery_type:GEOCODE\naddress:%s'%(keyword)
    return query

#剔除掉异常字符(剔除掉XML无法解析的字符)
def invalidCharFilter(line):
    invalidChar1 = ['&middot;','&mdash;','&nbsp;','&amp;','&quot;','＆middot;','＆mdash;']#HTML转义字符
    invalidChar2 = ['?','？','&','＆','，','','＜','＞','','']#其他异常字符
    for invalidChar in invalidChar1:
        if invalidChar in line:
            line = line.replace(invalidChar,'')

    for invalidChar in invalidChar2:
        if invalidChar in line:
            line = line.replace(invalidChar,'')

    return line

#剔除掉异常字符(剔除掉TTT线程无法读取的字符)
def invalidCharFilter2(line):
    invalidChar3 = ['①','☆','ㄏ','．','／','②','④','●','━','─','＿','ㄧ','「','」','の','℃','?']#'gb18030' codec can't decode
    for invalidChar in invalidChar3:
        if invalidChar in line:
            line = line.replace(invalidChar,' ')

    return line

class TTT(threading.Thread):
    def __init__(self, lines, socks):
        threading.Thread.__init__(self)
        self.lines = lines
        self.socks = socks

    def __del__(self):
        uninit_socks(self.socks)

    def run(self):
        global m_FldNo_Address,m_DefaultCity
        global closedThread
        global server_hosts
        i = 0
        while i < len(self.lines):
            line = self.lines[i]
            #采用UTF8带BOM格式的编码，则首行可能出现异常字符
            #如果line中有异常字符，打印时会出现异常，下面try-except块将删除这些异常字符
            address = ''
            try:
                terms = line.strip('\r\n ').split(',')
                address = terms[m_FldNo_Address]
                address = address.decode('utf-8').encode('gbk')
            except:
                pass

            success = False
            try:
                # address = invalidCharFilter(address)
                success = connect_multi(genquery(address,m_DefaultCity), line, self.socks)
                if not success:
                    print 'trying re-connect...'
                    uninit_socks(self.socks)
                    self.socks = init_socks(m_DefaultCity)
                    success = connect_multi(genquery(address,m_DefaultCity), line, self.socks)


            except Exception,e:
                print 'TTT:%s error: %s' % (self.name,e)
                #print 'error at line[%d]: %s' % (i,line.decode('utf-8'))
                try:
                    uninit_socks(self.socks)
                    self.socks = init_socks(m_DefaultCity)
                    # connect_multi(genquery(address,m_DefaultCity), line, self.socks)
                except:
                    print 're-connecting failed'
                    pass
            i += 1
        closedThread += 1
        print '%s has closed, which has processed %d lines' % (self.name,len(self.lines))

#added by Chris 2017.11.17
def get_field_index(fields):
    for i in range(0, len(fields)):
        field = fields[i]
        if field.lower() == 'norm_address':
            return i
    for i in range(0, len(fields)):
        field = fields[i]
        if field.lower() == 'address':
            return i
    return -1



g_queryResults = ""
g_mutex = threading.Lock()
g_count = 0
g_total_count = 0
g_output_file = "rtn_geo.csv"
if __name__=='__main__':
    global timeStart
    if len(sys.argv) > 1:
        src_file = sys.argv[1]

        if len(sys.argv) > 2:
            g_output_file = sys.argv[2]

        else:
            g_output_file = './rtn_geo.csv'

        m_DefaultCity = '0'

        f = open(src_file)
        lines = f.read().splitlines()
        f.close()

        # #大数据部门不需要处理标题行和添加表头
        # #处理标题行
        # header=[]
        # fs = open(g_output_file, "wb")
        # fieldnames = lines[0].strip('\r\n')
        # header = fieldnames.split(',')
        # fieldnames += ',SF_lon,SF_lat,SF_GL_level,SF_precision,SF_adcode,SF_src_level,SF_type,valid_flag,geo_src,data_src\n'
        # fs.write(fieldnames)
        # fs.close()
        # del lines[0]
        # #获取norm_address所在列的序号
        # # for i in len(fieldnames):
        # #     if fieldnames[i] == 'norm_address':
        # #         m_FldNo_Address = i
        #
        # #地址所在列: 2017.11.17 by Chris
        # numIndex = get_field_index(header)
        # if numIndex!=-1:
        #     m_FldNo_Address = numIndex


        g_total_count = len(lines)
        print "%s\ttotal_count=%d" % (GetCurTime(), g_total_count)

        thread_no = m_ThreanCount
        threads = []
        ll = len(lines)/thread_no
        t1=time.time()
        timeStart = t1
        for i in range(thread_no):
            if i < thread_no - 1:
                t = TTT(lines[ll*i:ll*(i+1)], init_socks(m_DefaultCity))
                t.start()
                threads.append(t)
            if i == thread_no - 1:
                t = TTT(lines[ll*i:], init_socks(m_DefaultCity))
                t.start()
                threads.append(t)

        for t in threads:
            t.join()
        t2=time.time()

        with open(g_output_file, "a+") as fp_w:
            fp_w.write(g_queryResults)
            fp_w.close()

        print "%s\tcount=%d\tsupplement=%d\tsf=%d\tnavInfo=%d\tautoNavi=%d" % (GetCurTime(), g_count,supplement_count,sf_count,navInfo_count,autoNavi_count)
        print '%s\tused %ds.'%(GetCurTime(), t2-t1)
    else:
        print 'python geo_tcp_domain.py src_file dest_file ipIndex city'
