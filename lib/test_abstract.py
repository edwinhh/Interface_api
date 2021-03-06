# -*- coding: utf-8 -*-
#python3


import unittest
import urllib
import urllib.request,urllib.parse, urllib.error

import os,sys,json,base64
import http.cookiejar
import configparser
import requests
import socket
import os,sys,json,base64
import time
import http.cookiejar
import configparser
from openpyxl import Workbook
import openpyxl
import urllib3
from urllib import parse


p=[]
r=[]
dic={}


class TestAbstract(unittest.TestCase):
	user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"

	headers = {'User-Agent': user_agent, 'Connection': 'keep-alive','Content-Type':'application/json;charset=UTF-8'}

	config_file=os.path.dirname(os.path.dirname(__file__)) + '/conf/base.conf'

	@classmethod
	def setUpClass(clz):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	@classmethod
	def tearDownClass(clz):
		pass

	def getConfig(self,section,key):
		config = configparser.ConfigParser()
		config.read(self.config_file)
		return config.get(section,key)

	def requestGET(self,url,data={},auth=None):


		# if None != data and len(data)>0:
		# 	req = urllib.request.Request(url + "?" + urllib.parse.urlencode(data),headers=self.headers)
		#
		# else:
		# 	req = urllib.request.Request(url,headers=self.headers)

		timeout = 30
		socket.setdefaulttimeout(timeout)

		if None != data and len(data)>0:
			
			#p=urllib.parse.urlencode(data).replace('%23','#')
			p = urllib.parse.urlencode(data)


			#req = urllib.request.Request(url + "?" +p ,headers=self.headers)
			req = urllib.request.Request(url + "?" + p)
			
			
		else:
			#req = urllib.request.Request(url,headers=self.headers)
			req = urllib.request.Request(url)
			
		if None != auth:
			req.add_header('Authorization',self.getAuthHeader(auth))
		   # 查看添加auth之后heads字段对比
		
		res = urllib.request.urlopen(req).read().decode('utf-8')
		#return res

		# start=time.time()
		# res = urllib.request.urlopen(req)
		# p.append(data)
		# r.append(res)
		# content=res.read().decode('utf-8')
		# end=time.time()
		# #print(end-start)
		# res.close()
		#print(self.formatResult(content))
		return self.formatResult(res)

	#return self.content


	def requestPOST(self,url,data={},type=''):

		# if type=='xml':
		# 	req = urllib.request.Request(url,data,{'Content-Type':'text/xml'},headers=self.headers)
		# else:
		#
		# 	req = urllib.request.Request(url,urllib.parse.urlencode(data).encode(encoding='UTF8'),headers=self.headers)
		# if None != auth:
		# 	req.add_header('Authorization',self.getAuthHeader(auth))
		# res = urllib.request.urlopen(req).read()
		# return self.formatResult(res)
		print(type)
		if type=='':
			req = urllib.request.Request(url,data,{'Content-Type':'text/xml'})
			print("1")
			print(req)
		else:
			if type=="json" :
				p=urllib.parse.urlencode(data).encode(encoding='UTF8')
				print("2")
				print(p)
			# print (urllib.parse.urlencode(data).replace('%23','#'))
			# print (urllib.parse.urlencode(data).replace('%23','#').encode(encoding='UTF8'))
			#c='address=##%E6%B7%B1%E5%9C%B3%E5%B8%82%E8%BD%AF%E4%BB%B6%E4%BA%A7%E4%B8%9A%E5%9F%BA%E5%9C%B0&ak=a4fbd3a08ecc4f9e41bc9b06421ef3b5&opt='
			#print (p)
				print(self.headers)
				req = urllib.request.Request(url,p,headers=self.headers)
				print("3")

		# if None != auth:
		# 	req.add_header('Authorization',self.getAuthHeader(auth))
		try:
			res = urllib.request.urlopen(req).read()
			print(res)
			
		except urllib.error.HTTPError as e:
			
			print(e.code)
			
			print(e.read().decode("utf8"))
		
		return self.formatResult(res)
	

	def formatResult(self,res):
		try:
			json_res = json.loads(res)
		except Exception as e:
			return res
		return json_res

	# def getAuthHeader(self,auth):
	# 	base64string = base64.encodestring('%s:%s' % ( str(auth['username']), str(auth['password']) )).encode())[:-1]
	# 	# base64string = base64.encodestring('%s:%s' % (((str(auth['username']), str(auth['password'])).encode()).decode()[:-1]
	# 	authheader = "Basic %s" % base64string
	# 	return authheader

	def getAuthHeader(self,auth):
		temp_str=str(auth['username'])+':'+str(auth['password'])
		base64string = base64.b64encode(temp_str.encode(encoding="utf-8"))
		authheader = "Basic" +base64string
		return authheader

	def savecookies(self,url, data={},cookie_fiename=os.path.dirname(__file__)+'/cookie.txt'):

		postdata = urllib.parse.urlencode(data).encode()


		cookie_filename =cookie_fiename
		cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
		handler = urllib.request.HTTPCookieProcessor(cookie)
		opener = urllib.request.build_opener(handler)

		request = urllib.request.Request(url, postdata, headers=self.headers)
		try:
			response = opener.open(request)
			page = response.read().decode()

		# k=response.info()

		# page1 = json.loads(page)
		# print(page)
		# for k,v in page1.items():
		#     print(k,v)
		except urllib.error.URLError as e:
			print('e',e)

		cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中

	def cookiesget(self,url,cookie_fiename=os.path.dirname(__file__)+'/cookie.txt'):
		cookie = http.cookiejar.MozillaCookieJar(cookie_fiename)
		cookie.load(cookie_fiename, ignore_discard=True, ignore_expires=True)
		handler = urllib.request.HTTPCookieProcessor(cookie)
		opener = urllib.request.build_opener(handler)

		get_url = url  # 利用cookie请求访问另一个网址
		get_request = urllib.request.Request(get_url, headers=self.headers)
		get_response = opener.open(get_request)
		res= get_response.read().decode()
		return self.formatResult(res)


	def cookiespost(self,url,data={},type='html',cookie_fiename=os.path.dirname(__file__)+'/cookie1.txt'):

		cookie = http.cookiejar.MozillaCookieJar(cookie_fiename)
		cookie.load(cookie_fiename, ignore_discard=True, ignore_expires=True)
		handler = urllib.request.HTTPCookieProcessor(cookie)
		opener = urllib.request.build_opener(handler)


		if type=='xml':
			req = urllib.request.Request(url,data,{'Content-Type':'text/xml'},headers=self.headers)
		else:
			req = urllib.request.Request(url,urllib.parse.urlencode(data).encode(encoding='UTF8'),headers=self.headers)

		get_response = opener.open(req)
		res= get_response.read().decode()
		return self.formatResult(res)



	def requestsget(self,url,data={}):
		urllib3.disable_warnings()
		# start=time.time()
		# session = requests.Session()
		# session.keep_alive = False
		res = requests.get(url, params=data,verify=False)
		# end = time.time()
		# print(self.formatResult(res.text))
		# print(end-start)
		return self.formatResult(res.text)
	    #return res.text
	
	def requestspost(self,url,data={}):
		res = requests.post(url, data=json.dumps(data), verify=False,headers=self.headers)
		
		return self.formatResult(res.text)







