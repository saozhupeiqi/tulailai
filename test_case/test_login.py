import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,path)
import unittest
import requests
from lib import HTMLTestRunner
from lib import logger
from lib.tools import p
from conf.settings import PROJECT_PORT
from conf.settings import PROJECT_IP

class UserLogin(unittest.TestCase):
    def setUp(self):
        print('测试用例开始执行...self的id是',str(id(self)))
        self.url = 'http://' + PROJECT_IP + ':' + PROJECT_PORT + '/login'

    def tearDown(self):
        print('测试用例执行完成...')
