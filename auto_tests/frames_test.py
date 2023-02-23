import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10, 0.4)

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
driver.maximize_window()

# driver.switch_to.frame(0)
driver.switch_to.frame("packageListFrame")
# driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
package_link = wait.until(ExCon.visibility_of_element_located((By.LINK_TEXT, "org.openqa.selenium")), '"org.openqa.selenium" LINK BUTTON')
package_link.click()

driver.switch_to.default_content()  # back to main page
# driver.switch_to.parent_frame()
driver.switch_to.frame("packageFrame")
web_driver_link = wait.until(ExCon.visibility_of_element_located((By.LINK_TEXT, "WebDriver")), '"WebDriver" LINK BUTTON')
web_driver_link.click()

driver.switch_to.default_content()  # back to main page
# driver.switch_to.parent_frame()
driver.switch_to.frame("classFrame")
help_link = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//div[@class='topNav']//a[contains(text(), 'Help')]")), '"Help" LINK BUTTON')
help_link.click()

time.sleep(5)
driver.quit()
