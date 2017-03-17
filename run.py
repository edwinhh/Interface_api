#coding:utf-8
import os,shutil
import unittest
import xmlrunner
from case.test_view import TestView
from case.test_job import TestJob
from case.test_userinfo import TestUserinfo

if __name__ == '__main__':
	suite = unittest.TestSuite()
	# suite.addTest(unittest.makeSuite(TestView))
	# suite.addTest(unittest.makeSuite(TestJob))
	suite.addTest(unittest.makeSuite(TestUserinfo))

	if(os.path.exists(os.path.dirname(__file__) + '/test-reports')):
		shutil.rmtree(os.path.dirname(__file__) + '/test-reports')
	runner = xmlrunner.XMLTestRunner(output='test-reports',verbose = 1)
	#runner = unittest.TextTestRunner(verbosity = 1)
	runner.run(suite)

