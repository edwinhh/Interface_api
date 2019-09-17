 #-*- coding: utf-8 -*-
from ftplib import FTP
import sys,os


remotefile="\\何昊\\ftp.txt"
remotedir="\\地理编码\\V2.1\\"
localfile="E:\\test\\ftp.txt"
localdir="E:\\test\\"



def ftpconnect():
    ftp_server = ''  # FTP server ip address
    username = ''
    password = ''
    timeout = 3000
    port = 21
    ftp = FTP()
    ftp.set_debuglevel(2)  # open debug level 2, can display detail message
    ftp.connect(ftp_server, port)  # connect to FTP server
    ftp.login(username, password)
    return ftp



def is_same_size(self, localfile, remotefile):
    try:
        remotefile_size = self.ftp.size(remotefile)
    except:
        remotefile_size = -1
    try:
        localfile_size = os.path.getsize(localfile)
    except:
        localfile_size = -1
    print('localfile_size:%d  remotefile_size:%d' % (localfile_size, ) )
    if remotefile_size == localfile_size:
        return 1
    else:
        return 0

# def get_filename(line):
#     pos = line.rfind(':')
#     while (line[pos] != ' '):
#         pos += 1
#     while (line[pos] == ' '):
#         pos += 1
#     file_arr = [line[0], line[pos:]]
#     return file_arr
#
# def get_file_list(file_list,line):
#     ret_arr = []
#     file_arr = get_filename(line)
#     if file_arr[1] not in ['.', '..']:
#         file_list.append(file_arr)



def download_file(ftp,localfile, remotefile):
    # if self.is_same_size(localfile, remotefile):
    #     print('%s 文件大小相同，无需下载' % localfile)
    #     return
    # else:
    #     print('>>>>>>>>>>>>下载文件 %s ... ...' % localfile)
        # return
    file= open(localfile.decode('utf-8'), "wb")
    bufsize = 2048
    ftp.retrbinary('RETR %s' %remotefile, file.write,bufsize)
    file.close()

def download_files(ftp,localdir, remotedir):
    file_list = []

    try:
        ftp.cwd(remotedir)
    except:
        print ("目录%s不存在，继续...' %remotedir")
        return
    if not os.path.isdir(localdir):
        os.makedirs(localdir)
    ftp.dir(file_list.append)
    # for i in file_list:
    #     print len(i.split())
    #     print i.split()[0][0:1]
    #     print i.split()[8]

        #print(remotenames)
        #return
    for item in file_list:
        filetype = item.split()[0][0:1]
        name = item.split()[8]
        local = os.path.join(localdir, name)
        if filetype == 'd':
            download_files(local, name)
        elif filetype == '-':
            download_file(ftp,local, name)
    ftp.cwd('..')
    print "返回上层目录 %s" %ftp.pwd()


if __name__ == "__main__":
    ftp = ftpconnect()
    download_files(ftp,localdir, remotedir)
    # uploadfile_to_FTP()