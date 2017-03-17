# -*- coding: utf-8 -*-
import os,sys,unittest,time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from test_abstract import TestAbstract
from lib.userinfo import UserInfo

class TestUserinfo(TestAbstract):

	userinfo = UserInfo()

	def test_get_empty(self):
		url = self.getConfig('userinfo','url') + 'userinfo/get'
		res = self.requestGET(url,{'uid':'0'})
		print res
		self.assertEqual(102,res['errno'])
		self.assertEqual('not exist user',res['errmsg'])
		self.assertEqual([],res['data'])

	def test_get_success(self):
		url = self.getConfig('userinfo','url') + 'userinfo/get'
		uid = self.userinfo.add()
		print uid
		res = self.requestGET(url,{'uid':uid})
		print res
		self.assertEqual(0,res['errno'])
		self.assertEqual('',res['errmsg'])
		self.assertEqual(uid,res['data'][0]['uid'])

	def test_set_success(self):
		url = self.getConfig('userinfo','url') + 'userinfo/set'
		uid = self.userinfo.add()
		print uid
		res = self.requestGET(url,{'uid':uid,'mobile':'13511112222'})
		print res
		self.assertEqual(0,res['errno'])
		self.assertEqual('',res['errmsg'])




