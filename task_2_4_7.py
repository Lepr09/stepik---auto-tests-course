import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
#browser.implicitly_wait(5)

try:
    browser.get(link)
#    l = browser.find_element_by_css_selector('#price')
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element(browser.find_element_by_id('price').text, '$100'))
    butt = browser.find_element_by_css_selector('#book')
    butt.click()
    x = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_css_selector('#answer').send_keys(calc(x))
    button = browser.find_element_by_css_selector('[type=submit]')
    button.click()
    
    
#    new_window = browser.window_handles[1]
#    first_window = browser.window_handles[0]
#    browser.switch_to.window(new_window)
    
#    browser.switch_to.alert.accept()
#    x = browser.find_element_by_css_selector('#input_value').text
#    browser.find_element_by_css_selector('#answer').send_keys(str(calc(x)))
#    button = browser.find_element_by_css_selector('[type=submit]')
#    button.click()

finally:
    time.sleep(10)
    browser.quit()