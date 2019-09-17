#coding:utf-8
import HTMLTestRunner
import os
import time
import unittest

import sys

sys.path.append('e:/project/Interface_api-master')

# from case.test_view import TestView
# from case.test_job import TestJob
from case.BMS.get_AOI_QuantityData import getAddrByCityCodeAndAddr
from case.BMS.getNormAndSbCountByCityCode import getNormAndSbCountByCityCode




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(getAddrByCityCodeAndAddr))
    suite.addTest(unittest.makeSuite(getNormAndSbCountByCityCode))





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


