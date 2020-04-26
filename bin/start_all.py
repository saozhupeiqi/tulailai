# -*- coding: utf-8 -*-
import os
import sys
# 把path加入环境变量，0表示在最前面
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from conf.settings import TESTCASE_PATH
from conf.settings import TESTREPORT_PATH
import unittest
from lib.HTMLTestReportCN import HTMLTestRunner as hr1
from lib.HTMLTestReportCN import HTMLTestRunner as hr2
import time
suit = unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern='test_*.py')
print(suit)
if __name__ == "__main__":
    now = time.strftime("%Y-%M-%D-%H-%M-%S")#获取当前时间，并指定输出格式
    #创建报告文件
    fp = open(TESTREPORT_PATH+'_report_all.html', 'wb')

    runner = hr2(
        stream=fp,
        title=u'赖韵的测试报告',
        description=u'测试报告可以访问服务器查看，地址：http://101.201.146.42:8081/',
        tester=u"赖韵")
    runner.run(suit)
    fp.close()







