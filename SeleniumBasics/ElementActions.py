from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")

username_element = driver.find_element(By.ID, 'username')
password_element = driver.find_element(By.ID, 'password')
login_button_element = driver.find_element(By.ID, 'loginBtn')

actionChains = ActionChains(driver)
# actionChains.send_keys_to_element(username_element, 'batchautomation@gmail.com').perform()
# actionChains.send_keys_to_element(password_element, 'Test@12345').perform()
actionChains.send_keys_to_element(username_element, 'batchautomation@gmail.com')
actionChains.send_keys_to_element(password_element, 'Test@12345')
actionChains.click(login_button_element).perform()


time.sleep(3)
driver.quit()