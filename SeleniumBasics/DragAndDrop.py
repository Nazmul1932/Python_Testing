from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actionChains = ActionChains(driver)
# actionChains.drag_and_drop(source, target).perform()
actionChains.click_and_hold(source).move_to_element(target).release().perform()

time.sleep(2)