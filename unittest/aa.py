# -*- coding: utf-8 -*-

from selenium import webdriver
from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest

class Aa(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.baidu.com/"
    
    def test_aa(self):
        self.setUp()
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("huilan")
        driver.find_element_by_id("su").click()
        driver.find_element_by_id("su").click()
        self.tearDown()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    report = './report/report.html'
    with open(report, 'wb')as f:
        runner = HTMLTestRunner(stream=f,
                                title='数学计算方法的测试',
                                description='执行人：FeiXCMeng',
                                verbosity=2
                                )

        runner.run(Aa('test_aa'))