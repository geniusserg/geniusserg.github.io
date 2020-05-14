import test_entry as template #TODO delete
import time
from selenium.webdriver.common.keys import Keys

#title should be CarConfigurator
class TestMain(template.TestTemplate):
    def __init__(self, *args, **kwargs):
        super(TestMain, self).__init__(*args, **kwargs)

#title CArConfigurator
    def test_case_1(self):
        self.description = "title should be CarConfigurator"
        title = self.driver.title
        self.assertEqual(title, "CarConfigurator")

#DiscountValue form should be 0 by default
    def test_case_2(self):
        self.description = "DiscountValue form should be 0 by default"
        input_discount = self.driver.find_element_by_id("DiscountValue_input")
        self.assertEqual(input_discount.get_attribute("value"), '0')

#When we click on VehicleTable, Base Price field should change
    def test_case_3(self):
        self.description = "When we click on VehicleTable, Base Price field doesnt change"
        table = self.driver.find_element_by_id("VehicleTable").find_element_by_tag_name("tbody").find_elements_by_class_name("dataRow")
        for i in range(1,len(table)):
            table[i].click()
            table = self.driver.find_element_by_id("VehicleTable").find_element_by_tag_name(
                "tbody").find_elements_by_class_name("dataRow")
            desired_value = table[i].find_elements_by_class_name("dataCell")[1].text.split(" ")[0]
            real_value = self.driver.find_element_by_id("BasePrice_input").text
            self.assertEqual(desired_value, real_value)

#Price is correctly changed when discount is changing
    def test_case_4(self):
        self.description = "Price is not correctly changed when discount is changing"
        price = self.driver.find_element_by_id("DiscountValue_input")
        price.send_keys("5")
        table = self.driver.find_element_by_id("VehicleTable").find_element_by_tag_name(
            "tbody").find_elements_by_class_name("dataRow")
        table[1].click()
        old_value = self.driver.find_element_by_id("BasePrice_input").text
        new_value = self.driver.find_element_by_id("CalculatedPrice_input").text
        old_value = float(old_value.split(" ")[0].replace(',', ''))
        new_value = float(new_value.split(" ")[0].replace(',', ''))
        self.assertAlmostEqual((old_value/100)*95, new_value)

#When incorrect data entered error dialog is displayed
    def test_case_5(self):
        self.description = "When value > 100 or < 0 entered error dialog is not displayed"
        price = self.driver.find_element_by_id("DiscountValue_input")
        price.send_keys("120")
        self.errorDialogInput()
        price.send_keys("-")
        self.errorDialogInput()

#When incorrect data entered error dialog is displayed
    def test_case_6(self):
        self.description = "When value string is entered error dialog is not displayed"
        price = self.driver.find_element_by_id("DiscountValue_input")
        price.send_keys("Qwe")
        self.errorDialogInput()
        price.send_keys("*")
        self.errorDialogInput()