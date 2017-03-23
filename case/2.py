# -*- coding: utf-8 -*-
# 引入webdriver和unittest所需要的包
import urllib.request, urllib.parse, urllib.error
# import http.cookiejar
import unittest, time, re,os,json
from case.test_abstract import TestAbstract

# 引入HTMLTestRunner包
import HTMLTestRunner


# def ck(url,data,url1):
#     URL = url
#     data = data
#     postdata = urllib.parse.urlencode(data).encode()
#     user_agent = "'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept - Language': 'zh - CN, zh;q = 0.8'"
#     headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
#
#     cookie_filename = os.path.dirname(__file__)+'/cookie1.txt'
#     cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
#     handler = urllib.request.HTTPCookieProcessor(cookie)
#     opener = urllib.request.build_opener(handler)
#
#     request = urllib.request.Request(URL, postdata,  headers = headers)
#     try:
#         response = opener.open(request)
#         page = response.read().decode()
#         # k=response.info()
#
#         # page1 = json.loads(page)
#         # print(page)
#         # for k,v in page1.items():
#         #     print(k,v)
#     except urllib.error.URLError as e:
#         print(e.code, ':', e.reason)
#
#     cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
#     # print(cookie)
#     # # for item in cookie:
#     # #     print('Name = ' + item.name)
#     # #     print('Value = ' + item.value)
#
#     # get_  # 利用cookie请求访问另一个网址
#
#     cookie1 = http.cookiejar.MozillaCookieJar(cookie_filename)
#     cookie1.load(cookie_filename, ignore_discard=True, ignore_expires=True)
#     print(cookie1)
#     handler = urllib.request.HTTPCookieProcessor(cookie1)
#     opener = urllib.request.build_opener(handler)
#
#     get_url = url1  # 利用cookie请求访问另一个网址
#     get_request = urllib.request.Request(get_url,  headers = headers)
#     get_response = opener.open(get_request)
#     print(get_response.read().decode())



if __name__ == "__main__":
    URL = 'http://testent.killerwhale.cn/services/user/login'
    data = {"ticket": "a7490b80-0f72-11e7-b8fa-ad8cd3c36cdb"}
    url1 = 'http://testent.killerwhale.cn/services/companyinfo/companyuserinfo'
    auth = {'username': 'admin008', 'password': '111111'}
    tmp1 = {'j_username':'hehao','j_password':'123456','from':'/',
            'json':'{"j_username": "hehao", "j_password": "123456", "remember_me": false, "from": "/"}',
            'Submit':'登录'}
    k='http://ci.szzbmy.com/j_acegi_security_check'
    L='http://ci.szzbmy.com'


    # ck(k,tmp1,L)
    cookie=os.path.dirname(__file__)+'/cookie1.txt'
    a = TestAbstract()
    # res1=a.savecookies(URL, data)
    # res2=a.cookiesget(url1)
    # print(type(res1))
    # print(type(res2))

    print(a.requestGET(url1, auth=auth))
    res=a.cookiesget(url1)['msg']
    assert('成功1'==res['msg'])