from __future__ import print_function
import pandas as pd
from openpyxl import load_workbook

wb = load_workbook(filename='data/climate_change_download_0.xlsx')
ws = wb.get_sheet_by_name('Data')

for row in ws.rows:
    for cell in row:
        print(cell.value)

df = pd.read_excel('data/climate_change_download_0.xlsx')
print(df)
