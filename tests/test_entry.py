import unittest
from selenium import webdriver
import time


class TestTemplate(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
         chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path="/opt/chrome_driver/chromedriver", chrome_options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost:8080')
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()


