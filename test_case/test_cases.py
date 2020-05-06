import unittest
import requests
from ddt import *
from conf.settings import SHEET_NAME
from lib.parameter_substitution import parameter_substitution
from lib.global_variables import gv
from lib.assert_res import assert_res
from lib.read_excel import read_excel
from lib.logger import logger
from lib import HTMLTestRunner


@ddt
class MyRequest(unittest.TestCase):
    test_datas = read_excel(SHEET_NAME)

    @data(*test_datas)
    @unpack
    def test_my_request(self, project, module, case_id, case_name, description, url, method, headers, cookies, params,
                        body, file, init_sql, globalVariable, assertRes, request, actualResults, result, tester):
        """请求"""
        logger.logger.debug("======【当前执行的用例是：%s:%s】======" % (case_id, case_name))
        # url,headers,cookies,params,body做参数化
        url = parameter_substitution(url)
        headers = parameter_substitution(headers)
        cookies = parameter_substitution(cookies)
        params = parameter_substitution(params)
        body = parameter_substitution(body)
        logger.logger.debug(">>>请求的method是:%s" % method)
        logger.logger.debug(">>>请求的url是:%s" % url)
        logger.logger.debug(">>>请求的headers是：%s" % headers)
        logger.logger.debug(">>>请求的cookies是：%s" % cookies)
        logger.logger.debug(">>>请求的params是：%s" % params)
        logger.logger.debug(">>>请求的body是：%s" % body)
        logger.logger.debug(">>>断言的内容是是：%s" % assertRes)
        # 转化
        headers_ = eval(headers) if headers else headers
        cookies_ = eval(cookies) if cookies else cookies
        params_ = eval(params) if params else params
        body_ = eval(body) if body else body

        if init_sql:
            pass
        if method.upper() == 'GET':
            try:
                res = request.get(url=url, headers=headers_, cookies=cookies_,params=params_, timeout=10)
                logger.logger.debug("执行请求后，结果是：%s" % res.text)
                # 如果有需要被后续请求用的变量
                if globalVariable:
                    gv.save_global_variable(globalVariable,res.text)

                # 断言
                if assertRes:
                    res_status = assert_res(assertRes, res.text)
                    logger.logger.debug("断言结果是：%s\n\n" % res.text )
                    gv.res.append([res.text,url,headers,cookies,body,res_status])
                    self.assertEqual(res_status, 'pass')

            except Exception as e:
                print('出错了 %s' %e)
                raise e

        if method.upper == 'POST':
            """执行请求"""
            try:
                res = request.post(url=url, headers=headers_,cookies=cookies_,params=params_,json=body_,timeout=10)
                logger.logger.debug("执行请求后结果是：%s" %res.text)
                if globalVariable:
                    gv.save_global_variable(globalVariable,res.text)

                if assertRes:
                    res_status = assert_res(assertRes,res.text)
                    logger.logger.debug("断言结果是：%s" %res_status)
                    gv.res.append([res.text, url,headers, cookies, params, body, res_status])
                    self.assertEqual(res_status, 'pass')
            except Exception as e:
                print('出错了 %s' % e)
                raise e


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(MyRequest('test_my-request'))
    fp = open('./report_debug.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'自动化测试报告')
    runner.run(suit)
    fp.close()