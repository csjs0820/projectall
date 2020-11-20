from openpyxl import *
import numpy

rb = load_workbook("flex_value2.xlsx")
ws =  rb['Sheet1']
get_cells = ws['A1':'A14925']
flexvalue = []
for row in get_cells:
        for cell in row:
            flexvalue.append(cell.value)

#print(flexvalue)

for i in flexvalue:
    for j in range(5):
        



