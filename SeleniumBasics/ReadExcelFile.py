import xlrd
import openpyxl
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

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial-old/")

url_name           = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name     = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name      = driver.find_element(By.ID, 'Form_submitForm_LastName')
email_id         = driver.find_element(By.ID, 'Form_submitForm_Email')
job_title      = driver.find_element(By.ID, 'Form_submitForm_JobTitle')
company_name       = driver.find_element(By.ID, 'Form_submitForm_CompanyName')
phone_no         = driver.find_element(By.ID, 'Form_submitForm_Contact')
noofemployee  = driver.find_element(By.ID, 'Form_submitForm_NoOfEmployees')
industry      = driver.find_element(By.ID, 'Form_submitForm_Industry')
country       = driver.find_element(By.ID, 'Form_submitForm_Country')



workbook = xlrd.open_workbook('data_file.xlsx')

print(workbook.sheet_names())

sheet = workbook.sheet_by_name('registration')

row_count = sheet.nrows
col_count = sheet.ncols

print(row_count)
print(col_count)

for curr_rows in range(1,row_count):
    url           = sheet.cell_value(curr_rows, 0)
    firstname     = sheet.cell_value(curr_rows, 1)
    lastname      = sheet.cell_value(curr_rows, 2)
    email         = sheet.cell_value(curr_rows, 3)
    jobtitle      = sheet.cell_value(curr_rows, 4)
    company       = sheet.cell_value(curr_rows, 5)
    phone         = sheet.cell_value(curr_rows, 6)
    noofemployee  = sheet.cell_value(curr_rows, 7)
    industry      = sheet.cell_value(curr_rows, 8)
    country       = sheet.cell_value(curr_rows, 9)
    
# print(url+firstname+lastname)

    url_name.clear()
    url_name.send_keys(url)
    first_name.clear()
    first_name.send_keys(firstname)
    last_name.clear()
    last_name.send_keys(lastname)
    email_id.clear()
    email_id.send_keys(email)
    job_title.clear()
    job_title.send_keys(jobtitle)
    company_name.clear()
    company_name.send_keys(company)
    phone_no.clear()
    phone_no.send_keys(phone)
    # noofemployee.send_keys(noofemployee)
    # industry.send_keys(industry)
    # country.send_keys(country)

    time.sleep(4)
    
    
    