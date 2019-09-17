# coding:utf-8
import sys
import os
import socket
import struct
import time
import threading
import urllib2
import urllib
import json
import codecs


# 多线程类
class Cpreprocessor(threading.Thread):
    def __init__(self, lines, outfile):
        threading.Thread.__init__(self)
        self.lines = lines
        self.outfile = outfile
        self.queryResults = ""
        self.nCount = 0

    def run(self):
        global index_phone, index_mobile, index_address, index_citycode
        fw = open(self.outfile, "a+")

        for line in self.lines:
            # print line
            try:
                line.strip()
                line = line.strip('\r\n')  # .decode('utf8').encode('gbk', 'ignore')
                terms = line.split(',')
                if len(terms) >= index_citycode:
                    if terms[index_address] == "address" or len(terms[index_address]) > 500:
                        continue

                    addr = terms[index_address]
                    phone = terms[index_phone]
                    mobile = terms[index_mobile]
                    citycode = terms[index_citycode]

                    if phone != mobile and phone != "" and mobile != "":
                        values = {"ak": ak, "addr": addr, "tel": phone, "mobile": mobile, "citycode": citycode}
                        data = urllib.urlencode(values)
                        request = urllib2.Request(url, data)
                        response = urllib2.urlopen(request)
                        res_phone = response.read()
                        hjson = json.loads(res_phone, strict=False)

                        if hjson['status'] == 1:
                            err = hjson['result']['err']
                            msg = hjson['result']['msg']
                            terms.append(str(err))
                            terms.append(msg.encode("utf8"))
                            terms.append("")
                            terms.append("")
                            # print err, msg
                        elif hjson['status'] == 0:
                            err = hjson['result']['err']
                            deptcode = hjson['result']['deptcode']
                            if znoMap.get(deptcode) != None:
                                deptcode = znoMap[deptcode]
                            teamcode = hjson['result']['teamcode']
                            terms.append(str(err))
                            terms.append("")
                            terms.append(str(deptcode))
                            terms.append(str(teamcode))
                            # print err, deptcode, teamcode

                        newline = ",".join(terms) + "\n"
                        self.queryResults += newline
                        self.nCount += 1

                    else:
                        tel = ""
                        if phone != "":
                            tel = phone
                        elif mobile != "":
                            tel = mobile

                        if tel != "":
                            values = {"ak":ak, "addr": addr, "tel": tel, "qtype": "tel", "citycode": citycode}
                            data = urllib.urlencode(values)
                            request = urllib2.Request(url, data)
                            response = urllib2.urlopen(request)
                            res = response.read()
                            hjson = json.loads(res, strict=False)

                            if hjson['status'] == 1:
                                err = hjson['result']['err']
                                msg = hjson['result']['msg']
                                terms.append(str(err))
                                terms.append(msg.encode("utf8"))
                                terms.append("")
                                terms.append("")
                                # print err, msg
                            elif hjson['status'] == 0:
                                err = hjson['result']['err']
                                deptcode = hjson['result']['deptcode']
                                if znoMap.get(deptcode) != None:
                                    deptcode = znoMap[deptcode]
                                teamcode = hjson['result']['teamcode']
                                terms.append(str(err))
                                terms.append("")
                                terms.append(str(deptcode))
                                terms.append(str(teamcode))
                                # print err, deptcode, teamcode

                            newline = ",".join(terms) + "\n"
                            self.queryResults += newline
                            self.nCount += 1

                    if self.nCount % 1 == 0:
                        fw.write(self.queryResults)
                        self.queryResults = ""
                        print self.outfile + ":" + str(self.nCount)

            except Exception as e:
                print e
                print line
                pass

        if self.queryResults != "":
            fw.write(self.queryResults)
            self.queryResults = ""
            fw.flush()
            fw.close()


index_phone = 0
index_mobile = 1
index_address = 2
index_citycode = 11
index_sssdeptcode = 3
index_gisdeptcode = 4
index_tt_deptcode = 5
index_dept = 15


def get_field_index(fields, field_name):
    for i in range(0, len(fields)):
        field = fields[i]
        if field.lower() == field_name.lower():
            return i
    return -1


def getResultIndex(terms):
    global index_phone, index_mobile, index_address, index_citycode

    ret = get_field_index(terms, "phone")
    if ret != -1:
        index_phone = ret

    ret = get_field_index(terms, "mobile")
    if ret != -1:
        index_mobile = ret

    ret = get_field_index(terms, "address")
    if ret != -1:
        index_address = ret

    ret = get_field_index(terms, "citycode")
    if ret != -1:
        index_citycode = ret


def loadZnolist(zno_file):
    fread = open(zno_file, "rb")
    totalCount = 0

    for line in fread:
        terms = line.strip("\r\n").split(',')
        totalCount += 1
        if totalCount == 1:
            continue
        if len(terms) >= 2 and terms[0] != terms[2]:
            znoMap[terms[0]] = terms[2]


def handle_utf8_bom(group_file):
    """
    清除文件头的bom
    :param group_file:
    :return:
    """
    BUFSIZE = 4096
    BOMLEN = len(codecs.BOM_UTF8)

    with open(group_file, "r+b") as fp:
        chunk = fp.read(BUFSIZE)
        if chunk.startswith(codecs.BOM_UTF8):
            i = 0
            chunk = chunk[BOMLEN:]
            while chunk:
                fp.seek(i)
                fp.write(chunk)
                i += len(chunk)
                fp.seek(BOMLEN, os.SEEK_CUR)
                chunk = fp.read(BUFSIZE)
            fp.seek(-BOMLEN, os.SEEK_CUR)
            fp.truncate()
    print "utf8 bom handled!"


