from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.google.com")
print(driver.title)
driver.find_element(By.NAME, "q").send_keys("naveen automationlabs")
optionsList = driver.find_elements(By.XPATH, '//*[@id="contents"]/span[2]')
print(len(optionsList))
for ele in optionsList:
    print(ele.text)
    if ele.text == "naveen automationlabs youtube":
        ele.click()
        break

time.sleep(3)
driver.quit()