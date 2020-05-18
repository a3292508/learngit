#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

        cls.driver.get('http://13.haowu.com/hoss-web/hoss-v2/app/account/login.html')
        cls.driver.maximize_window()
        cls.driver.find_element_by_xpath('//*[@id="username"]').send_keys('18818255073')
        cls.driver.find_element_by_xpath('//*[@id="password"]').send_keys('111111')
        cls.driver.find_element_by_xpath('//*[@id="loginForm"]/input[3]').click()

    def setUp(self):
        pass

    def test_login(self):
        for i in range(1,100):
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//li[@class="clearfix"]/div/a')))
            self.driver.find_elements_by_xpath('//li[@class="clearfix"]/div/a')[0].click()
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="submit"]')))
            self.driver.find_element_by_xpath('//*[@id="submit"]').click()

            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()




# learngit
