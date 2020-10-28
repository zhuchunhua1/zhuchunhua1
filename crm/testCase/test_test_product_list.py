import unittest
from common.configHttp import RequestMethod
from common.login_info import login_info

class ProductManagementtList(unittest.TestCase):
    
    def setUp(self):
        self.base_url = "https://demo10.72crm.com/api/crmProduct/queryPageList"
        self.headers = {'Content-Type':'application/json;charset=UTF-8','Admin-Token':'{}'.format(login_info())}
        self.data = {"page":1,"limit":15,"search":"","type":4}
        self.response = {"code": 0,"msg":"success"}

    def tearDown(self):
        print(self.req_result)

    def test_productlist(self):
        self.req_result = RequestMethod().post(self.base_url, self.data, self.headers).json()
        print("111",self.req_result)
        self.assertEqual(self.response["code"],self.req_result["code"])
        self.assertEqual(self.response["msg"],self.req_result["msg"])

if __name__ == "__main__":
    unittest.main()
