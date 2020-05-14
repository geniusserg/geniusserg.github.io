import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
import time
import os

class TestTemplate(unittest.TestCase):
    driver = None

    def __init__(self, *args, **kwargs):
        super(TestTemplate, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver_path = ""
        if os.name == 'posix':
            driver_path = "/opt/chrome_driver/chromedriver"
        else:
            driver_path = "C:\\java\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
        self.driver.implicitly_wait(10)
        resource = ""
        if os.name == 'posix':
            resource = 'http://localhost:8080/' #for CI
        else:
            resource = 'http://geniusserg.github.io/' #for developing
        self.driver.get(resource)
        self.driver.implicitly_wait(3)
        self.initDialogs()



    def initDialogs(self):
        dialogs = self.driver.find_elements_by_tag_name("div")
        self.dialogs = {}
        for i in dialogs:
            if i.get_attribute("aria-labelledby") == "ui-dialog-title-IlligalInput":
                self.dialogs['errorInput'] = i

    def errorDialogInput(self):
        error_dialog = self.dialogs['errorInput']
        self.assertTrue(error_dialog.is_displayed())
        error_dialog.find_element_by_tag_name("button").click()
        self.assertFalse(error_dialog.is_displayed())