thread_no = 16
url = "http://10.203.33.198:8080/teltc/tc/bytel?"
ak = "8bb09e5e110845f39a000391668e3e80"
znoMap = {}


def main():
    # input = sys.argv[1]
    # znolist = sys.argv[2]
    # output = sys.argv[3]

    input = "D:\\diffSplit\\sit\\phone\\738\\test\\738_teltc_testdata_tt.csv"
    znolist = "D:\\diffSplit\\sit\\phone\\738\\test\\738_exportZnoList20181228120214.csv"
    output = "D:\\diffSplit\\sit\\phone\\738\\test\\738_teltc_testdata_tt.csv-out.csv"

    t1 = time.time()

    loadZnolist(znolist)
    handle_utf8_bom(input)

    ## process
    f = open(input)
    lines = f.read().splitlines()
    # 验证字段是否合法
    terms = lines[0].strip("\r\n").split(',')

    global index_phone, index_mobile, index_address, index_citycode, index_tt_deptcode
    getResultIndex(terms)

    total_count = len(lines)
    threads = []
    ll = total_count / thread_no

    for i in range(thread_no - 1):
        Opreprocessor = Cpreprocessor(lines[ll * i:ll * (i + 1)], output + "." + str(i) + ".csv")
        Opreprocessor.setDaemon(True)
        threads.append(Opreprocessor)

    Opreprocessor = Cpreprocessor(lines[ll * (thread_no - 1):], output + "." + str(thread_no - 1) + ".csv")
    Opreprocessor.setDaemon(True)
    threads.append(Opreprocessor)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    # 写表头
    fw = open(output, "w")
    terms.append("err")
    terms.append("msg")
    terms.append("dept")
    terms.append("team")
    header = ",".join(terms) + "\n"
    fw.write(header)

    for i in range(thread_no):
        for line in open(output + "." + str(i) + ".csv", "r"):
            fw.write(line)
        os.remove(output + "." + str(i) + ".csv")

    fw.close()

    print "begin to total..."
    sssdept = 0
    sssdept_null = 0
    sssdept_match = 0
    gisdept = 0
    gisdept_null = 0
    gisdept_match = 0
    ttdept = 0
    ttdept_null = 0
    ttdept_match = 0
    dept = 0
    dept_null = 0
    dept_comm = 0
    dept_match = 0
    global index_sssdeptcode, index_gisdeptcode, index_tt_deptcode, index_dept

    fread = open(output, "rb")
    freadres = open(output + ".result.csv", "wb")
    totalCount = 0

    for line in fread:
        terms = line.strip("\r\n").split(',')
        totalCount += 1
        if totalCount == 1:
            getResultIndex(terms)
            continue
        if len(terms) >= index_dept:
            if terms[index_sssdeptcode] == "" or terms[index_dept] == "":
                sssdept_null += 1
            else:
                sssdept += 1
                if terms[index_dept] == terms[index_sssdeptcode]:
                    sssdept_match += 1

            if terms[index_gisdeptcode] == "" or terms[index_dept] == "":
                gisdept_null += 1
            else:
                gisdept += 1
                if terms[index_dept] == terms[index_gisdeptcode]:
                    gisdept_match += 1

            if terms[index_tt_deptcode] == "" or terms[index_dept] == "":
                ttdept_null += 1
            else:
                ttdept += 1
                if terms[index_dept] == terms[index_tt_deptcode]:
                    ttdept_match += 1

            if terms[index_dept] == "":
                dept_null += 1
            else:
                dept += 1

            if terms[index_sssdeptcode] == terms[index_gisdeptcode] and terms[index_sssdeptcode] != "" and terms[
                index_dept] != "":
                dept_comm += 1
                if terms[index_dept] == terms[index_sssdeptcode]:
                    dept_match += 1

    freadres.write(output + "\n")
    freadres.write("sssdeptcode: count:" + str(sssdept) + ", null:" + str(sssdept_null) + ", match:" + str(
        sssdept_match) + ", rate:" + str(sssdept_match * 1.0 / sssdept) + "\n")
    freadres.write("gisdeptcode: count:" + str(gisdept) + ", null:" + str(gisdept_null) + ", match:" + str(
        gisdept_match) + ", rate:" + str(gisdept_match * 1.0 / gisdept) + "\n")
    freadres.write("ttdeptcode: count:" + str(ttdept) + ", null:" + str(ttdept_null) + ", match:" + str(
        ttdept_match) + ", rate:" + str(ttdept_match * 1.0 / ttdept) + "\n")
    freadres.write("dept_comm: count:" + str(dept_comm) + ", match:" + str(dept_match) + ", rate:" + str(
        dept_match * 1.0 / dept_comm) + "\n")
    freadres.write("dept: count:" + str(dept) + ", null:" + str(dept_null) + ", null:" + ", rate:" + str(
        dept * 1.0 / (dept + dept_null)) + "\n")
    freadres.close()

    t2 = time.time()
    print 'process used %ds./n' % (t2 - t1)


if __name__ == "__main__":
    main()
    print "end!"