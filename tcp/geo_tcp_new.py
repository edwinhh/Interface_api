#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket,sys, struct, codecs,os, time, threading
from xml.parsers.expat import *
import xml.etree.cElementTree as ET
import time
#from geo_in import *
import csv
#2018-04-17 修改：若输入数据传入adcode参数，则根据adcode判断是否为直辖市、直管县，做出相应的处理
#2018-04-28 修改：程序执行命令可增加no_citycode参数，仅当附带该参数时，输入数据读取adcode/citycode
#2018-07-03 修改：支门牌视为高精、yy分为yy1、yy2
#本脚本通过一个端口完成多源地理编码

server_hosts = [("RSS-REGO-RDP.SFDC.COM.CN", 20180)]#生产环境
server_hosts = [("10.202.43.221",20184)]#测试环境（正式）
# server_hosts = [("10.202.43.221",10184)]#测试环境（测试）


#本地白名单路径
# whiteListPath = '/data/1/tmp/address/whiteList.csv'#生产环境
whiteListPath = 'whiteList.csv'#测试环境

#本地白名单字典
whiteListDic = {}

# config:address fldno(0 begin)
#在此指定地址所在列
m_FldNo_Address = 0
m_FldNo_adcode = None
m_ThreanCount = 8

m_DefaultCity = ""
adcodeDic = {}

sf_count = 0
navInfo_count = 0
autoNavi_count = 0
autoNavi_Supplement_count = 0
baidu_Supplement_count = 0
supplement_count = 0

timeStart = None

closedThread = 0#计数器：完成编码任务的接口数

geo_map=({"GL_COUNTRY":("国家",0),
				"GL_PROVINCE":("省",1),
				"GL_CITY":("城市",2),
				"GL_COUNTY":("区县",3),
				"GL_DEV_ZONE":("开发区",5),
				"GL_TOWN":("乡镇/街道",4),
				"GL_VILLAGE":("村/社区",5),
				"GL_GROUP":("组/队",5),
				"GL_BZONE":("商圈",5),
				"GL_LINE":("道路",6),
				"GL_ROAD":("道路",6),
				"GL_ROAD_BRANCH":("道路",6),
				"GL_STREETNO":("门牌",8),
				"GL_STREETNO_SUB":("支门牌",8),
				"GL_POI":("POI",9),
				"GL_ROADINTER":("道路交叉口",9),
				"GL_BUILDINGNO":("楼栋号",10),
				"GL_BUILDING_UNIT"	:("单元房间",11),
				"GL_BUILDING_FLOOR" :("单元房间",11),
				"GL_BUILDING_ROOM"  :("单元房间",11),
				"GL_OTHER":("other",-1),
				"GL_INTER":("门牌插值",-1),
				"GL_NEARBY":("附近",-1)}
	)

geo_precision_level_set = set(["GL_BUILDINGNO","GL_POI","GL_STREETNO","GL_STREETNO_SUB","GL_ROAD_BRANCH"])
geo_precision_filter_set = set(["1","2","8"])

def GetCurTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def xml2Text(obj):
    return obj.text + str(obj.attrib)

def getInfoFromXML(input, line):
    global geo_map,geo_precision_level_set,geo_precision_filter_set
    match_level = ''
    adcode = ''
    x = 0
    y = 0
    src_level = ''
    filter = ''
    match_type = ''
    precision = 0
    validAddress = '0'
    data_Src = '0'
    base_id = ''
    group_id = ''
    source = ''

    ret = (match_level,adcode,x,y,src_level,filter,match_type,precision,validAddress,data_Src,base_id,group_id,source)

    try:
        try:
            tree = ET.fromstring(input.decode('gb18030').encode('utf8').replace('GBK', 'utf-8'))
        except Exception:
            input_ = input.replace('\xb3</','</')
            tree = ET.fromstring(input_.decode('gb18030').encode('utf8').replace('GBK', 'utf-8'))
        # tree = ET.fromstring(input.decode('gb18030').encode('utf8').replace('GBK', 'utf-8'))
        ss = ET.tostring(tree, 'utf8')
        if tree.find("count").text=="0":
            pass
            # return ret
        else:
            listResult = tree.find("list")
            source = tree.find('source').text
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
                    # (match_type,match_level) = get_geolevel(src_level)
                    # precision = get_geoprecision(src_level,filter)
                    (match_type,match_level) = ("",-1)
                    if geo_map.has_key(src_level):
                        (match_type,match_level) = geo_map[src_level]
                    precision = 0
                    if src_level in geo_precision_level_set and filter in geo_precision_filter_set :
                        precision = 2
                    data_Src = xml_poi.find('dataSrc').text
                    adcode = xml_poi.find('adcode').text
                    x = float(xml_poi.find('x').text)
                    y = float(xml_poi.find('y').text)
                    base_id = xml_poi.find('id').text
                    if xml_poi.find('group') != None:
                        group_id = xml_poi.find('group').text


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

        return (match_level , adcode , x , y , src_level , filter , match_type , precision , validAddress , data_Src,base_id,group_id,source)

    except Exception as e:
        print 'getInfoFromXML Error: %s' % e
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

