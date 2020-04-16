import os
BATH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#项目路径
TESTCASE_PATH = os.path.join(BATH_PATH,'test_case')#指定测试用例目录
TESTREPORT_PATH = os.path.join(BATH_PATH,'report/')#指定测试报告路径
LOG_PATH = os.path.join(BATH_PATH,'log\log.txt')#指定日志路径
DATA_PATH = os.path.join(BATH_PATH,'data')#指定测试数据路径
#project
PROJECT_IP = '127.0.0.1'
PROJECT_PORT = 9999





