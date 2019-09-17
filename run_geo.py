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
from case.geo.geo_opt import geo_opt
from case.geo.geo_sz import geo_sz
from case.geo.geo_sw import geo_sw
from case.geo.geo_gf import geo_gf
from case.geo.geo_yy import geo_yy
from case.geo.geo_sf import geo_sf
from case.geo.geo_bd import geo_bd
from case.geo.geo_tc import geo_tc
from case.geo.geo_ts import geo_ts
from case.geo.v1_22 import v1_22
from case.geo.v1_23 import v1_23
from case.geo.v1_8 import v1_8
from case.geo.yy import yy
from case.geo.geo_cx import geo_cx
from case.geo.geo_core import geo_core
from case.geo.v2_0 import v2_0
from case.geo.v2_1 import v2_1
from case.geo.v2_5 import v2_5
from case.geo.v2_7 import v2_7
from case.geo.v3_7 import v3_7
from case.geo.v4_01 import v4_01
from case.geo.v4_02 import v4_02
from case.geo.v4_20 import v4_20
from case.geo.sy import sy
from case.geo.mc import mc
from case.geo.mc2 import mc2
from case.geo.mc3 import mc3
from case.geo.rh import rh
from case.geo.v5_01 import v5_01

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(geo_opt))
    suite.addTest(unittest.makeSuite(geo_sw))
    suite.addTest(unittest.makeSuite(geo_gf))
    suite.addTest(unittest.makeSuite(geo_yy))
    suite.addTest(unittest.makeSuite(geo_sf))
    suite.addTest(unittest.makeSuite(geo_bd))
    suite.addTest(unittest.makeSuite(geo_tc))
    suite.addTest(unittest.makeSuite(geo_ts))
    suite.addTest(unittest.makeSuite(yy))
    suite.addTest(unittest.makeSuite(geo_cx))
    suite.addTest(unittest.makeSuite(geo_core))
    suite.addTest(unittest.makeSuite(gis_geo))
    suite.addTest(unittest.makeSuite(v2_0))
    suite.addTest(unittest.makeSuite(v2_1))
    suite.addTest(unittest.makeSuite(v2_5))
    suite.addTest(unittest.makeSuite(v4_01))
    suite.addTest(unittest.makeSuite(v4_02))
    suite.addTest(unittest.makeSuite(v4_20))
    suite.addTest(unittest.makeSuite(v5_01))
    suite.addTest(unittest.makeSuite(rh))
    suite.addTest(unittest.makeSuite(mc))
    suite.addTest(unittest.makeSuite(mc2))
    suite.addTest(unittest.makeSuite(mc3))
    suite.addTest(unittest.makeSuite(sy))
    
 





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


