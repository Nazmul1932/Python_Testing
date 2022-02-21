from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
# driver.get("https://www.amazon.in/")
driver.get("https://www.facebook.com/")
# driver.get("https://classic.crmpro.com/")

# best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
# driver.execute_script("arguments[0].click();", best_sellers)

# title = driver.execute_script("return document.title;")
# print(title)

# # driver.execute_script("history.go(0);")
# driver.execute_script("alert('Hello amazon from selenium');")

# inner_text = driver.execute_script("return document.documentElement.innerText")
# print(inner_text)
# # driver.execute_script("arguments[0].style.border = '3px solid red'", best_sellers)
# form = driver.find_element(By.ID, 'email')
# driver.execute_script("arguments[0].style.border = '3px solid red'", form)
# time.sleep(3)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# # forget_pwd = driver.find_element(By.LINK_TEXT, 'Forgot Password?')
# # driver.execute_script("arguments[0].scrollIntoView(true);", forget_pwd)

# sports_header = driver.find_element(By.XPATH, '//span[text()="Best Sellers in Sports, Fitness & Outdoors"]')
# driver.execute_script("arguments[0].scrollIntoView(true);", sports_header)
# driver.execute_script("arguments[0].style.border = '3px solid red'", sports_header)

# print(driver.execute_script("return navigator.userAgent;"))
driver.execute_script("document.getElementById('email').value='test@gmail.com';")


time.sleep(2)