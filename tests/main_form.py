import tests.test_entry as template
import unittest


class TestMain(template.TestTemplate):
    def test_title(self):
        title = self.driver.title
        self.assertEqual(title, "WebCarConfigurator")

    def test_case_2(self):
        
