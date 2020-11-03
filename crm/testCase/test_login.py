import unittest
import requests
from common.configHttp import RequestMethod
from ddt import ddt, data, file_data, unpack


"""
登陆
"""
@ddt
class login(unittest.TestCase):
    
    def setUp(self):
            self.base_url = "https://demo10.72crm.com/api/login"
            self.headers = {'Content-Type':'application/json;charset=UTF-8'}
                      
    def tearDown(self):
        print(self.req_result)

    @file_data('data/login.json')
    def test_case(self, tile, data):
        self.req_result = RequestMethod().post(self.base_url, data, self.headers).json()
        if tile != "success" :
            try:
                self.assertIsNone(self.req_result["dta"])
            except KeyError:
                print("登陆失败")
                raise                
        else:
            try:
                self.assertIsNotNone(self.req_result["data"])
            except AssertionError:
                print("登陆成功")
                    
        
if __name__ == "__main__":
    unittest.main()