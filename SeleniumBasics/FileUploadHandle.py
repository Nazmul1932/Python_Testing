from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.implicitly_wait(10)

driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

driver.find_element(By.NAME, 'upfile').send_keys('E:\\gitTutorial\\file1.txt') # type='file' should be there

driver.find_element(By.XPATH, '//input[@type="submit"]').click()

time.sleep(3)
driver.quit()