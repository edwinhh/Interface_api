# -*- coding: utf-8 -*-
import os,sys,unittest,time
from Interface_api.lib.test_abstract import TestAbstract

class TestJob(TestAbstract):

	def test_get_job(self):
		url = self.getConfig('jenkins','url') + '/job/api001/api/json'
		res = self.requestGET(url,auth={'username':'mazheng','password':'123456'})
		print res
		self.assertEquals(1,res['nextBuildNumber'] - res['lastBuild']['number'] )

	def test_get_job_with_number(self):
		url = self.getConfig('jenkins','url') + '/job/api001/api/json'
		res = self.requestGET(url,auth={'username':'mazheng','password':'123456'})
		number = str(res['lastBuild']['number'])
		url = self.getConfig('jenkins','url') + '/job/api001/'+number+'/api/json'
		res = self.requestGET(url,auth={'username':'mazheng','password':'123456'})
		print res
		self.assertEquals('SUCCESS',res['result'])


	def test_build_job(self):
		url = self.getConfig('jenkins','url') + '/job/api001/build'
		res = self.requestPOST(url,auth={'username':'mazheng','password':'123456'})

	def test_build_job_with_param(self):
		url = self.getConfig('jenkins','url') + '/job/api002/buildWithParameters'
		res = self.requestPOST(url,data={'pa':'hello','pb':'world'},auth={'username':'mazheng','password':'123456'})



