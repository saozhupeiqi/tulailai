import sys,os
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.insert(0, path)
import requests
import unittest
from lib import HTMLTestRunner


class UserReg(unittest.TestCase):
    def setUp(self):
        print('...测试用例开始执行...')

    def tearDown(self):
        print('...测试用例执行完成...')

    def test_user_reg_ok(self):
        """注册成功"""
        pass

    def test_user_reg_exsit(self):
        """用户已存在 """
        pass

    def test_user_reg_no_phone(self):
        """手机号为空"""


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(UserReg('test_user_reg_ok'))
    suit.addTest(UserReg('test_user_reg_exsit'))
    suit.addTest(UserReg('test_user_reg_no_phone'))
    fp = open('/report_debug.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试项目报告',description=u'自动化测试项目报告')
    runner.run(suit)
    fp.close()



