import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from typing import List


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
wait = WebDriverWait(driver, 10, 0.6)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  # 0 since there is only 1 frame on the page
"mm/dd/yyyy"
date_picker_input_box: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//input[@id='datepicker']")), "DATE INPUT BOX")
date_picker_input_box.send_keys('05/15/1993')

time.sleep(5)
driver.quit()
