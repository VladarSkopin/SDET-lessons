import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10, 0.4)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


alert_btn = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//button[text()='Click Me']")), "ALERT BTN")
alert_btn.click()



time.sleep(5)
driver.quit()

