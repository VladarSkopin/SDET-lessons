import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10, 0.4)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# get current window ID, click on link button to open another window
window_id = driver.current_window_handle
print(f'current window: {window_id}')  # this ID is different every time !
bottom_link_btn = wait.until(ExCon.visibility_of_element_located((By.LINK_TEXT, "OrangeHRM, Inc")), "BOTTOM LINK BTN")
bottom_link_btn.click()

# get window IDs, switch to the second (child) window
window_ids = driver.window_handles
parent_window_id = window_ids[0]
print(f'parent window: {parent_window_id}')  # == driver.current_window_handle
child_window_id = window_ids[1]
driver.switch_to.window(child_window_id)
time.sleep(5)
driver.save_screenshot('window_child.png')
print(f'driver title: {driver.title}')
print(f'child window: {child_window_id}')
driver.close()

# switch the driver back to the first (parent) window
driver.switch_to.window(parent_window_id)
time.sleep(5)
driver.save_screenshot('window_parent.png')
print(f'driver title: {driver.title}')


if window_id == parent_window_id:
    print("Current window ID is the same as the parent window ID")
else:
    print("Current window ID is NOT the same as the parent window ID")

time.sleep(5)
driver.quit()
