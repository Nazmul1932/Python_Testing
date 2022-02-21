from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()
# driver.get("https://classic.crmpro.com/")
driver.get("https://www.amazon.com/")

# username = driver.find_element(By.NAME, "username")
# password = driver.find_element(By.NAME, "password")
# login = driver.find_element(By.XPATH, "//input[@value='Login']")
#
# username.send_keys("batchautomation")
# password.send_keys("Test@12345")
# login.click()
# linkLists = driver.find_elements(By.TAG_NAME, "a")
# print(len(linkLists))
#
# for ele in linkLists:
#     print(ele.text)
#     print(ele.get_attribute('href'))


imgLists = driver.find_elements(By.TAG_NAME, "img")
print(len(imgLists))

for ele in imgLists:
    # print(ele.text)
    print(ele.get_attribute('src'))


time.sleep(3)