def connect_multi(addr_qurey,adcode_qurey, line, sock_list):
    global g_queryResults, g_mutex, g_count, g_total_count,g_match_count,g_whiteList_count, g_output_file
    global sf_count,navInfo_count,autoNavi_count,autoNavi_Supplement_count,baidu_Supplement_count,supplement_count
    global whiteListDic
    result = None
    # i = 0
    query = genquery(addr_qurey,adcode_qurey)
    for sock in sock_list:
        # i += 1
        result = connect_one(query, line, sock)
        if not result:
            return False

        # if result[7] == 2:
        #     # g_match_count += 1
        #     break

    if g_mutex.acquire(1):
        try:
            portNum = 0
            match_level, adcode,  queryXResult, queryYResult, queryLevelResult, filter, match_type, precision, validAddress, dataSrc,base_id ,group_id,source = result
            if source == 'sf':
                sf_count += 1
                portNum = 1
            elif source == 'sw':
                navInfo_count += 1
                portNum = 2
            elif source == 'gf' or source == '':
                autoNavi_count += 1
                portNum = 3
            elif 'yy' in source:
                supplement_count += 1
                portNum = 6
            else:
                print 'new source:%s'%source

            # #白名单
            # if addr_qurey.decode('gb18030').encode('utf-8') in whiteListDic.keys():
            #     (queryXResult, queryYResult) = whiteListDic[addr_qurey.decode('gb18030').encode('utf-8')]
            #     portNum = 7
            #     precision = 2
            #     g_whiteList_count += 1

            if precision == 2:
                g_match_count += 1
            try:
                geo_src = '%d%03d' % (portNum,int(dataSrc))
            except:
                geo_src = '%d%900' % (portNum)

            queryResult = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (line,str(queryXResult), str(queryYResult), queryLevelResult,precision,adcode,match_level,match_type,validAddress,geo_src,dataSrc,base_id,group_id )
            g_queryResults += queryResult
            g_count += 1

            if g_count % 10000 == 0:
                fs = open(g_output_file, "a+")
                fs.write(g_queryResults)
                fs.close()
                g_queryResults = ""

                if g_count % 10000 == 0:
                    print "%s\tcount=%d\tyy=%d\tsf=%d\tsw=%d\tgd=%d\ttime remaining: %d s" % (GetCurTime(), g_count,supplement_count,sf_count,navInfo_count,autoNavi_count,(g_total_count - g_count) * (time.time() - timeStart) / g_count)

        except Exception,e:
            print 'connetMulti Error: %s' % e
            #print 'error at line: %s' % line.decode('utf-8')
        g_mutex.release()

    return True


def genquery(keyword, adcode=""):
    # query='user_id:ronghe\nfilter_uprecision:2\nquery_type:GEOCODE\naddress:%s\nadcode:%s\n'% (keyword, adcode)
    # query='user_id:ronghe\nret_splitinfo:2\nfilter_uprecision:2\nquery_type:GEOCODE\naddress:%s'%(keyword)#不带adcode
    query='user_id:ronghe\nret_splitinfo:2\nfilter_uprecision:2\nquery_type:GEOCODE\naddress:%s\nadcode:%s\n'%(keyword, adcode)#带adcode
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

