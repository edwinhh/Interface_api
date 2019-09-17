import os, sys, unittest, time, json
from lib.test_abstract import TestAbstract
from lib.wxls import *
import traceback
from functools import partial
from pathos.multiprocessing import ProcessingPool
import threading
import time
import numpy as np

# 做新旧对比，将文档每行具体地址通过,拆分为参数，然后多线程执行
p1 = []
r1 = []
p2 = []
r2 = []
p3 = []
r3 = []
T1 = []
T2 = []
T3 = []
filelist = []
test = 1

# url2='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'
# url2='http://10.202.52.103:8080/geo'
# url1='http://gis-int.intsit.sfdc.com.cn:1080/geo/api'

url1 = 'http://gis-int.intsit.sfdc.com.cn:1080/tip/api'
url2 = 'http://gis-int.intsit.sfdc.com.cn:1080/tip/api'
url3 = 'http://gis-int.intsit.sfdc.com.cn:1080/tip/api'

name = os.path.basename(__file__).split('.')[0]

file = "e:/项目/地理编码/数据/加密/测试2.txt"


# file="e:/项目/地理编码/数据/cx2.csv"

class geo_Mutest(TestAbstract):
	def __init__(self):
		self.num = 0
		self.datas = []
		self.datas1 = []
	
	def readcsv(self, file):
		with open(file, 'r', encoding='utf_8')as f:
			for line in f.readlines():
				if len(line) == 1 or line.startswith('#'):
					continue
				self.num += 1
				
				temp = line.strip().split(",")
				
				data1 = {'q': temp[0], \
						 'opt': "sf30", \
						 'city': temp[2], \
						 'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
				data2 = {'q': temp[1], \
						 'opt': "sf30", \
						 'city': temp[2], \
						 'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
				data3 = {'q': temp[0], \
						 'opt': "sf30", \
						 'city': temp[2], \
						 'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
				
				# data1 = {'address': temp[0], \
				#         'opt': '', \
				#         'city': "香港", \
				#          'span':"1", \
				#          'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
				# data2 = {'address': temp[0], \
				#         'opt': '', \
				#         'city': "香港", \
				#          'span':"1", \
				#          'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
				self.datas1.append(data1)
				self.datas1.append(data2)
				self.datas1.append(data3)
				self.datas.append(self.datas1)
				self.datas1 = []
	
	def openfile(self, a):
		now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
		# file2 = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/report' + '/' + name + "_" + now + ".txt"
		file2 = os.path.dirname(os.path.dirname(__file__)) + '/report'+ '/tip' + '/' + 'tip_' + a + "_" + now + ".txt"
		filelist.append(file2)
		# os.mknod(rfile)
		# with open(file2, 'w+', encoding='utf_8')as f
		f = open(file2, 'a', encoding='utf_8')
		return f
	
	def report(self, f, url, data, res):
		
		# f.write(str(i + 1))
		f.write('\t')
		# f.write(n[i])
		f.write('\n')
		for i in range(len(data)):
			temp = []
			for key in data[i]:
				temp.append(key + "=" + data[i][key])
			parameters = "&".join(temp)
			case = url + "?" + parameters
			f.write(str(i + 1))
			f.write('\n')
			f.write(case)
			f.write('\n\n')
			f.write(str(res[i]))
			f.write('\n')
	
	def err(self, url2, url3, r1, r2, r3, p1, p2, p3):
		reqnew = []
		resnew = []
		resold = []
		node = {}
		k = 0
		now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
		diff_post_ED = "e:/project/Interface_api-master/report/tip/" + "diff_post加密与get对比_" + now + ".txt"
		diff_post = "e:/project/Interface_api-master/report/tip/" + "diff_post非加密与get对比_" + now + ".txt"
		p_ED = open(diff_post_ED, 'w', encoding='utf-8')
		p = open(diff_post, 'w', encoding='utf-8')
		
		for i in range(len(p1)):
			# print (json.loads(newres[i])["status"])
			# print ("&")
			# print (type(json.loads(oldres[i])["status"]))
			
			if r2[i]["status"] == 1 and r1[i]["status"] == 0:
				k = k + 1
				temp = []
				for key in p2[i]:
					temp.append(key + "=" + p2[i][key])
				parameters = "&".join(temp)
				case = url2 + "?" + parameters
				p_ED.write(str(k))
				p_ED.write('\n')
				p_ED.write(case)
				p_ED.write('\n')
				p_ED.write(json.dumps(r2[i]))
				p_ED.write('\n\n')
			if r3[i]["status"] == 1 and r1[i]["status"] == 0:
				k = k + 1
				temp = []
				for key in p3[i]:
					temp.append(key + "=" + p3[i][key])
				parameters = "&".join(temp)
				case = url3 + "?" + parameters
				p.write(str(k))
				p.write('\n')
				p.write(case)
				p.write('\n')
				p.write(json.dumps(r2[i]))
				p.write('\n\n')
	
	def empty(self, url2, url3, r1, r2, r3, p1, p2, p3):
		reqnew = []
		resnew = []
		resold = []
		node = {}
		k = 0
		now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
		empty_post_ED = "e:/project/Interface_api-master/report/tip/" + "empty_post加密与get对比_" + now + ".txt"
		empty_post = "e:/project/Interface_api-master/report/tip/" + "empty_post非加密与get对比_" + now + ".txt"
		e_ED = open(empty_post_ED, 'w', encoding='utf-8')
		e = open(empty_post, 'w', encoding='utf-8')
		
		for i in range(len(p1)):
			# if json.loads(oldres[i])["status"] == 0:
			#     print (json.loads(oldres[i])["result"]["src"])
			
			# print ("&")
			# print (type(json.loads(oldres[i])["status"]))
			if r2[i]["status"] == 0 and r1[i]["status"] == 0:
				if r2[i]["result"]["src"] == "empty" and r1[i]["result"]["src"] != "empty":
					k = k + 1
					temp = []
					for key in p2[i]:
						temp.append(key + "=" + p2[i][key])
					parameters = "&".join(temp)
					case = url2 + "?" + parameters
					e_ED.write(str(k))
					e_ED.write('\n')
					e_ED.write(case)
					e_ED.write('\n')
					e_ED.write(json.dumps(r2[i]))
					e_ED.write('\n\n')
			# print ((type(r3[i])))
			# print (type(json.loads(r3[i])))
			# print (r3[i])
			if r3[i]["status"] == 0 and r1[i]["status"] == 0:
				if r3[i]["result"]["src"] == "empty" and r1[i]["result"]["src"] != "empty":
					k = k + 1
					temp = []
					for key in p3[i]:
						temp.append(key + "=" + p3[i][key])
					parameters = "&".join(temp)
					case = url3 + "?" + parameters
					e_ED.write(str(k))
					e_ED.write('\n')
					e_ED.write(case)
					e_ED.write('\n')
					e_ED.write(json.dumps(r3[i]))
					e_ED.write('\n\n')
	
	def geo(self, data, url, p, r):
		global test
		for i in data:
			res = self.requestGET(url, i)
			p.append(i)
			r.append(res)
			# print(test)
			test += 1
			
			
			# try:
			#     assert 0 == res['status']
			# except AssertionError as ae:  # 明确抛出此异常
			#         # 抛出 AssertionError 不含任何信息，所以无法通过 ae.__str__()获取异常描述
			#     print('[AssertionError]', ae, ae.__str__())
			#     print('[traceback]')
			#     traceback.print_exc()
			#     print('assert except')
	
	def geo2(self, data, url1, url2, url3):
		global test
		
		for i in data:
			tp = []
			tr = []
			s1 = time.time()
			res = self.requestGET(url1, i[0])
			e1 = time.time()
			T1.append(e1 - s1)
			tp.append(i[0])
			tr.append(res)
			s2 = time.time()
			res = self.requestPOST(url2, i[1])
			e2 = time.time()
			T2.append(e2 - s2)
			tp.append(i[1])
			tr.append(res)
			s3 = time.time()
			res = self.requestGET(url3, i[2])
			e3 = time.time()
			T3.append(e2 - s2)
			tp.append(i[2])
			tr.append(res)
			p1.append(tp[0])
			r1.append(tr[0])
			p2.append(tp[1])
			r2.append(tr[1])
			p3.append(tp[2])
			r3.append(tr[2])
			print(test)
			test += 1
	
	def splist(self, ls, n):
		if not isinstance(ls, list) or not isinstance(n, int):
			return []
		ls_len = len(ls)
		if n <= 0 or 0 == ls_len:
			return []
		if n > ls_len:
			return []
		elif n == ls_len:
			return [[i] for i in ls]
		else:
			j = int(ls_len / n)
			k = int(ls_len % n)
			### j,j,j,...(前面有n-1个j),j+k
			# 步长j,次数n-1
			ls_return = []
			for i in range(0, (n - 1) * j, j):
				ls_return.append(ls[i:i + j])
				# 算上末尾的j+k
			ls_return.append(ls[(n - 1) * j:])
			return ls_return


if __name__ == "__main__":
	
	k = 16
	x = geo_Mutest()
	x.readcsv(file)
	splist = x.splist(x.datas, k)
	
	thread_list = []  # 线程存放列表
	for i in range(k):
		t = threading.Thread(target=x.geo2, args=(splist[i], url1, url2, url3))
		t.setDaemon(True)
		thread_list.append(t)
	
	for t in thread_list:
		t.start()
	
	for t in thread_list:
		t.join()
	
	# print(p1)
	# print('\n')
	# print(p2)
	# for i in p:
	#     print(i[0])
	#     print(i[1])
	print ("get执行时间：%f秒" % (np.sum(T1)))
	print ("post加密执行时间：%f秒" % (np.sum(T2)))
	print ("post非加密执行时间：%f秒" % (np.sum(T3)))
	f1 = x.openfile("get执行结果")
	x.report(f1, url1, p1, r1)
	f2 = x.openfile("post加密结果")
	x.report(f2, url2, p2, r2)
	f3 = x.openfile("post非加密结果")
	x.report(f3, url3, p3, r3)
	x.err(url2, url3, r1, r2, r3, p1, p2, p3)
	x.empty(url2, url3, r1, r2, r3, p1, p2, p3)






