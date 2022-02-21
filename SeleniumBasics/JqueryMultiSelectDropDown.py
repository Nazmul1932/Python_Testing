from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")


def select_values(drop_down_list, value):
    if not value[0] == 'all':
        for ele in drop_down_list:
            print(ele.text)
            # if ele.text == value:
            #     ele.click()
            #     break
            for l in range(len(value)):
                if ele.text == value[l]:
                    ele.click()
                    break
    else:
        try:
            for ele in drop_down_list:
                ele.click()
        except Exception as e:
            print(e)


driver.find_element(By.ID, 'justAnInputBox').click()

dropdown_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
values_list = ['choice 6', 'choice 5', 'choice 3']  # multi selection
# values_list = ['choice 6']  # for one selection
# values_list = ['all']  # for all selection
select_values(dropdown_list, values_list)
# select_values(dropdown_list, 'choice 6')
# select_values(dropdown_list, 'choice 5')
# select_values(dropdown_list, 'choice 3')
# for ele in dropdown_list:
#     print(ele.text)
#     if ele.text == 'choice 6 2 3':
#         ele.click()
#         break
time.sleep(3)
driver.quit()

