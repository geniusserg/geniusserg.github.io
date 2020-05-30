import test_entry as template #TODO delete
import time
from selenium.webdriver.common.keys import Keys

#title should be CarConfigurator
class TestMain(template.TestTemplate):
    def __init__(self, *args, **kwargs):
        super(TestMain, self).__init__(*args, **kwargs)

#All components are visible
    def test_case_1(self):
        self.description = "Not visible"
        table = self.driver.find_element_by_id("VehicleTable"). \
            find_element_by_tag_name("tbody")
        self.assertTrue(table.is_displayed())

#Components are visible
    def test_case_2(self):
        self.description = "Empty menu"
        table = self.driver.find_element_by_id("VehicleTable").\
            find_element_by_tag_name("tbody").\
            find_elements_by_class_name("dataRow")
        self.assertTrue(table != 0)

#When we click on VehicleTable, Base Price field should change
    def test_case_3(self):
        self.description = "When we click on VehicleTable," \
                           " Base Price field change"
        table = self.driver.find_element_by_id("VehicleTable").\
            find_element_by_tag_name("tbody").\
            find_elements_by_class_name("dataRow")
        for i in range(1,len(table)):
            table[i].click()
            table = self.driver.find_element_by_id("VehicleTable").\
                find_element_by_tag_name("tbody").\
                find_elements_by_class_name("dataRow")
            desired_value = table[i].find_elements_by_class_name("dataCell")[1]. \
            text.split(" ")[0]
            real_value = self.driver.find_element_by_id("BasePrice_input").text
            self.assertEqual(desired_value, real_value)

    # When incorrect data entered error dialog is displayed
    def test_case_4(self):
        self.description = "When value is ot correct, error dialog is not displayed"
        price = self.driver.find_element_by_id("DiscountValue_input")
        for case in self.test_data_discount['High']['F']:
            price.send_keys(case)
            self.errorDialogInput(True)

#Price is correctly changed when discount is changing
    def test_case_5(self):
        self.description = "Price is not correctly changed when discount is changing"
        price = self.driver.find_element_by_id("DiscountValue_input")
        for case in self.test_data_discount['High']['T']:
            price.send_keys(case)
            table = self.driver.find_element_by_id("VehicleTable").\
                find_element_by_tag_name("tbody").\
                find_elements_by_class_name("dataRow")
            table[1].click()
            old_value = self.driver.find_element_by_id("BasePrice_input").text
            new_value = self.driver.find_element_by_id("CalculatedPrice_input").text
            old_value = float(old_value.split(" ")[0].replace(',', ''))
            new_value = float(new_value.split(" ")[0].replace(',', ''))
            self.assertAlmostEqual((old_value/100)*(100-int(case)), new_value)

#+5 is correctly works
    def test_case_6(self):
        self.description = "+5% correctly works"
        discount = self.driver.find_element_by_id("DiscountValue_input")
        button_up = self.driver.find_elements_by_xpath("xpath=//div[@onclick='javascript: GrantDiscount();']")
        button_up.click()
        self.assertTrue(discount.get_property("value"), 5)
        for i in range(0,20):
            button_up.click()
        self.assertTrue(discount.get_property("value"), 99)