# if __name__ == "__main__":
# 	URL = 'http://testent.killerwhale.cn/services/user/login'
# 	data = {"ticket": "a7490b80-0f72-11e7-b8fa-ad8cd3c36cdb"}
# 	url1 = 'http://testent.killerwhale.cn/services/companyinfo/companyuserinfo'
# 	auth = {'username': 'admin008', 'password': '111111'}
# 	tmp1 = {'j_username': 'hehao', 'j_password': '123456', 'from': '/',
# 			'json': '{"j_username": "hehao", "j_password": "123456", "remember_me": false, "from": "/"}',
# 			'Submit': '登录'}
# 	k = 'http://ci.szzbmy.com/j_acegi_security_check'
# 	L = 'http://ci.szzbmy.com'
#
# 	# ck(k,tmp1,L)
# 	a = TestAbstract()
# 	# res1=a.savecookies(URL, data)
# 	# res2=a.cookiesget(url1)
# 	# print(type(res1))
# 	# print(type(res2))
#
# 	print(a.requestGET(url1,auth=auth))
# 	print(a.cookiesget(url1))

	# def get_basic_auth_str(username, password):
	# 	temp_str = username + ':' + password
	# 	# 转成bytes string
	# 	bytesString = temp_str.encode(encoding="utf-8")
	# 	# base64 编码
	# 	encodestr = base64.b64encode(bytesString)
	# 	# 解码
	# 	decodestr = base64.b64decode(encodestr)
	# 	return 'Basic ' + encodestr.decode()





