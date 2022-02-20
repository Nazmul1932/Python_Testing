from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.reddit.com/")

print(driver.get_cookies())

driver.add_cookie({"name":"nazmul_automation", "domain":"reddit.com", "value":"Python"})

print(driver.get_cookies())

# cookies = driver.get_cookies()

# for cookie in cookies:
#     print(cookie)

time.sleep(3)
driver.quit()