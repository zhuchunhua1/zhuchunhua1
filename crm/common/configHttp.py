import json
import requests

"""
封装接口请求的请求方式post/get，将url、data、headers参数化，
不同接口在请求post/get方式的接口时，
可根据接口请求类型调用configHttp.py中RequestMethod类下的方法：get、post,
每次请求调用时，都只需要传入三个变量：url、data、headers
"""

class RequestMethod:
    """定义请求类型"""

    def __init__(self):
        """初始化参数"""
        self.data = {}
        self.files = {}

    def get(self, url, data, headers):
        """定义get请求"""
        try:
            return requests.get(url= url, data= data, headers= headers, dtimeout= 60)
        except TimeoutError:
            return print('%s get request timeout!' % url)

    def post(self, url,data, headers):
        """定义post请求"""
        try:
            return requests.post(url= url, data=json.dumps(data), headers= headers, timeout= 60)
        except TimeoutError:
            return print('%s get request timeout!' % url)