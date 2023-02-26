import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
# driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10, 0.4)

driver.get("https://whatmylocation.com")
driver.maximize_window()


time.sleep(5)
driver.quit()
