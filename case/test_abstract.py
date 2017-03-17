# -*- coding: utf-8 -*-
import unittest
import urllib,urllib2
import os,json,base64
import ConfigParser

class TestAbstract(unittest.TestCase):

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
		config = ConfigParser.ConfigParser()
		config.read(self.config_file)
		return config.get(section,key)

	def requestGET(self,url,data={},auth=None):
		if None != data and len(data)>0:
			req = urllib2.Request(url + "?" + urllib.urlencode(data))
		else:
			req = urllib2.Request(url)
		if None != auth:
			req.add_header('Authorization',self.getAuthHeader(auth))
		res = urllib2.urlopen(req).read()
		return self.formatResult(res)

	def requestPOST(self,url,data={},auth=None,type='html'):
		if type=='xml':
			req = urllib2.Request(url,data,{'Content-Type':'text/xml'})
		else:
			req = urllib2.Request(url,urllib.urlencode(data))
		if None != auth:
			req.add_header('Authorization',self.getAuthHeader(auth))
		res = urllib2.urlopen(req).read()
		return self.formatResult(res)

	def formatResult(self,res):
		try:
			json_res = json.loads(res)
		except Exception,e:
			return res
		return json_res

	def getAuthHeader(self,auth):
		base64string = base64.encodestring('%s:%s' % ( str(auth['username']), str(auth['password']) ))[:-1]
		authheader = "Basic %s" % base64string
		return authheader

