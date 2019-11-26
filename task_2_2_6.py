from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    x = driver.find_element_by_css_selector('#input_value').text
    answ = math.log(abs(12*math.sin(int(x))))
    driver.execute_script('window.scrollBy(0, 200)')
    x = driver.find_element_by_css_selector('#answer')
    x.send_keys(str(answ))
#    time.sleep(15)
    inp1 = driver.find_element_by_css_selector('#robotCheckbox')
    inp1.click()
    inp1 = driver.find_element_by_css_selector('#robotsRule')
    inp1.click()
    button = driver.find_element_by_css_selector('[type=submit]')
    button.click()

finally:
    time.sleep(15)
    driver.quit()