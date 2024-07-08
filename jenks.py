from openpyxl import load_workbook 
from jenkspy import JenksNaturalBreaks

workbook = load_workbook(filename='dados.xlsx')
sheet = workbook.active
indicate_column = 'B'
next_line = 1

lista = []

while sheet[f"{indicate_column}{next_line}"].value is not None:
    lista.append(sheet[f"{indicate_column}{next_line}"].value)
    next_line += 1

workbook.save('dados.xlsx')