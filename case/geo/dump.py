import os,sys,unittest,time
from lib.test_abstract import TestAbstract
from lib.wxls import geturl
from lib.wxls import *

url1 = 'http://gis-rss.intsit.sfdc.com.cn:1080/geo'

url=geturl("geo")
print (url)