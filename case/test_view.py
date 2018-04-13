# -*- coding: utf-8 -*-
import os,sys,unittest,time
<<<<<<< d4c1796fe2af615ff7231609b7167ff5870d3a6c
from Interface_api.lib.test_abstract import TestAbstract
=======
from lib.test_abstract import TestAbstract
>>>>>>> 添加多线程执行并相同顺序写入文件

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

<<<<<<< d4c1796fe2af615ff7231609b7167ff5870d3a6c
=======
	# def test_get_job(self):
	# 	url = self.getConfig('jenkins','url') + '/job/api001/api/json'
	# 	res = self.requestGET(url,auth={'username':'mazheng','password':'123456'})
	# 	print res
	# 	self.assertEquals(1,res['nextBuildNumber'] - res['lastBuild']['number'] )
	#
	# def test_get_job_with_number(self):
	# 	url = self.getConfig('jenkins','url') + '/job/api001/api/json'
	# 	res = self.requestGET(url,auth={'username':'mazheng','password':'123456'})
	# 	number = str(res['lastBuild']['number'])
	# 	url = self.getConfig('jenkins','url') + '/job/api001/'+number+'/api/json'
	# 	res = self.requestGET(url,auth={'username':'mazheng','password':'123456'})
	# 	print res
	# 	self.assertEquals('SUCCESS',res['result'])
	#
	#
	# def test_build_job(self):
	# 	url = self.getConfig('jenkins','url') + '/job/api001/build'
	# 	res = self.requestGET(url,auth={'username':'mazheng','password':'123456'})
	#
	# def test_build_job_with_param(self):
	# 	url = self.getConfig('jenkins','url') + '/job/api002/buildWithParameters'
	# 	res = self.requestGET(url,data={'pa':'hello','pb':'world'},auth={'username':'mazheng','password':'123456'})

>>>>>>> 添加多线程执行并相同顺序写入文件






