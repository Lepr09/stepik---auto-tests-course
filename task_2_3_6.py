from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element_by_css_selector('[type=submit]').click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    
#    browser.switch_to.alert.accept()
    x = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_css_selector('#answer').send_keys(str(calc(x)))
    button = browser.find_element_by_css_selector('[type=submit]')
    button.click()

finally:
    time.sleep(15)
    browser.quit()