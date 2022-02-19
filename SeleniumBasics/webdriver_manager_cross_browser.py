from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

browserName = 'ie'

if browserName == "chrome":
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "edge":
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
else:
    print("please enter the correct browser name", browserName)
    raise Exception('driver is not found')

driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.ID, 'txtUsername').send_keys("Admin")
driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
driver.find_element(By.ID, 'btnLogin').click()

print(driver.title)

time.sleep(3)
driver.quit()





