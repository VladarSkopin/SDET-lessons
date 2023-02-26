import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10, 0.4)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

page_title = driver.title
print(f'Page title: {page_title}')
assert page_title.lower() == "automation testing practice"

# click on alert
alert_btn = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//button[text()='Click Me']")), "ALERT BTN")
alert_btn.click()
prompt_window = driver.switch_to.alert
print(f'Prompt window text: {prompt_window.text}')
time.sleep(3)
prompt_window.accept()

# get text after clicking on alert
text_under_alert_btn = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//p[@id='demo']")), "TEXT UNDER ALERT BTN").text
print(f'Text under alert button: \"{text_under_alert_btn}\"')
assert text_under_alert_btn == "You pressed OK!"

# type "taco" into the search box
input_wiki_btn = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//input[@class='wikipedia-search-input']")), "INPUT WIKI BTN")
input_wiki_btn.send_keys("taco")

# click the search button
wiki_search_btn = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//input[@class='wikipedia-search-button']")), "WIKI SEARCH BTN")
wiki_search_btn.click()

# first search result
wiki_search_text_link_1 = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//div[@id='wikipedia-search-result-link'][1]/a[1]")), "WIKI SEARCH RESULT TEXT LINK 1")
wiki_search_text_link_first_text = wiki_search_text_link_1.text
print(f'Wiki search result first text link: \"{wiki_search_text_link_first_text}\"')
assert wiki_search_text_link_first_text.lower() == 'taco'
wiki_search_text_link_1.click()

# second search result
wiki_search_text_link_2 = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//div[@id='wikipedia-search-result-link'][2]/a[1]")), "WIKI SEARCH RESULT TEXT LINK 2")
wiki_search_text_link_first_text = wiki_search_text_link_2.text
print(f'Wiki search result second text link: \"{wiki_search_text_link_first_text}\"')
assert wiki_search_text_link_first_text.lower() == 'taco bell'
wiki_search_text_link_2.click()

# third search result
wiki_search_text_link_3 = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//div[@id='wikipedia-search-result-link'][3]/a[1]")), "WIKI SEARCH RESULT TEXT LINK 3")
wiki_search_text_link_first_text = wiki_search_text_link_3.text
print(f'Wiki search result third text link: \"{wiki_search_text_link_first_text}\"')
assert wiki_search_text_link_first_text.lower() == 'tacoma, washington'
wiki_search_text_link_3.click()

# fourth search result
wiki_search_text_link_4 = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//div[@id='wikipedia-search-result-link'][4]/a[1]")), "WIKI SEARCH RESULT TEXT LINK 4")
wiki_search_text_link_first_text = wiki_search_text_link_4.text
print(f'Wiki search result fourth text link: \"{wiki_search_text_link_first_text}\"')
assert wiki_search_text_link_first_text.lower() == 'tacoma narrows bridge (1940)'
wiki_search_text_link_4.click()

# fifth search result
wiki_search_text_link_5 = wait.until(ExCon.visibility_of_element_located((By.XPATH, "//div[@id='wikipedia-search-result-link'][5]/a[1]")), "WIKI SEARCH RESULT TEXT LINK 5")
wiki_search_text_link_first_text = wiki_search_text_link_5.text
print(f'Wiki search result fifth text link: \"{wiki_search_text_link_first_text}\"')
assert wiki_search_text_link_first_text.lower() == 'tacko fall'
wiki_search_text_link_5.click()

window_ids = driver.window_handles
count = 1
for window in window_ids:
    driver.switch_to.window(window)
    print(f'window {count}: {window}')
    time.sleep(3)
    driver.save_screenshot(f"screenshots_tasks/window_{count}.png")
    count += 1

for window in window_ids:
    driver.switch_to.window(window)
    time.sleep(1)
    driver.close()

time.sleep(5)
driver.quit()
