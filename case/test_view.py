# -*- coding: utf-8 -*-
import os,sys,unittest,time
from Interface_api.lib.test_abstract import TestAbstract

class TestView(TestAbstract):

	def test_get_view(self):
		url = self.getConfig('jenkins','url') + '/view/selenium/api/json'
		res = self.requestGET(url,auth={'username':'mazheng','password':'123456'})
		print res
		self.assertEquals(2,len(res['jobs']))

	def test_get_view_with_tree(self):
		url = self.getConfig('jenkins','url') + '/view/selenium/api/json'
		res = self.requestGET(url,{'tree':'jobs[name,url]'},auth={'username':'mazheng','password':'123456'})
		print res
		self.assertEquals(2,len(res['jobs']))







