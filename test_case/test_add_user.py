import sys, os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.insert(0, path)
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
        self.token = login_token.get_token('qzcsbj','123456')
        print(self.token)
        self.headers = {'content-type':'application/json'}

    def tearDown(self):
        print('...测试用例执行完毕...')

