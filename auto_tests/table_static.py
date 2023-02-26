import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from typing import List

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
wait = WebDriverWait(driver, 10, 0.4)

driver.get("https://testautomationpractice.blogspot.com/")
driver.fullscreen_window()

# Count the number of rows in a table
table_rows: List[WebElement] = wait.until(ExCon.presence_of_all_elements_located((By.XPATH, "//table[@name='BookTable']//tr")), "TABLE ROWS")
print(f'Table rows count: {len(table_rows)}')
print('-----')

# Count the number of columns in a table
table_columns: List[WebElement] = wait.until(ExCon.presence_of_all_elements_located((By.XPATH, "//table[@name='BookTable']//tr[1]/th")), "TABLE COLUMNS")
print(f'Table columns count: {len(table_columns)}')
print('-----')

# Get specific table cell - 1st column, 5th row
specific_table_cell: WebElement = wait.until(ExCon.presence_of_element_located((By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]")), "TABLE CELL")
print(f'Cell text (1st column, 5th row): "{specific_table_cell.text}"')
print('-----')

# Read all the rows and columns
for x in range(2, (len(table_rows) + 1)):  # starting from 2nd row, since 1st row = table headers
    print(f'Row #{x}: ', end='')
    for y in range(1, (len(table_columns) + 1)):
        data = wait.until(ExCon.presence_of_element_located((By.XPATH, f"//table[@name='BookTable']//tr[{x}]/td[{y}]")), f"TABLE CELL FROM COLUMN #{x} ROW #{y}")
        # print(f'Cell text from column #{x} row #{y}: {data.text}')
        print(f'| "{data.text}"', end='')
    print()
print('-----')

# Read a required table row
print('Author "Mukesh" is found in: ')
for x in range(2, (len(table_rows) + 1)):  # starting from 2nd row, since 1st row = table headers
    data_author = wait.until(ExCon.presence_of_element_located((By.XPATH, f"//table[@name='BookTable']//tr[{x}]/td[{2}]")), f"AUTHOR")
    if data_author.text == 'Mukesh':
        print(f'Row #{x}: ', end='')
        for y in range(1, (len(table_columns) + 1)):
            data = wait.until(ExCon.presence_of_element_located((By.XPATH, f"//table[@name='BookTable']//tr[{x}]/td[{y}]")), f"TABLE CELL FROM COLUMN #{x} ROW #{y}")
            print(f'| "{data.text}"', end='')
        print()


time.sleep(5)
driver.quit()
