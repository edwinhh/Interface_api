#-*- coding: utf-8 -*-
from ftplib import FTP
import sys


def ftpconnect():
    ftp_server = '10.202.15.196'  # FTP server ip address
    username = 'guigen'
    password = 'hgg'
    timeout = 30
    port = 21

    ftp = FTP()
    ftp.set_debuglevel(2)  # open debug level 2, can display detail message
    ftp.connect(ftp_server, port, timeout)  # connect to FTP server
    ftp.login(username, password)

    return ftp


def downloadfile_from_FTP(argv):
    ftp = ftpconnect()
    #print ftp.getwelcome()  # can display FTP server welcome message.

    bufsize = 1024  # set buffer size
    for i in sys.argv[1:]:
        print "i:"+i
        remotepath = "\\何昊\\"+i
        localpath = "E:\\test\\"+i

        fp = open(localpath, "wb")
        ftp.retrbinary('RETR %s' % remotepath, fp.write, bufsize)  # start to download file :FTP server --> local

        ftp.set_debuglevel(0)  # close debug

        fp.close()  # close connect

    ftp.quit()  # quit FTP server


def uploadfile_to_FTP():
    ftp = ftpconnect()
    #print ftp.getwelcome()  # can display FTP server welcome message.
    bufsize = 1024
    remotepath = "\\何昊\\geo&rgeo.jmx"
    localpath = 'E:\\test'
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)  # start to upload file :local --> FTP server
    ftp.set_debuglevel(0)  # close debug
    fp.close()  # close connect
    ftp.quit()  # quit FTP server


if __name__ == "__main__":
    downloadfile_from_FTP(sys.argv[2:])
    # uploadfile_to_FTP()