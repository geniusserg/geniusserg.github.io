import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestTemplate(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_case_1(self):
        self.driver.get('https://localhost:8080')
        title = self.driver.title
        self.assertEqual(title, 'CarConfiguration')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
