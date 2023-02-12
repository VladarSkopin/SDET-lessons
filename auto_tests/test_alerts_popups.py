import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, 0.4)

driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
# prompt_btn = wait.until(ExCon.presence_of_element_located((By.XPATH, "//button[@onclick='jsPrompt()']")), 'PROMPT BTN')
prompt_btn = wait.until(ExCon.presence_of_element_located((By.XPATH, "//button[normalize-space()='Click for JS Prompt']")), 'PROMPT BTN')
prompt_btn.click()
alert_window = driver.switch_to.alert  # .window / .frame ...
print(alert_window.text)  # DOESN'T PRINT ANYTHING (???)

alert_window.send_keys("I am Alex")
alert_window.accept()
# alert_window.dismiss()

# driver.save_screenshot('alerts_1.png')
time.sleep(5)
