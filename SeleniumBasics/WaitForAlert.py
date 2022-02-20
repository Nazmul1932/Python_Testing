from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME, 'proceed').click()
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.alert_is_present())
print(alert.text)
alert.accept()
driver.close()