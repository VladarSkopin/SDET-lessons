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

driver: WebDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
wait: WebDriverWait = WebDriverWait(driver, 10, 0.6)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

slider_start: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//div[@id='slider-range']/span[1]")), "SLIDER START")
slider_stop: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//div[@id='slider-range']/span[2]")), "SLIDER STOP")
print(f'Slider start location: {slider_start.location}')
print(f'Slider stop location: {slider_stop.location}')

act = ActionChains(driver)
act.drag_and_drop_by_offset(slider_start, 300, 250).perform()
act.drag_and_drop_by_offset(slider_stop, -100, 250).perform()

time.sleep(5)
driver.quit()
