from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

right_click_element = driver.find_element(By.XPATH, "//span[text()='right click me']")
actionChains = ActionChains(driver)
actionChains.context_click(right_click_element).perform()
right_click_options_list = driver.find_elements(By.CSS_SELECTOR, "li.context-menu-icon span")

for ele in right_click_options_list:
    print(ele.text)
    if ele.text == 'Copy':
        ele.click()
        break

time.sleep(3)
driver.quit()
