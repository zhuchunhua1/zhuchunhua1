import time
import unittest
from HTMLTestRunner import HTMLTestRunner
#from db_fixture.test_data import init_data

# 初始化测试数据
#init_data()

suit = unittest.defaultTestLoader.discover(
    start_dir="./testCase",
    pattern="test_*.py"
)

now_time = time.strftime("%Y-%m-%d %H.%M.%S")

with open("./reports/"+now_time +".html", "wb") as f:
    runner = HTMLTestRunner(stream=f)
    runner.run(suit)

 # 发送邮件
    # time.sleep(5)  # 设置睡眠时间，等待测试报告生成完毕
    # email = sendEmail.SendEmail()
    # email.sendReport()  