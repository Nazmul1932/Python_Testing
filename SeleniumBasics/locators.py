from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

userNameElement = driver.find_element(By.ID, "Form_submitForm_subdomain")
fullNameElement = driver.find_element(By.ID, "Form_submitForm_Name")
emailElement = driver.find_element(By.ID, "Form_submitForm_Email")
home_element_img = driver.find_element(By.XPATH, "//img[@class='nav-logo']")


userNameElement.send_keys("admin ")
fullNameElement.send_keys("admin nazmul")
emailElement.send_keys("admin_nazu@gmail.com")
home_element_img.click()

# print(driver.title)
time.sleep(3)

