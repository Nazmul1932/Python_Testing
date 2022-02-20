from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login-cgi")
driver.find_element(By.NAME, "proceed").click()
alert_element = driver.switch_to.alert
print(alert_element.text)
alert_element.accept()
# alert_element.dismiss()
# alert_element.send_keys()
driver.switch_to.default_content()

time.sleep(3)
driver.quit()