import unittest
from BeautifulReport import BeautifulReport
from selenium import webdriver

class UnittestCaseSecond(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""
    
    def test_equal(self):
        """
            test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.assertTrue(1 == 1)
    def test_sample(self):
        browser = webdriver.Chrome()
        print("cooooooooooool")
        browser.get("http://www.baidu.com")
        browser.find_element_by_id("kw").send_keys("selenium")
        browser.find_element_by_id("su").click()
        browser.quit()
