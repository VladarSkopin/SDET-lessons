import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

capitals: List[WebElement] = wait.until(ExCon.presence_of_all_elements_located((By.XPATH, "//div[@class='dragableBox' and contains(@id, 'box')]")), "CAPITALS LIST")
print(len(capitals))

countries: List[WebElement] = wait.until(ExCon.presence_of_all_elements_located((By.XPATH, "//div[@class='dragableBoxRight']")), "COUNTRIES LIST")
print(len(countries))

act = ActionChains(driver)

country_italy = countries[0]
country_spain = countries[1]
country_norway = countries[2]
country_denmark = countries[3]
country_south_korea = countries[4]
country_sweden = countries[5]
country_us = countries[6]

for capital in capitals:
    if capital.text.lower() == 'rome':
        act.move_to_element(capital).click_and_hold().move_to_element(country_italy).release().perform()
    elif capital.text.lower() == 'madrid':
        act.move_to_element(capital).click_and_hold().move_to_element(country_spain).release().perform()
    elif capital.text.lower() == 'oslo':
        act.move_to_element(capital).click_and_hold().move_to_element(country_norway).release().perform()
    elif capital.text.lower() == 'copenhagen':
        act.move_to_element(capital).click_and_hold().move_to_element(country_denmark).release().perform()
    elif capital.text.lower() == 'seoul':
        act.move_to_element(capital).click_and_hold().move_to_element(country_south_korea).release().perform()
    elif capital.text.lower() == 'stockholm':
        act.move_to_element(capital).click_and_hold().move_to_element(country_sweden).release().perform()
    elif capital.text.lower() == 'washington':
        act.move_to_element(capital).click_and_hold().move_to_element(country_us).release().perform()

time.sleep(5)
driver.quit()
