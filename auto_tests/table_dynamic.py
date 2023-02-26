import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from typing import List

USER_LOGIN = "Admin"
USER_PASSWORD = "admin123"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
wait = WebDriverWait(driver, 10, 0.4)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

input_username: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//input[@name='username']")), "INPUT USERNAME")
input_username.send_keys(USER_LOGIN)

input_password: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//input[@name='password']")), "INPUT PASSWORD")
input_password.send_keys(USER_PASSWORD)

submit_btn: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//div[@class='oxd-form-actions orangehrm-login-action']/button[@type='submit']")), "SUBMIT BTN")
submit_btn.click()

admin_tab: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//a[@class='oxd-main-menu-item'][1]")), "ADMIN TAB")
admin_tab.click()

user_management_dropdown: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and text()='User Management ']")), "USER MANAGEMENT DROPDOWN")
user_management_dropdown.click()

time.sleep(3)  # mock user behaviour

users_dropdown_option = wait.until(ExCon.presence_of_element_located((By.XPATH, "//a[text()='Users']")), "USERS DROPDOWN OPTION")
users_dropdown_option.click()

time.sleep(5)  # mock user behaviour

# total number of rows
dynamic_table_rows: List[WebElement] = wait.until(ExCon.presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell'][2]")), "TABLE ROWS")
number_of_rows = len(dynamic_table_rows)
print(f'Total number of rows in the table: {number_of_rows}')

# print Username, User role, Employee name where Status is "Enabled"
print('Where Status is "Enabled": ')
count_enabled_users = 0
count_disabled_users = 0
for x in range(1, number_of_rows + 1):
    status_data: str = wait.until(ExCon.presence_of_element_located((By.XPATH, f"//div[@class='oxd-table-card'][{x}]//div[@class='oxd-table-cell oxd-padding-cell'][5]")), "STATUS").text
    if status_data.lower() == 'enabled':
        current_username: str = wait.until(ExCon.presence_of_element_located((By.XPATH, f"//div[@class='oxd-table-card'][{x}]//div[@class='oxd-table-cell oxd-padding-cell'][2]")), "USER NAME").text
        current_user_role: str = wait.until(ExCon.presence_of_element_located((By.XPATH, f"//div[@class='oxd-table-card'][{x}]//div[@class='oxd-table-cell oxd-padding-cell'][3]")), "USER ROLE").text
        current_employee_name: str = wait.until(ExCon.presence_of_element_located((By.XPATH, f"//div[@class='oxd-table-card'][{x}]//div[@class='oxd-table-cell oxd-padding-cell'][4]")), "EMPLOYEE NAME").text
        current_status: str = wait.until(ExCon.presence_of_element_located((By.XPATH, f"//div[@class='oxd-table-card'][{x}]//div[@class='oxd-table-cell oxd-padding-cell'][5]")), "USER STATUS").text
        print(f'Username: "{current_username}" | User Role: "{current_user_role}" | Employee Name: "{current_employee_name}" | Status: "{current_status}"')
        count_enabled_users += 1
    else:
        count_disabled_users += 1
    print()

print(f'Total number of users with "Enabled" status: {count_enabled_users}')
print(f'Total number of users with "Disabled" status: {count_disabled_users}')

time.sleep(5)
driver.quit()
