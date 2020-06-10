import outcome as outcome
from selenium.webdriver.common.alert import Alert
import unittest
import test_entry as template #TODO delete
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#title should be CarConfigurator
class TestMain(template.TestTemplate):
    currentResult=False
    def __init__(self, *args, **kwargs):
        super(TestMain, self).__init__(*args, **kwargs)

#All components are visible
    def test_case_1(self):
        table = self.driver.find_element_by_id("VehicleTable")
        self.assertTrue(table.is_displayed())
        switch = self.driver.find_element_by_xpath("//a[@id='TabbedPaneSpecialModel']")
        switch.click()
        table = self.driver.find_element_by_id("SpecialsCombo")
        table.click()
        self.assertTrue(table.is_displayed())
        switch = self.driver.find_element_by_xpath("//a[@id='TabbedPaneAccessory']")
        switch.click()
        table = self.driver.find_element_by_id("TabbedPaneAccessory")
        table.click()
        self.assertTrue(table.is_displayed())

#Components are visible
    def test_case_2(self):
        title = self.driver.title
        self.assertTrue(title == 'CarConfigurator')

#When we click on VehicleTable, Base Price field should change
    def test_case_3(self):
        self.description = "When we click on VehicleTable," \
                           " Base Price field change"
        table = self.driver.find_element_by_id("VehicleTable").\
            find_element_by_tag_name("tbody").\
            find_elements_by_class_name("dataRow")
        if len(table) == 1:
            self.assertFalse(True, "there are not any records in menue")
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
        price = self.driver.find_element_by_id("DiscountValue_input")
        for case in self.testing_data['case_4']['F']:
            price.clear()
            price.send_keys(case)
            self.errorDialogInput(True)

#Price is correctly changed when discount is changing
    def test_case_5(self):
        price = self.driver.find_element_by_id("DiscountValue_input")
        t = 1
        for case in self.testing_data['case_5']['T']:
            price.clear()
            price.send_keys(case)
            table = self.driver.find_element_by_id("VehicleTable").\
                find_element_by_tag_name("tbody").\
                find_elements_by_class_name("dataRow")
            table[t].click()
            t += 1
            old_value = self.driver.find_element_by_id("BasePrice_input").text
            new_value = self.driver.find_element_by_id("CalculatedPrice_input").text
            old_value = float(old_value.split(" ")[0].replace(',', ''))
            new_value = float(new_value.split(" ")[0].replace(',', ''))
            self.assertAlmostEqual((old_value/100)*(100-int(case)), new_value)

#+5 is correctly works
    def test_case_6(self):
        self.description = "+5% correctly works"
        discount = self.driver.find_element_by_id("DiscountValue_input")
        button_up = self.driver.find_element_by_xpath("//div[@onclick='javascript: GrantDiscount();']")
        button_up.click()
        self.assertTrue(discount.get_property("value"), 5)
        for i in range(0,20):
            button_up.click()
        self.assertTrue(discount.get_property("value"), 99)

#menues correctly change when switch panel
    def test_case_7(self):
        self.description = "correct switch with panels"
        panels = [self.driver.find_element_by_id("TabbedPaneSpecialModel"),
                  self.driver.find_element_by_id("TabbedPaneAccessory")]
        menu = [self.driver.find_element_by_id("SpecialsArea"),
                self.driver.find_element_by_id("AccessoryTable")]
        for index in range(0,len(panels)):
            panels[index].click()
            self.assertTrue(menu[index].is_displayed())

#When select another special  price changes and correctly
    def test_case_8(self):
        old_value = self.driver.find_element_by_id("SpecialPrice_input").text
        switch = self.driver.find_element_by_xpath("//a[@id='TabbedPaneSpecialModel']")
        switch.click()
        select = Select(self.driver.find_element_by_id('SpecialsCombo'))
        for i in self.testing_data["case_8"]["select"]:
            select.select_by_visible_text(i)
            new_value = self.driver.find_element_by_id("SpecialPrice_input").text
            self.assertFalse(old_value == new_value)
#Append new vehicles
    def test_case_9(self):
        data = self.testing_data["case_9"]
        for i in range(len(data["price"])):
            table = self.driver.find_element_by_id("VehicleTable"). \
                find_element_by_tag_name("tbody"). \
                find_elements_by_class_name("dataRow")
            length_Vehicle = len(table)
            btn_1 = self.driver.find_element_by_id("mOptions_menu")
            btn_1.click()
            btn_1 = self.driver.find_element_by_id("miVehicles_menu")
            btn_1.click()
            diag = self.driver.find_element_by_xpath("//div[@id='VehiclesDialog']/div")
            self.assertTrue(diag.is_displayed())
            inp = self.driver.find_element_by_id("VehicleName_input")
            inp.click()
            inp.send_keys(data["name"][i])
            inp = self.driver.find_element_by_id("VehiclePrice_input")
            inp.click()
            inp.send_keys(data["price"][i])
            inp = self.driver.find_element_by_xpath("// button[ @ id = 'NewButton1'] / span")
            inp.click()
            inp = self.driver.find_element_by_xpath("//button[@id='OkButton1']/span")
            inp.click()
            table = self.driver.find_element_by_id("VehicleTable"). \
                find_element_by_tag_name("tbody"). \
                find_elements_by_class_name("dataRow")
            self.assertTrue(length_Vehicle!=len(table))

#DElete vehicles
    def test_case_10(self):
        table = self.driver.find_element_by_id("VehicleTable"). \
            find_element_by_tag_name("tbody"). \
            find_elements_by_class_name("dataRow")
        length_Vehicle = len(table)
        btn_1 = self.driver.find_element_by_id("mOptions_menu")
        btn_1.click()
        btn_1 = self.driver.find_element_by_id("miVehicles_menu")
        btn_1.click()
        diag = self.driver.find_element_by_xpath("//div[@id='VehiclesDialog']/div")
        self.assertTrue(diag.is_displayed())
        if (len(table)==0):
            self.assertTrue(False)
        link = self.driver.find_element_by_xpath("//a[contains(text(),'delete')]")
        link.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        inp = self.driver.find_element_by_xpath("//button[@id='OkButton1']/ span")
        inp.click()
        table = self.driver.find_element_by_id("VehicleTable"). \
            find_element_by_tag_name("tbody"). \
            find_elements_by_class_name("dataRow")
        self.assertTrue(length_Vehicle > len(table))

