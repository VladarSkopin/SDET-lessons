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

act = ActionChains(driver)


time.sleep(5)
driver.quit()
