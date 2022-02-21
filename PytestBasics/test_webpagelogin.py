from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

def test_google():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    assert driver.title == 'Google'
    driver.quit()
    
def test_facebook():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    assert driver.title == 'Facebook – log in or sign up'
    driver.quit()
    
def test_instagram():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/")
    assert driver.title == 'Instagram'
    driver.quit()
    
def test_orangehrm():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
    assert driver.title == 'Sign Up for a Free HR Software Trial | OrangeHRM'
    driver.quit()