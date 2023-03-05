import time
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from typing import List


driver: WebDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
wait: WebDriverWait = WebDriverWait(driver, 10, 0.6)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  # 0 since there is only 1 frame on the page
date_picker_input_box: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//input[@id='datepicker']")), "DATE INPUT BOX")
# "mm/dd/yyyy" date format
date_picker_input_box.send_keys('05/15/1993')

year: str = '2002'
month: str = 'September'
day: str = '1'

while True:
    m: str = wait.until(ExCon.presence_of_element_located((By.XPATH, "//span[@class='ui-datepicker-month']")), "DATEPICKER MONTH TEXT").text
    y: str = wait.until(ExCon.presence_of_element_located((By.XPATH, "//span[@class='ui-datepicker-year']")), "DATEPICKER YEAR TEXT").text

    if m == month and y == year:
        # find day table element
        days_in_current_month: List[WebElement] = wait.until(ExCon.presence_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")), "DATEPICKER DAYS")
        for d in days_in_current_month:
            print(d.text)
            if d.text == day:
                d.click()  # click on the date
                break
        break
    else:
        # click "Next" icon
        wait.until(ExCon.presence_of_element_located((By.XPATH, "//a[@data-handler='next']")), "DATEPICKER NEXT ICON").click()
        time.sleep(0.1)
"""        
    elif int(y) < int(year):
        # click "Next" icon
        wait.until(ExCon.presence_of_element_located((By.XPATH, "//a[@data-handler='next']")), "DATEPICKER NEXT ICON").click()
        time.sleep(1)
    elif int(y) > int(year):
        # click "Previous" icon
        wait.until(ExCon.presence_of_element_located((By.XPATH, "//a[@data-handler='prev']")), "DATEPICKER PREVIOUS ICON").click()
        time.sleep(1)
"""


time.sleep(5)
driver.quit()
