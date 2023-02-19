import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, 0.4)

driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

# PROMPT WINDOW
# prompt_btn = wait.until(ExCon.presence_of_element_located((By.XPATH, "//button[@onclick='jsPrompt()']")), 'PROMPT BTN')
prompt_btn = wait.until(ExCon.presence_of_element_located((By.XPATH, "//button[normalize-space()='Click for JS Prompt']")), 'PROMPT BTN')
prompt_btn.click()
prompt_window = driver.switch_to.alert  # .window / .frame ...
print(prompt_window.text)  # DOESN'T PRINT ANYTHING (???)
prompt_window.send_keys("I am Alex")
prompt_window.accept()  # "Ok" button
# alert_window.dismiss()  # "Cancel" button

# CONFIRM WINDOW
confirm_btn = wait.until(ExCon.presence_of_element_located((By.XPATH, "//button[normalize-space()='Click for JS Confirm']")), 'CONFIRM BTN')
confirm_btn.click()
confirm_window = driver.switch_to.alert
print(confirm_window.text)
confirm_window.dismiss()

# ALERT WINDOW
alert_btn = wait.until(ExCon.presence_of_element_located((By.XPATH, "//button[normalize-space()='Click for JS Alert']")), 'ALERT BTN')
alert_btn.click()
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.accept()

time.sleep(5)




