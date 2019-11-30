# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRegicstration2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_regicstration2(self):
    # Test name: regicstration2
    # Step # | name | target | value | comment
    # 1 | open | http://selenium1py.pythonanywhere.com/ru/ |  | 
    self.driver.get("http://selenium1py.pythonanywhere.com/ru/")
    # 2 | setWindowSize | 1552x848 |  | 
    self.driver.set_window_size(1552, 848)
    # 3 | click | id=login_link |  | 
    self.driver.find_element(By.ID, "login_link").click()
    # 4 | click | id=id_registration-email |  | 
    self.driver.find_element(By.ID, "id_registration-email").click()
    # 5 | type | id=id_registration-email | testtest@test.test | 
    self.driver.find_element(By.ID, "id_registration-email").send_keys("testtest@test.test")
    # 6 | click | id=id_registration-password1 |  | 
    self.driver.find_element(By.ID, "id_registration-password1").click()
    # 7 | type | id=id_registration-password1 | 123456_test | 
    self.driver.find_element(By.ID, "id_registration-password1").send_keys("123456_test")
    # 8 | click | id=id_registration-password2 |  | 
    self.driver.find_element(By.ID, "id_registration-password2").click()
    # 9 | type | id=id_registration-password2 | 123456_test | 
    self.driver.find_element(By.ID, "id_registration-password2").send_keys("123456_test")
    # 10 | click | name=registration_submit |  | 
    self.driver.find_element(By.NAME, "registration_submit").click()
    # 11 | assertText | //*[@id="messages"]/div/div | Спасибо за регистрацию! | 
    assert self.driver.find_element(By.XPATH, "//*[@id=\"messages\"]/div/div").text == "Спасибо за регистрацию!"