#生成citycode adcode对应字典
def loadadcodeDic():
    # global adcodeDic
    title = True
    with open('./city_code.csv','r') as f:
        for line in f:
            if title:
                title = False
                continue
            items = line.strip('\r\n ').split(',')
            citycode = items[3]
            adcode = items[1]
            if citycode in adcodeDic.keys():
                # adcodeDic[citycode] = '%s0000'%adcode[:2]
                adcodeDic[citycode] = ''
            else:
                adcodeDic[citycode] = adcode
    #saveAsTXT(dic):
    f = open('city_code.txt','wb')
    f.write(str(adcodeDic))
    f.close()
    return 0




def loadAdcodeDicFromTXT(path = 'city_code.txt'):
    global adcodeDic
    f = open(path,'r')
    a = f.read()
    adcodeDic = eval(a)
    f.close()
    print '%s\tAdcodeDic is Ready, lenth = %d'%(GetCurTime(),len(adcodeDic.keys()))
    return 0

#判断参数是否是adcode，如果是citycode则转为adcode
def getAdcode(str):
    rtn = ''
    if str.isdigit():
        if len(str) == 4 or len(str) == 3:
            try:
                rtn = adcodeDic[str]
            except:
                rtn = ''

        elif len(str) == 6:
            # 中央直辖市，输出省级行政区划代码
            if str[0:2] in ['11','12','31','50']:
                rtn = str[:2] + '0000'
            # 省直辖县级行政单位，输出空
            elif str[2:4] == '90':
                rtn = ''
            # 其他行政区，输出地市级行政区划代码
            else:
                rtn = str[:4]+'00'

    return rtn
    # if len(str) == 6:
    #     return str
    # if len(str) == 4 or len(str) == 3:
    #     str = adcodeDic[str]
    #     return str
    # return ''

#剔除掉异常字符(剔除掉TTT线程无法读取的字符)
def invalidCharFilter2(line):
    invalidChar3 = ['①','☆','ㄏ','．','／','②','④','●','━','─','＿','ㄧ','「','」','の','℃','?']#'gb18030' codec can't decode
    for invalidChar in invalidChar3:
        if invalidChar in line:
            line = line.replace(invalidChar,' ')

    return line

#下载白名单至本地
def downloadWhiteListToLocal():
    global whiteListPath
    #command = 'hive --incremental=true --outputformat=csv2 --silent=true -e \"use dm_gis;select * from addr_mining_exceptiondata_whitelist_20180206\" > '
    command = 'hive -S -e "set hive.cli.print.header=true;select * from dm_gis.addr_mining_exceptiondata_whitelist_20180206" > '
    command += whiteListPath
    command += ' 2>dump.txt'
    os.system(command)
    print '%s\twhite list downloaded'%(GetCurTime())
    return 0
#加载本地白名单
def loadWhiteList(path):
    global whiteListPath,whiteListDic
    if path == '':
        path = whiteListPath

    whiteListDic = {}
    addr_field_No = 0
    x_field_No = 0
    y_filed_No = 0

    with open(path,'r') as f:
        title = True
        lines = csv.reader(f,delimiter=',')
        for line in lines:
            if title:
                title = False
                for i in range(len(line)):
                    if line[i].endswith('.address'):
                        addr_field_No = i
                    if line[i].endswith('.lng'):
                        x_field_No = i
                    if line[i].endswith('.lat'):
                        y_filed_No = i
                continue
            addr = line[addr_field_No]
            if addr not in whiteListDic.keys():
                whiteListDic[addr] = (line[x_field_No],line[y_filed_No])
            # else:
            #     pass

    print '%s\twhitelist loaded'%(GetCurTime())
    # print addr
    # f = open(whiteListPath.replace('.csv','.txt',-1),'wb')
    # f.write(str(whiteListDic))
    # f.close()
    return 0

