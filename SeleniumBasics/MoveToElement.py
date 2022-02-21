from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://spicejet.com/")
time.sleep(3)

addons_element = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-1v8vaea r-1d2f490 r-u8s1d r-zchlnj r-1pozq62']")
actionChains = ActionChains(driver)
actionChains.move_to_element(addons_element).perform()