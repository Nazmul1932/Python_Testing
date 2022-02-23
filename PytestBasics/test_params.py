from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubSpot(BaseTest):
    
    
    @pytest.mark.parametrize(
                                "username,password",
                                [("admin@gmail.com","admin123"),("naveen@gmail.com","naveen123")]
                            )
    def test_login(self,username,password):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.ID, 'email').send_keys(username)
        self.driver.find_element(By.ID, 'pass').send_keys(password)