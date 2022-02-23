from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.implicitly_wait(10)
    request.cls.driver = ch_driver
    yield 
    ch_driver.close()
    
    
@pytest.fixture(scope='class')
def init_firefox_driver(request):
    ff_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    # driver.implicitly_wait(10)
    request.cls.driver = ff_driver
    yield 
    ff_driver.close()
    

@pytest.mark.usefixtures("init_chrome_driver")    
class Base_Chrome_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):
    
    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == 'Google'
        

@pytest.mark.usefixtures("init_firefox_driver")    
class Base_Firefox_Test:
    pass

class Test_Google_Firefox(Base_Firefox_Test):
    
    def test_google_title_firefox(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == 'Google'