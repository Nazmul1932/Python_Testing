from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    
    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    if request.param == "firefox":
         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
         
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield 
    driver.close()