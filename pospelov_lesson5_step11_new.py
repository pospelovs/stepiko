from selenium import webdriver
import time
import unittest


class TestElement(unittest.TestCase):
    def test_element1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("form > .first_block > .form-group:nth-child(1) > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("form > .first_block > .form-group:nth-child(2) > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("form > .first_block > .form-group:nth-child(3) > input")
        input3.send_keys("email")
        input4 = browser.find_element_by_css_selector("form > .second_block > .form-group:nth-child(1) > input")
        input4.send_keys("666")
        input5 = browser.find_element_by_css_selector("form > .second_block > .form-group:nth-child(2) > input")
        input5.send_keys("Smolensk")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text,
                         "Congratulations! You have successfully registered!", "Error 1")

        time.sleep(5)
        browser.quit()

    def test_element2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("form > .first_block > .form-group:nth-child(1) > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("form > .first_block > .form-group:nth-child(2) > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("form > .first_block > .form-group:nth-child(3) > input")
        input3.send_keys("email")
        input4 = browser.find_element_by_css_selector("form > .second_block > .form-group:nth-child(1) > input")
        input4.send_keys("666")
        input5 = browser.find_element_by_css_selector("form > .second_block > .form-group:nth-child(2) > input")
        input5.send_keys("Smolensk")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text,
                         "Congratulations! You have successfully registered!", "Error 2")

        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    unittest.main()


