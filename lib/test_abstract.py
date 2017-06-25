# -*- coding: utf-8 -*-
#python3
import unittest
import urllib
import urllib.request,urllib.parse, urllib.error
import os,sys,json,base64
import http.cookiejar
import configparser

class TestAbstract(unittest.TestCase):
	user_agent = "'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept - Language': 'zh - CN, zh;q = 0.8'"
	headers = {'User-Agent': user_agent, 'Connection': 'keep-alive','Accept - Language': 'zh - CN, zh;q = 0.8'}

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

		if None != data and len(data)>0:
			req = urllib.request.Request(url + "?" + urllib.parse.urlencode(data),headers=self.headers)
		else:
			req = urllib.request.Request(url,headers=self.headers)
			# print(req.headers)
		if None != auth:
			req.add_header('Authorization',self.getAuthHeader(auth))
			# print(req.headers)            查看添加auth之后heads字段对比
		res = urllib.request.urlopen(req).read().decode('utf-8')
		return res

	def requestPOST(self,url,data={},auth=None,type='html'):

		if type=='xml':
			req = urllib.request.Request(url,data,{'Content-Type':'text/xml'},headers=self.headers)
		else:
			req = urllib.request.Request(url,urllib.parse.urlencode(data).encode(encoding='UTF8'),headers=self.headers)
		if None != auth:
			req.add_header('Authorization',self.getAuthHeader(auth))
		res = urllib.request.urlopen(req).read()
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
		base64string = base64.encodestring(('%s:%s' % (str(auth['username']), str(auth['password']) )).encode())[:-1]
		authheader = "Basic %s" % base64string
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




