#coding: utf-8

import unittest,HTMLTestRunner

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testName(self):
        self.assertEquals(3,1)



    def testName1(self):
        self.assertEquals(1,1)

    def testName2(self):
        self.assertEquals(2,2)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestView))
    # suite.addTest(unittest.makeSuite(TestJob))
    suite.addTest(unittest.makeSuite(Test))
    filename = 'd:\\myreport.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, title='my unit test', description='This is a report test')
    runner.run(suite)
    fp.close()