from conf.settings import PROJECT_IP
from conf.settings import PROJECT_PORT
import requests


# noinspection PyBroadException
def get_token(username,password):
    url = 'http://' + PROJECT_IP + ':' + PROJECT_PORT + '/login'
    print(url)
    params = {"username":username,"password":password}
    try:
        res = requests.post(url=url,params=params,verify=False,timeout=10).json()
        if res['code'] == 9420:
            return res['token']
        else:
            return None

    except Exception as e:
        print('连接错误')
        return None


if __name__ == '__main__':
    get_token('qzcsbj','123456')