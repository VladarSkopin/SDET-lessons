import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10, 0.4)

driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()

wait.until(ExCon.visibility_of_element_located((By.XPATH, "//a[@href='#Multiple']")), '"Frame within a frame" TAB').click()

# //iframe[@src='MultipleFrames.html']
outer_frame = wait.until(ExCon.presence_of_element_located((By.XPATH, "//iframe[@src='MultipleFrames.html']")), 'OUTER FRAME')
driver.switch_to.frame(outer_frame)

# //iframe[@src='SingleFrame.html']
inner_frame = wait.until(ExCon.presence_of_element_located((By.XPATH, "//iframe[@src='SingleFrame.html']")), 'INNER FRAME')
driver.switch_to.frame(inner_frame)

input_box = wait.until(ExCon.presence_of_element_located((By.XPATH, "//input[@type='text']")), 'INPUT BOX')
input_box.send_keys("Sasha")
driver.save_screenshot('screenshots/nested_frames.png')

time.sleep(5)
driver.quit()
