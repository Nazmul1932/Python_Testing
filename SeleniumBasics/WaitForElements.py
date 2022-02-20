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
driver.get("https://www.freshworks.com/")

wait = WebDriverWait(driver, 10)
footer_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.footer-nav li')))
print(len(footer_links))

for ele in footer_links:
    print(ele.text)