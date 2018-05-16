#coding:utf-8
import HTMLTestRunner
import os
import time
import unittest

import sys

sys.path.append('e:/project/Interface_api-master')

# from case.test_view import TestView
# from case.test_job import TestJob
from case.rgeo.gis_rgeo import gis_rgeo
from case.rgeo.gis_rgeo2 import gis_rgeo2
from case.rgeo.rgeo_21 import rgeo_1
from case.rgeo.slow import rgeo_5



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(gis_rgeo))
    suite.addTest(unittest.makeSuite(gis_rgeo2))
    suite.addTest(unittest.makeSuite(rgeo_1))
    suite.addTest(unittest.makeSuite(rgeo_5))




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


