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

    def test_login_ok(self):
        '''登陆成功'''
        print('test_user_login_ok:',str(id(self)))
        logger.logger.logger.debug('当前方法：%s'% p.get_current_function_name())
        params = {
            "username":'laiyun',
            "password":'123456'}#请求参数
        try:
            #传表单
            res = requests.post(url=self.url,params=params,verify=False,timeout=10).json()
        except Exception as e:
            res = {
                'code':'999',
                'msg':'连接错误'
            }
        logger.logger.logger.debug(
                '是测试点【%s】下的用例【%s:%s】,返回结果【%s】'
                %(self.__class__.__name__),getattr(self,p.get_current_function_name()).__doc__,
                p.get_current_function_name(),res
            )
        self.assertEqual(res['code'],9420)

    def test_user_login_fail(self):
        '''用户名或密码错误'''
        print('test user login fail:',str(id(self)))
        params = {
            "username":'laiyun',
            "password":'1234567'
        }
        try:
            res = requests.post(url=self.url,params=params,verify=False,timeout=10).json()
        except Exception as e:
            res = {
                'code':'999',
                'msg':'连接错误'
            }
        logger.logger.logger.debug('是测试点【%s】下的用例【%s:%s】,返回结果【%s】'
                                   %(self.__class__.__name__),getattr(self,p.get_current_function_name()).__doc__,
                                   p.get_current_function_name().res)
        self.assertEqual(res['code'],9410)

        def test_user_login_no_hone(self):
            '''未填写用户名'''
            print('test user login no phone',str(id(self)))
            params = {
                "username":'',
                "password":'123456'
            }
            try:
                res = requests.post(url=self.url,params=params,verify=False,timeout=10).json()
            except Exception as e:
                res = {
                    'code':'999',
                    'msg':'连接失败'
                }
            logger.logger.logger.debug('是测试用例【%s】下的用例【%s:%s】,返回结果【%s】'
                                       %(self.__class__.__name__),
                                       getattr(self,p.get_current_function_name().__doc__,
                                               p.get_current_function_name(),res))
            self.assertEqual('res[code]',9400)

if __name__ == '__main__':
    suit = unittest.TestSuite()#测试套件
    suit.addTest(UserLogin('test_login_ok'))#将登录情况加入测试套件,登陆成功
    suit.addTest(UserLogin('test_user_login_no_phone'))#登录失败
    suit.addTest(UserLogin('test_user_login_no_phone'))#未填写用户名
    fp = open('./report_debug.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告debug',description=u'自动化项目测试报告')
    runner.run(suit)
    fp.close()







