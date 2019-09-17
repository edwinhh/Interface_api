#coding:utf-8
import HTMLTestRunner
import os
import time
import unittest

import sys

sys.path.append('e:/project/Interface_api-master')

# from case.test_view import TestView
# from case.test_job import TestJob
from case.tip.tip_13341 import tip_13341
from case.tip.tip_13342 import tip_13342
from case.tip.tip_13343 import tip_13343
from case.tip.tip_13344 import tip_13344
from case.tip.tip_13345 import tip_13345
from case.tip.tip_13346 import tip_13346
from case.tip.tip_13347 import tip_13347
from case.tip.tip_13348 import tip_13348
from case.tip.v1_23 import tip1_23
from case.tip.v1_18 import tip1_18
from case.tip.v1_25 import v_125
from case.tip.v1_26 import v_126
from case.tip.v1_26_post import v_128
from case.tip.gis_tip import tip
from case.tip.gis_tip2 import tip2
from case.tip.tip_1 import tip_1
from case.tip.tip_2 import tip_2
from case.tip.tip_3 import tip_3
from case.tip.tip_4 import tip_4
from case.tip.tip_5 import tip_5
from case.tip.tip_6 import tip_6
from case.tip.tip_7 import tip_7
from case.tip.tip_8 import tip_8


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(tip_13341))
    suite.addTest(unittest.makeSuite(tip_13342))
    suite.addTest(unittest.makeSuite(tip_13343))
    suite.addTest(unittest.makeSuite(tip_13344))
    suite.addTest(unittest.makeSuite(tip_13345))
    suite.addTest(unittest.makeSuite(tip_13346))
    suite.addTest(unittest.makeSuite(tip_13347))
    suite.addTest(unittest.makeSuite(tip_13348))
    suite.addTest(unittest.makeSuite(tip))
    suite.addTest(unittest.makeSuite(tip2))
    suite.addTest(unittest.makeSuite(tip1_18))
    suite.addTest(unittest.makeSuite(tip1_23))
    suite.addTest(unittest.makeSuite(v_125))
    suite.addTest(unittest.makeSuite(v_126))
    suite.addTest(unittest.makeSuite(v_128))
    suite.addTest(unittest.makeSuite(tip_1))
    suite.addTest(unittest.makeSuite(tip_2))
    suite.addTest(unittest.makeSuite(tip_3))
    suite.addTest(unittest.makeSuite(tip_4))
    suite.addTest(unittest.makeSuite(tip_5))
    suite.addTest(unittest.makeSuite(tip_6))
    suite.addTest(unittest.makeSuite(tip_7))
    suite.addTest(unittest.makeSuite(tip_8))



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


