from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://demo.applitools.com/"
driver = webdriver.Edge()
driver.get(url)


username = "shreya"
password = "shreya123"

username_field = driver.find_element(By.XPATH,"//input[@id='username']")
password_field = driver.find_element(By.XPATH,"//input[@id='password']")
check_box = driver.find_element(By.XPATH,"//input[@class='form-check-input']")
login_field = driver.find_element(By.XPATH,"//a[@id='log-in']")
time.sleep(1)
username_field.send_keys(username)
time.sleep(2)
password_field.send_keys(password)
time.sleep(2)
check_box.click()
time.sleep(2)
login_field.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)


driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)



time.sleep(5)
driver.quit()