#coding:utf-8
import os,shutil,time
import unittest
import HTMLTestRunner
# from case.test_view import TestView
# from case.test_job import TestJob
from case.test_userinfo import TestUserinfo

if __name__ == '__main__':
	suite = unittest.TestSuite()
	# suite.addTest(unittest.makeSuite(TestView))
	# suite.addTest(unittest.makeSuite(TestJob))
	suite.addTest(unittest.makeSuite(TestUserinfo))
    #
	# if(os.path.exists(os.path.dirname(__file__) + '/test-reports')):
	# 	shutil.rmtree(os.path.dirname(__file__) + '/test-reports')
	# runner = xmlrunner.XMLTestRunner(output='test-reports')
	now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
	file=os.path.dirname(__file__) + '/'+now+'test-reports.html'


	fp = open(file, 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title=u'测试报告',
		description=u'用例执行情况：',
		verbosity = 1)
	runner1 = unittest.TextTestRunner(verbosity = 1)
	runner.run(suite)
	fp.close()

