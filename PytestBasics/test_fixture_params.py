from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import pytest


# @pytest.fixture(params=["chrome", "firefox"], scope='class')
# def init_driver(request):
    
#     if request.param == "chrome":
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#     if request.param == "firefox":
#          driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
         
#     request.cls.driver = driver
#     yield 
#     driver.close()
    
    
@pytest.mark.usefixtures("init_driver")    
class BaseTest:
    pass


class Test_Google(BaseTest):
    
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
        
    def test_google_url(self):
        self.driver.get("https://www.google.com")
        assert self.driver.current_url == "https://www.google.com/"