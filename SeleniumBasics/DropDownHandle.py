from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/open-source/demo/")


def select_value(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


def selectValuesFromDropDown(dropDownOptionList, values):
    # country_list = driver.find_elements(By.XPATH, "//select[@id='Form_submitRequest_Country']/option")
    print(len(dropDownOptionList))
    for ele in dropDownOptionList:
        print(ele.text)
        if ele.text == 'Gambia':
            ele.click()
            break


country_list = driver.find_elements(By.XPATH, "//select[@id='Form_submitRequest_Country']/option")
selectValuesFromDropDown(country_list, 'Tokelau')
selectValuesFromDropDown(country_list, 'Senegal')

industry_dropdown = driver.find_element(By.ID, "Form_submitRequest_Industry")
country_dropdown = driver.find_element(By.ID, "Form_submitRequest_Country")

select_value(industry_dropdown, 'Education')
select_value(country_dropdown, 'Bangladesh')
# select_industry = Select(industry_dropdown)
# select_industry.select_by_visible_text("Education")
# # # select_industry.select_by_index(5)
# # # select_industry.select_by_value('media')
# # print(select_industry.is_multiple())
#
# country_dropdown = driver.find_element(By.ID, "Form_submitRequest_Country")
# select_country = Select(country_dropdown)
# select_country.select_by_visible_text("Bangladesh")

# select = Select(country_dropdown)
# country_list = select.options
# for ele in country_list:
#     print(ele.text)
#     if ele.text == 'Gambia':
#         ele.click()
#         break

# country_list = driver.find_elements(By.XPATH, "//select[@id='Form_submitRequest_Country']/option")
# print(len(country_list))
# for ele in country_list:
#     print(ele.text)
#     if ele.text == 'Gambia':
#         ele.click()
#         break


time.sleep(3)
driver.quit()
