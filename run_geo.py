#coding:utf-8
import HTMLTestRunner
import os
import time
import unittest

import sys

sys.path.append('e:/project/Interface_api-master')

# from case.test_view import TestView
# from case.test_job import TestJob
from case.geo.gis_geo import gis_geo
from case.tip.gis_tip import tip
from case.tip.v1_18 import tip1_18
from case.tip.v1_25 import v_125
from case.geo.geo_opt import geo_opt
from case.geo.geo_sz import geo_sz
from case.geo.geo_sw import geo_sw
from case.geo.geo_gf import geo_gf
from case.geo.geo_yy import geo_yy
from case.geo.geo_gd import geo_gd
from case.geo.geo_bd import geo_bd
from case.geo.geo_tc import geo_tc
from case.geo.v1_22 import v1_22
from case.geo.v1_23 import v1_23
from case.geo.v1_8 import v1_8
from case.geo.yy import yy
from case.geo.geo_cx1 import geo_cx
from case.geo.geo_core import geo_core
from case.geo.v2_0 import v2_0
from case.geo.v2_1 import v2_1


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(v1_8))
    suite.addTest(unittest.makeSuite(geo_opt))
    suite.addTest(unittest.makeSuite(geo_sz))
    suite.addTest(unittest.makeSuite(geo_sw))
    suite.addTest(unittest.makeSuite(geo_gf))
    suite.addTest(unittest.makeSuite(geo_yy))
    suite.addTest(unittest.makeSuite(geo_gd))
    suite.addTest(unittest.makeSuite(geo_bd))
    suite.addTest(unittest.makeSuite(geo_tc))
    suite.addTest(unittest.makeSuite(v1_22))
    suite.addTest(unittest.makeSuite(v1_23))
    suite.addTest(unittest.makeSuite(yy))
    suite.addTest(unittest.makeSuite(geo_cx))
    suite.addTest(unittest.makeSuite(geo_core))
    suite.addTest(unittest.makeSuite(gis_geo))
    suite.addTest(unittest.makeSuite(v2_0))
    suite.addTest(unittest.makeSuite(v2_1))




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


