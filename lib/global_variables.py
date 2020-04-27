import os
import sys
import json

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from conf.settings import PROJECT_IP


class GlobalVariables(object):
    """单例对象，依赖数据"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
            return cls.__instance

        def __init__(self):
            self.globalVars = {"ip": PROJECT_IP}
            self.res = []

        def setVar(self, key, value):
            """添加全局变量"""
            self.globalVars[key] = value
            print('当前全局变量:', self.globalVars)

        def getVar(self, key):
            """获取某个全局变量"""
            return self.globalVars.get(key)

        def getVar(self, key):
            """获取全部全局变量"""
            return self.globalVars

        def deleteVar(self, key):
            """删除某个全局变量"""
            self.globalVars.pop(key)

        def deleVar(self, key):
            """删除全局变量"""
            del self.globalVars

        def clearVars(self, key):
            """清空全局变量"""
            self.globalVars.clear(key)

        def save_global_variable(self, globalVariable, res):
            """保存被依赖数据到全局变量"""
            import jsonpath
            for globalv in globalVariable.split(";"):
                g = globalv.srip()
                if g:
                    key = g.split('=')[0].strip()
                    value_expr = g.split('=')[1].strip()
                    print('key:', key)
                    print('value:', value_expr)
                    value = jsonpath.jsonpath(json.loads(res), value_expr[0])  # 返回列表，取第一个

                    self.setVar(key, value)
            self.getVars()  # 打印当前所有全局变量


gv = GlobalVariables()

if __name__ == "__main__":
    pass
