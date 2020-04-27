import sys,os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import requests
import unittest
from lib import HTMLTestRunner
from lib.tools import p
from lib import logger
from conf.settings import PROJECT_IP
from conf.settings import PROJECT_PORT


class AddUser(unittest.TestCase):
    def setUp(self):
        print('...测试用例开始执行...')
        self.url = 'http://' + PROJECT_IP + ':' + PROJECT_PORT + '/add_user4'
        # 获取token
        from lib import login_token
        self.token = login_token.get_token('qzcsbj', '123456')
        print(self.token)
        self.headers = {'content-type': 'application/json'}

    def tearDown(self):
        print('...测试用例执行完毕...')

    def test_add_user_ok(self):
        """添加成功"""
        logger.logger.logger.debug('当前方法【%s】:' % p.get_current_function_name())
        payload = {"token": self.token,
                   "username": "test133",
                   "realname": "test133",
                   "sex": "1",
                   "phone": "17781780161",
                   "adduser": "qzcsbj"}
        try:
            res = requests.post(url=self.url, params=payload, headers=self.headers).json()
        except Exception as e:
            res = {
                'code': '999',
                'msg': '连接错误'
            }
        logger.logger.logger.debug('是测试点【%s】下用例【%s:%s】,返回结果【%s】'
                                   %(self.__class__.__name__,
                                     getattr(self,p.get_current_function_name()).__doc__,
                                     p.get_current_function_name(),res))
        self.assertEqual(res['code'],9550)

    def test_add_user_exist(self):
        """手机号已存在"""
        payload = {"token": self.token,
                   "username": "test13",
                   "realname": "test130",
                   "sex": "1",
                   "phone": "17781780161",
                   "adduser": "qzcsbj"}
        try:
            res = requests.post(url=self.url, params=payload, headers=self.headers).json()
        except Exception as e:
            res = {
                'code':'999',
                'msg':'连接错误'
            }
        logger.logger.logger.debug('是测试点【%s】下用例【%s:%s】,返回结果【%s】'
                                   % (self.__class__.__name__,
                                      getattr(self, p.get_current_function_name()).__doc__,
                                      p.get_current_function_name(), res))
        self.assertEqual(res['code'], 9360)

    def test_add_user_no_phone(self):
        """手机号为空"""
        payload = {"token": self.token, "username": "test131", "realname": "test131", "sex": "1",
                   "phone": " ", "adduser": "qzcsbj"}
        try:
            res = requests.post(url=self.url, params=payload, headers=self.headers).json()
        except Exception as e:
            res = {
                'code': '999',
                'msg': '连接错误'
            }
        self.assertEqual(res['code'], 9500)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(AddUser('test_add_user_ok'))
    suit.addTest(AddUser('test_add_user_exist'))
    suit.addTest(AddUser('test_add_user_no_phone'))
    fp = open('./report_debug.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'接口测试报告', description=u'接口测试报告')
    runner.run(suit)
    fp.close()

