from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
try:
    browser.get(link)
    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.send_keys('Petr')
    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.send_keys('Batlook')
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('noreply@test.tt')
     
    loadfile = browser.find_element_by_css_selector('#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'file.txt')
    time.sleep(1)
    loadfile.send_keys(file_path)
   
    button = browser.find_element_by_css_selector('[type=submit]')
    button.click()

finally:
    time.sleep(15)
    browser.quit()