from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import time

# for chrome
# options = Options()
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('--ignore-certificate-errors')

# desired_capabilities = DesiredCapabilities().CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True

# options = Options()
# options.set_capability('acceptInsecureCerts', True)


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options) 


# for firefox

# profile = webdriver.FirefoxProfile()
# profile.accept_untrusted_certs = True

desired_capabilities = DesiredCapabilities().FIREFOX.copy()
desired_capabilities['acceptInsecureCerts'] = True

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), capabilities=desired_capabilities) 


driver.implicitly_wait(10)


driver.get("https://expired.badssl.com/")
print(driver.find_element(By.TAG_NAME, 'h1').text)

driver.quit()