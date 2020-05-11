import unittest
from Selenium import webdriver
import time

class TestBrowserOpen(unittest.TestCase):
    def test_a(self):
        driver = webdriver.Remote()
        driver.maximize_window()
        driver.get("https://localhost:80")
        title = driver.title()
        print(title)
        time.sleep(3)
        driver.close()
        
if __name__ == '__main__':
    unittest.main()
