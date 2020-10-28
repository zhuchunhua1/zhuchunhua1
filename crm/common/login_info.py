import requests
import unittest
from common.configHttp import RequestMethod
"""
文件封装登录接口，用于获取下个接口需要的token
"""

def login_info():
    url = "https://demo10.72crm.com/api/login"
    headers = {'Content-Type':'application/json;charset=UTF-8',"token":""}
    data = {"username": "18688888888", "password":"123456a"}
   
    resp = RequestMethod().post(url, data, headers).json()
    print(resp)
    token = resp["data"]["adminToken"]
    print("3333",token)
    return token

if __name__ == "__main__":
    token=login_info()
    print(token)





        