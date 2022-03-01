from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import re


class BaseCommand:
    def __init__(self, driver):
        self.local_driver: webdriver.Chrome = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 5)

    def click_element(self, element):
       self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))
       self.local_driver.find_element(By.XPATH, element).click()

    def clear_element(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        self.local_driver.find_element(By.XPATH, element).clear()

    def send_text_to_element(self, element, text):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        self.local_driver.find_element(By.XPATH, element).send_keys(text)

    # def sort_element(self, element):
    #     self.wait.until(EC.element_located_to_be_selected((By.XPATH, element)))

    def get_element_text(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        return self.local_driver.find_element(By.XPATH, element).text

        self.wait.until(EC.text_to_be_present_in_element_value((By.XPATH, element)))
        return self.local_driver.find_element(By.XPATH, element).text

    def get_value(self, element):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        Elements = re.findall(r'\d+', self.local_driver.find_element(By.XPATH, element).text)
        Sum = '.'.join(Elements)
        return Sum







