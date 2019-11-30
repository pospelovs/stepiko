from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_basket_button(browser):
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
    )
    basket_button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert basket_button > 0, "No basket button"
