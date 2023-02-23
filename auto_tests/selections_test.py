import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10, 0.4)

driver.get('https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()

# country_dropdown_box = wait.until(ExCon.visibility_of_element_located((By.CSS_SELECTOR, 'select#input-country')), 'country dropdown')
country_dropdown_box = Select(wait.until(ExCon.visibility_of_element_located((By.CSS_SELECTOR, 'select#input-country')), 'country dropdown'))

country_options = country_dropdown_box.options
print(f'{len(country_options)} options in total')
print(f'First option: \n{country_options[0]} \n---------------')
print(f'Middle option: \n{country_options[len(country_options) // 2]} \n---------------')
print(f'Last option: \n{country_options[len(country_options) - 1]} \n---------------')

country_dropdown_box.select_by_index(13)  # Australia
time.sleep(3)
driver.save_screenshot('screenshots/registration_1.png')
country_dropdown_box.select_by_visible_text('Canada')
time.sleep(3)
driver.save_screenshot('screenshots/registration_2.png')
country_dropdown_box.select_by_value('10')  # Argentina
time.sleep(3)
driver.save_screenshot('screenshots/registration_3.png')
driver.quit()


