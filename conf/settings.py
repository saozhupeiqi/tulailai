import os

BATH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目路径
TESTCASE_PATH = os.path.join(BATH_PATH, 'test_case')  # 指定测试用例目录
TESTREPORT_PATH = os.path.join(BATH_PATH, 'report/')  # 指定测试报告路径
LOG_PATH = os.path.join(BATH_PATH, 'log/log.txt')  # 指定日志路径
DATA_PATH = os.path.join(BATH_PATH, 'data')  # 指定测试数据路径
# 项目环境
host_info = {
    'test': 'http://127.0.0.1',
    'dev': 'http://127.0.0.1',
    'preProduc': 'http://127.0.0.1'
}

# 当前sheet名
Sheet = 'Sheet01'
# sheet名及索引
Sheet_INFO = {
    'Sheet': 0
}
# project
PROJECT_IP = '127.0.0.1:9999'

# MySQL数据库连接信息
MySQL_Host = ''
MySQL_Port = 3806
MySQL_DB_USER = 'root'
MySQL_DB_PASSWORD = '123456'
MySQL_DB_NAME = 'mysql'
# redis连接信息
redis_port = '127.0.0.1'
redis_port = 6379
redis_DB = 0
redis_passwprd = 'test123456'
# 参数替换，获取key
PATTERN = '\$\{(.*?)\}'
