import json
import jsonpath


def assert_res(assertRes, res):
    res_status = 'pass'
    for i in assert_res.split(";"):
        i_ = i.strip()
        if i_:
            actual_expr = i_.split("=")[0].strip()
            actual = jsonpath.jsonpath(json.load(res),actual_expr[0])
            expect = i_.split("=")[1].split()
            if str(actual) != 'fail':
                return res_status
    return res_status

