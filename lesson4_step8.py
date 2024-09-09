from typing import Tuple
from xml.sax.xmlreader import Locator

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    wait_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), text_="100")
    )
    book_button = browser.find_element(By.CSS_SELECTOR, 'button#book.btn')
    book_button.click()


    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    input_answer.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, 'button#solve.btn')
    button.click()
    time.sleep(1)


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
