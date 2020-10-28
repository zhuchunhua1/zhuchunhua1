import unittest
import requests


class login(unittest.TestCase):
    
    def setUp(self):
            self.base_url = "https://demo10.72crm.com/api/login"
            self.data = {"username": "18688888888", "password":"123456a"}
            
    def tearDown(self):
        print(self.ret)
    
    def test_case(self):
        r = requests.post(self.base_url,  json= self.data)
        self.ret = r.json()
        #self.assertEqual(self.ret["code"], code)
        #self.assertEqual(self.ret["message"], msg)

if __name__ == "__main__":
    unittest.main()