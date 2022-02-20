from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

option = webdriver.ChromeOptions()
option.headless = False
option.add_argument('--incognito')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=option)

# option = webdriver.FirefoxOptions()
# option.headless = True
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
# driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
print(driver.title)