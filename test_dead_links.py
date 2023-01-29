import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Firefox()
driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()

wait = WebDriverWait(driver, 10, 0.4)
links_list = wait.until(ExCon.presence_of_all_elements_located((By.TAG_NAME, 'a')), 'LINKS LIST')
broken_links_count = 0

for link in links_list:
    url = link.get_attribute('href')
    res = requests.head(url)
    if res.status_code >= 400:
        print(f'{url} is a broken link')
        broken_links_count += 1
    else:
        print(f'{url} is a valid link')


print(f'Total number of broken links: {broken_links_count}')
