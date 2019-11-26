from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

driver = webdriver.Chrome()
try:
    driver.get(link)
    num1 = int(driver.find_element_by_css_selector('#num1').text)
#    user_name.send_keys('d.zhakov@web-regata.ru')
    num2 = int(driver.find_element_by_css_selector('#num2').text)
    select = Select(driver.find_element_by_css_selector('#dropdown'))
    select.select_by_visible_text(str(num1+num2))
#    time.sleep(10)
    
    button = driver.find_element_by_css_selector('[type=submit]')
    button.click()
    time.sleep(15)

finally:
    driver.quit()