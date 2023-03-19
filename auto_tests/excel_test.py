import openpyxl


file_excel = "test_data/file_example_XLSX_100.xlsx"
workbook = openpyxl.load_workbook(file_excel)
sheet = workbook["Sheet1"]
number_of_rows = sheet.max_row  # 101
number_of_columns = sheet.max_column  # 8

print(f'Sheet max row: {number_of_rows}')
print(f'Sheet max column: {number_of_columns}')

for row in range(1, number_of_rows + 1):
    for column in range(1, number_of_columns + 1):
        print(sheet.cell(row, column).value, end='  ')
    print()
