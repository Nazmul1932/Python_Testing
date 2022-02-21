from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.XPATH, "//input[@id='username']").send_keys('test@gmail.com')
driver.find_element(By.ID, "password").send_keys('test@12345')