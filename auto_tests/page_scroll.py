import time
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver: WebDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
wait: WebDriverWait = WebDriverWait(driver, 10, 0.6)

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()

# scroll down by pixels
driver.execute_script("window.scrollBy(0,3000)", "")
value = driver.execute_script("return window.pageYOffset;")
print(f'Number of pixels moved: {value}')
time.sleep(3)
driver.execute_script("window.scrollBy(0,5000)", "")
value = driver.execute_script("return window.pageYOffset;")
print(f'Number of pixels moved: {value}')
time.sleep(3)

# scroll down until the element is visible
last_flag_box: WebElement = wait.until(ExCon.presence_of_element_located((By.CSS_SELECTOR, 'div[class="col-md-4"]:last-child')), 'LAST FLAG BOX')
driver.execute_script("arguments[0].scrollIntoView();", last_flag_box)
value = driver.execute_script("return window.pageYOffset;")
print(f'Number of pixels moved: {value}')
time.sleep(3)

# scroll down until the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(f'Number of pixels moved: {value}')
time.sleep(3)

# scroll back to the beginning
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(f'Number of pixels moved: {value}')

time.sleep(5)
driver.quit()
