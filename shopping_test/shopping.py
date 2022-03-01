import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import math

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from util.base_command import BaseCommand
from util.field import Field


class HelloWorldTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")

        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
        self.driver.get("https://www.saucedemo.com/")

        self.base_command = BaseCommand(self.driver)

    def test_sauce_login(self):
        self.base_command.clear_element(Field.username_textfield)
        self.base_command.send_text_to_element(Field.username_textfield, "standard_user")

        self.base_command.clear_element(Field.username_passwordfield)
        self.base_command.send_text_to_element(Field.username_passwordfield, "secret_sauce")
        self.base_command.click_element(Field.login_button)

        self.assertEqual("Products".casefold(),
                         self.base_command.get_element_text(Field.product_span).casefold())

        self.base_command.click_element(Field.product_sort)
        self.base_command.click_element(Field.select_by_value)

        self.base_command.click_element(Field.add_to_cart)
        self.base_command.click_element(Field.add_to_cart_1)
        self.base_command.click_element(Field.add_to_cart_2)

        self.base_command.click_element(Field.inside_the_cart)
        self.base_command.click_element(Field.checkout)
        time.sleep(10)
        self.base_command.clear_element(Field.first_name)
        self.base_command.send_text_to_element(Field.first_name, "Vova")

        self.base_command.clear_element(Field.last_name)
        self.base_command.send_text_to_element(Field.last_name, "Lastname")
        self.base_command.send_text_to_element(Field.postal_code, "12345")

        self.base_command.click_element(Field.click_continue)
        #
        # self.base_command.get_element_text()

        time.sleep(10)

        # self.base_command.get_element_text(Field.get_total)
        # self.base_command.get_element_text(Field.sub_total)
        # Field.get_tax = round(float(Field.get_tax), 2)

        self.assertEqual("89.97", self.base_command.get_value(Field.sub_total))
        self.assertEqual("97.17", self.base_command.get_value(Field.total))

        self.assertEqual("7.20", self.base_command.get_value(Field.get_tax))


        substract = float(self.base_command.get_value(Field.total))-float(self.base_command.get_value(Field.sub_total))

        self.assertEqual(substract, (float(self.base_command.get_value(Field.get_tax))))


        def tearDown(self):
            self.driver.close()


if __name__ == '__main__':
    unittest.main()
