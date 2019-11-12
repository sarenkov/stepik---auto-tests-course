import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100"))
    book = browser.find_element_by_css_selector("#book")
    book.click()

    x = browser.find_element_by_css_selector("#input_value").text
    y = math.log(math.fabs(12*math.sin(int(x))))

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(y))

    submit = browser.find_element_by_css_selector(".btn#solve")
    submit.click()
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
