import time
from selenium import webdriver

driver = webdriver.Firefox()

# inject password and login INTO THE URL in complex alert scenarios
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
USER_LOGIN = 'admin'
USER_PASSWORD = 'admin'

time.sleep(5)
driver.quit()
