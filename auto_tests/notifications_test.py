import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
# driver = webdriver.Firefox()

driver.get("https://whatmylocation.com")
driver.maximize_window()

time.sleep(5)
driver.quit()
