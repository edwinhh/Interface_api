#-*- coding: utf-8 -*-
from ftplib import FTP
import sys,os


# remotefile="\\何昊\\ftp.txt"
remotedir="/输入提示/V1.23"
#remotedir="/ftp/HJZ"
# localfile="E:\\test\\ftp.txt"
localdir=r"E:/test"



def ftpconnect():
    ftp_server = '10.202.15.196'  # FTP server ip address
    username = 'guigen'
    password = 'hgg'
    port = 21
    timeout = 3000
    ftp = FTP()
    #ftp.set_debuglevel(2)  # open debug level 2, can display detail message
    ftp.connect(ftp_server, port)  # connect to FTP server
    ftp.login(username, password)
    return ftp



def download_file(ftp,localfile, remotefile):
    # if self.is_same_size(localfile, remotefile):
    #     print('%s 文件大小相同，无需下载' % localfile)
    #     return
    # else:
    #     print('>>>>>>>>>>>>下载文件 %s ... ...' % localfile)
        # return
    file= open(localfile.decode('utf-8'), "wb")
    bufsize = 1024
    ftp.retrbinary('RETR %s' %remotefile, file.write)
    file.close()

def download_files(ftp,localdir, remotedir):
    file_list = []
    try:
        ftp.cwd(remotedir)
    except:
        print"目录%s不存在，继续...' %remotedir"
        return

    #os.chdir(os.path.dirname(localdir))
    if not os.path.isdir(localdir):
        os.mkdir(localdir.decode('utf-8'))

    ftp.dir(file_list.append)




        #print(remotenames)
        #return
    for item in file_list:
        filetype = item.split()[0][0:1]
        name = item.split()[8]
        local = localdir + '/' + name
        remote = remotedir + '/' + name
        if filetype == 'd':
            if name not in ['.','..']:
                print local
                download_files(ftp,local, remote)
            # ftp.cwd('..')
            # os.chdir('..')


        elif filetype == '-':
            download_file(ftp,local, remote)
            print local





if __name__ == "__main__":
    ftp = ftpconnect()
    download_files(ftp,localdir, remotedir)
    # uploadfile_to_FTP()