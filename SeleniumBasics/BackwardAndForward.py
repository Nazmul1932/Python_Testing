from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
time.sleep(2)
driver.find_element(By.LINK_TEXT, 'Best Sellers').click()
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
driver.quit()