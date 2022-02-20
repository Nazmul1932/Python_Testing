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
driver.get("https://www.facebook.com/")

wait = WebDriverWait(driver, 10)
create_page_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Create a Page')))
print(create_page_link.text)
create_page_link.click()

email = wait.until(EC.visibility_of_element_located((By.ID, 'email')))
email.send_keys("admin@gmail.com")