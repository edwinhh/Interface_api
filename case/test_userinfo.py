# -*- coding: utf-8 -*-
import os,sys,unittest,time,json
import http.cookiejar
import requests
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Interface_api.lib.test_abstract import TestAbstract


class TestUserinfo(TestAbstract):
	global null

	null = ''


	def test_get_empty(self):
		URL = 'http://testent.killerwhale.cn/services/user/login'
		data = {"ticket": "a7490b80-0f72-11e7-b8fa-ad8cd3c36cdb"}
		url1 = 'http://testent.killerwhale.cn/services/companyinfo/companyuserinfo'
		auth = {'username': 'admin008', 'password': '111111'}
		tmp1 = {'j_username': 'hehao', 'j_password': '123456', 'from': '/',
				'json': '{"j_username": "hehao", "j_password": "123456", "remember_me": false, "from": "/"}',
				'Submit': '登录'}
		k = 'http://ci.szzbmy.com/j_acegi_security_check'
		L = 'http://ci.szzbmy.com'

		# ck(k,tmp1,L)
		cookie_k = os.path.dirname(__file__)+'/cookie_k.txt'
		cookie_ent = os.path.dirname(__file__) + '/cookie_ent.txt'
		a = TestAbstract()
		a.savecookies(k, tmp1, cookie_k)
		a.savecookies(URL,data,cookie_ent)
		res = a.cookiesget(url1,cookie_ent)
		print(res)
		# self.assertEqual('成功',res['msg'])
		# self.assertEqual(0,res['errcode'])
		# res1=eval(res)
		# print(res1)
		# self.assertEqual("SUCCESS",res1["status"])
		# self.assertEqual('not exist user',res['errmsg'])
		# self.assertEqual([],res['data'])

	def test_1(self):
		res=self.requestGET("http://www.cnbeta.com")
		return res
if __name__ == '__main__':
	print(os.path.dirname(os.path.dirname(__file__)))
	a = TestUserinfo()
	print(a.test_1())
	# res1=requests.get("http://www.163.com")
	# print(res1.text)
	# def test_get_1(self):
    #
	# 	url1 = 'http://topic.csdn.net/u/20110123/15/F71C5EBB-7704-480B-9379-17A96E920FEE.html'
	# 	url2 ='http://testsso.killerwhale.cn/api/user/login'
	# 	url3= 'http://ci.szzbmy.com/view/Tuyoumi/'
	# 	auth = {'username': 'admin008', 'password': '123456'}
	# 	data = {'username': 'admin008', 'password': '111112'}
	# 	res = self.requestPOST(url2,data)
	# 	print (res.decode('utf8'))
		#self.assertEqual("SUCCESS", res["status"])
	# def test_get_success(self):
	# 	url = self.getConfig('userinfo','url') + 'userinfo/get'
	# 	uid = self.userinfo.add()
	# 	print uid
	# 	res = self.requestGET(url,{'uid':uid})
	# 	print res
	# 	self.assertEqual(0,res['errno'])
	# 	self.assertEqual('',res['errmsg'])
	# 	self.assertEqual(uid,res['data'][0]['uid'])
    #
	# def test_set_success(self):
	# 	url = self.getConfig('userinfo','url') + 'userinfo/set'
	# 	uid = self.userinfo.add()
	# 	print uid
	# 	res = self.requestGET(url,{'uid':uid,'mobile':'13511112222'})
	# 	print res
	# 	self.assertEqual(0,res['errno'])
	# 	self.assertEqual('',res['errmsg'])




	# cookiejar = cookielib.CookieJar()
	# urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    #
	# # Send login/password to the site and get the session cookie
	# values = {'login': login, 'password': password}
	# data = urllib.urlencode(values)
	# request = urllib2.Request("http://www.imdb.com/register/login", data)
	# url = urlOpener.open(request)  # Our cookiejar automatically receives the cookies
	# page = url.read(500000)
    #
	# # Make sure we are logged in by checking the presence of the cookie "id".
	# # (which is the cookie containing the session identifier.)
	# if not 'id' in [cookie.name for cookie in cookiejar]:
	# 	raise ValueError, "Login failed with login=%s, password=%s" % (login, password)
    #
	# print
	# "We are logged in !"
    #
	# # Make another request with our session cookie
	# # (Our urlOpener automatically uses cookies from our cookiejar)
	# url = urlOpener.open('http://imdb.com/find?s=all&q=grave')
	# page = url.read(200000)



