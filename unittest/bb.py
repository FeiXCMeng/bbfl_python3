# -*- coding:utf-8 -*-
from selenium import webdriver
# import unittest

# class BaiduTest(unittest.TestCase):
# 	def setUp(self):
# 		self.driver = webdriver.Chrome()
# 		self.base_url = "https://www.baidu.com/"

# 	def tearDown(self):
# 		self.driver.quit()

# 	def test_badiu(self):
# 		driver = self.driver
# 		driver.get(self.base_url)
# 		driver.find_element_by_id('kw').clear()
# 		driver.find_element_by_id('kw').send_keys('Selenium33333')
# 		driver.find_element_by_id('su').click()

# if __name__ == '__main__':
# 	unittest.main()
#####################################################################################
driver = webdriver.Chrome()
base_url = "https://www.baidu.com/"
driver.get(base_url)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('Selenium33333')
driver.find_element_by_id('su').click()