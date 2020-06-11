import time
import unittest

import outcome
from selenium import webdriver
import json
import os

class TestTemplate(unittest.TestCase):
    driver = None

    def __init__(self, *args, **kwargs):
        super(TestTemplate, self).__init__(*args, **kwargs)
        self._outcome = outcome
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
            resource = 'http://geniusserg.github.io/' #for CD
        self.driver.get(resource)
        self.driver.implicitly_wait(3)
        self.initDialogs()
        self.initTestingData()
        self.initLog()


    def initDialogs(self):
        dialogs = self.driver.find_elements_by_tag_name("div")
        self.dialogs = {}
        for i in dialogs:
            if i.get_attribute("aria-labelledby") == "ui-dialog-title-IlligalInput":
                self.dialogs['errorInput'] = i

    def initTestingData(self):
        json_data = open('data.json')
        self.testing_data = json.load(json_data)

    def errorDialogInput(self, case):
        error_dialog = self.dialogs['errorInput']
        if case:
            self.assertTrue(error_dialog.is_displayed())
        else:
            self.assertFalse(error_dialog.is_displayed())
        error_dialog.find_element_by_tag_name("button").click()
        if not case:
            self.assertTrue(error_dialog.is_displayed())
        else:
            self.assertFalse(error_dialog.is_displayed())


    def initLog(self):
        log = open("test.log" ,"w")
        log.write("UNIT TESTING CAR CONFIG\n")
        log.write(str(time.ctime(time.time()))+"\n")
        log.write(str(self.countTestCases())+" cases \n")
        log.write("TEST SITE: "+self.driver.current_url+"\n")
        log.write("TEST DRIVER: " + self.driver.name + "\n")
        log.write("TEST DATA SET: data.json\n")
        log.write("::::::::::RESULT::::::::\n")
        log.close()