def loadWhiteListFromTXT():
    global whiteListPath,whiteListDic
    f = open(whiteListPath.replace('.csv','.txt',-1),'r')
    a = f.read()
    whiteListDic = eval(a)
    f.close()
    print '%s\twhitelist loaded from TXT'%(GetCurTime())
    return 0

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
        # lines = csv.reader(self.lines)
        # for line in lines:#利用csv模块读取文件
        while i < len(self.lines):
            lineStr = self.lines[i]
            #采用UTF8带BOM格式的编码，则首行可能出现异常字符
            #如果line中有异常字符，打印时会出现异常，下面try-except块将删除这些异常字符
            address = ''
            adcode = ''
            try:
                terms = lineStr.strip('\r\n ').split(',')
                address = terms[m_FldNo_Address]
                address = address.decode('utf-8').encode('gb18030')
                if m_FldNo_adcode != None:
                    adcode = getAdcode(terms[m_FldNo_adcode])
                else:
                    adcode = ''
                # address = line[m_FldNo_Address]
                # address = address.decode('utf-8').encode('gb18030')
                # adcode = getAdcode(line[m_FldNo_adcode])

            except:
                pass

            success = False
            try:
                #address = invalidCharFilter(address)#暂时不剔除异常字符
                # success = connect_multi(genquery(address,m_DefaultCity), line, self.socks)
                success = connect_multi(address, adcode, lineStr, self.socks)
                if not success:
                    print 'trying re-connect...'
                    uninit_socks(self.socks)
                    self.socks = init_socks(m_DefaultCity)
                    # success = connect_multi(genquery(address,m_DefaultCity), line, self.socks)
                    success = connect_multi(address, adcode, lineStr, self.socks)


            except Exception,e:
                print 'TTT:%s error: %s' % (self.name,e)
                #print 'error at line[%d]: %s' % (i,line.decode('utf-8'))
                try:
                    uninit_socks(self.socks)
                    self.socks = init_socks(m_DefaultCity)
                    # connect_multi(genquery(address,m_DefaultCity), line, self.socks)
                    # success = connect_multi(genquery(address,adcode), line, self.socks)
                except:
                    print 're-connecting failed'
                    pass
            i += 1
        closedThread += 1
        print '%s\t%s has closed, which has processed %d lines' % (GetCurTime(),self.name,len(self.lines))

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
g_match_count = 0
g_whiteList_count = 0
g_output_file = "rtn_geo.csv"
if __name__=='__main__':
    # global timeStart
    print '%s\t[geo_tcp_domain.py]  start!\tversion = 20180531'%(GetCurTime())
    t1=time.time()
    timeStart = t1
    #暂不具备从大数据下载的条件
    #downloadWhiteListToLocal()
    #print '%s\t downloaded'%GetCurTime()
    # print '%s\tloading whiteList.csv'%(GetCurTime())
    #loadWhiteList(whiteListPath)
    # loadWhiteListFromTXT()
    # print '%s\twhitelist lenth = %d'%(GetCurTime(),len(whiteListDic.keys()))
    #loadadcodeDic()
    loadAdcodeDicFromTXT()
    if len(sys.argv) > 1:
        src_file = sys.argv[1]

        if len(sys.argv) > 2:
            g_output_file = sys.argv[2]

        else:
            g_output_file = './rtn_geo.csv'

        if len(sys.argv) > 3:
            if sys.argv[3] == 'no_citycode':
                print '%s\tSet m_FldNo_adcode as None and load whiteList from \'%s\''%(GetCurTime(),whiteListPath)
                m_FldNo_adcode = None
                loadWhiteList(whiteListPath)
                print '%s\twhitelist loaded. lenth = %d'%(GetCurTime(),len(whiteListDic.keys()))

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
        # fieldnames += ',SF_lon,SF_lat,SF_GL_level,SF_precision,SF_adcode,SF_src_level,SF_type,valid_flag,geo_src,data_src,baseID,groupID\n'
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
        print "%s\ttotal_count = %d" % (GetCurTime(), g_total_count)

        thread_no = m_ThreanCount
        threads = []
        ll = len(lines)/thread_no

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

        print "%s\tcount=%d\tyy=%d\tsf=%d\tsw=%d\tgf=%d" % (GetCurTime(), g_count,supplement_count,sf_count,navInfo_count,autoNavi_count)
        print "%s\twhiteList = %d\tmatched = %d\t match rate = %.2f %%"%(GetCurTime(),g_whiteList_count,g_match_count,float(g_match_count)/float(g_total_count)*100)
        print '%s\tused %ds.'%(GetCurTime(), t2-t1)
    else:
        print 'python geo_tcp_domain.py src_file dest_file ipIndex city'
