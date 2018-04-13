# -*- coding: utf-8 -*-
import os,sys,unittest,time
from Interface_api.lib.test_abstract import TestAbstract

class TestDemo(TestAbstract):

	def test_001(self):
		#time.strftime("$Y-%m-%d %H:%M:%S")
		data = """
<project>
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <assignedNode>master</assignedNode>
  <canRoam>false</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders/>
  <publishers/>
  <buildWrappers/>
</project>
		"""
		url = self.getConfig('jenkins','url') + '/createItem?name=123'
		print url
<<<<<<< d4c1796fe2af615ff7231609b7167ff5870d3a6c
		res = self.requestPOST(url,data=data,auth={'username':'mazheng','password':'123456'},type='xml')
=======
		res = self.requestGET(url,data=data,auth={'username':'mazheng','password':'123456'},type='xml')
>>>>>>> 添加多线程执行并相同顺序写入文件
		print res




	def test002(self):
		url = self.getConfig('jenkins','url') + '/job/123/enable'
		print url
<<<<<<< d4c1796fe2af615ff7231609b7167ff5870d3a6c
		res = self.requestPOST(url,data={},auth={'username':'mazheng','password':'123456'})
=======
		res = self.requestGET(url,data={},auth={'username':'mazheng','password':'123456'})
>>>>>>> 添加多线程执行并相同顺序写入文件
		print res

	def test003(self):
		url = self.getConfig('jenkins','url') + '/job/123/disable'
		print url
<<<<<<< d4c1796fe2af615ff7231609b7167ff5870d3a6c
		res = self.requestPOST(url,data={},auth={'username':'mazheng','password':'123456'})
=======
		res = self.requestGET(url,data={},auth={'username':'mazheng','password':'123456'})
>>>>>>> 添加多线程执行并相同顺序写入文件
		print res

	def test004(self):
		url = self.getConfig('jenkins','url') + '/job/123/description'
		print url
		res = self.requestGET(url,data={},auth={'username':'mazheng','password':'123456'})
		print res

	def test005(self):
		url = self.getConfig('jenkins','url') + '/job/123/config.xml'
		print url
		res = self.requestGET(url,data={},auth={'username':'mazheng','password':'123456'})
		print res

	def test_delete(self):
		url = self.getConfig('jenkins','url') + '/job/123/doDelete'
		print url
<<<<<<< d4c1796fe2af615ff7231609b7167ff5870d3a6c
		res = self.requestPOST(url,data={},auth={'username':'mazheng','password':'123456'})
=======
		res = self.requestGET(url,data={},auth={'username':'mazheng','password':'123456'})
>>>>>>> 添加多线程执行并相同顺序写入文件
		print res