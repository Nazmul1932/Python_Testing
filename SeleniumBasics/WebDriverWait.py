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

# wait.until(EC.title_is('Facebook – log in or sign up'))
wait.until(EC.title_contains('Facebook –'))
print(driver.title)

email_id = wait.until(EC.presence_of_element_located((By.ID, 'email')))
email_id.send_keys('test@gmail.com')

driver.find_element(By.ID, 'pass').send_keys('test123')

time.sleep(2)