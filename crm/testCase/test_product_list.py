import unittest
import requests
from ddt import ddt, data, file_data, unpack
from common.configHttp import RequestMethod
from common.login_info import login_info



"""
产品列表查询
"""

@ddt
class ProductManagementtList(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://demo10.72crm.com/api/crmProduct/queryPageList"
        self.headers = {'Content-Type':'application/json;charset=UTF-8','Admin-Token':'{}'.format(login_info())}

    def tearDown(self):
        print(self.req_result)

    @file_data('data/productlist.json')
    def test_productlist(self,name,data,response):
        self.req_result = RequestMethod().post(self.base_url, data, self.headers).json()
        print("111",self.req_result)
        
        self.assertEqual(self.req_result["code"],response["code"])
        self.assertEqual(self.req_result["msg"],response["msg"])

if __name__ == "__main__":
    unittest.main()
