from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------setup-------")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")
    yield 
    print("-------teardown-------")
    driver.quit()
 
@pytest.mark.usefixtures("init_driver")   
def test_googleTitle():
    assert driver.title == 'Googlevgt'
    
@pytest.mark.usefixtures("init_driver")    
def test_googleUrl():
    assert driver.current_url == 'https://www.google.com/'