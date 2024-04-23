from openpyxl import load_workbook
wb=load_workbook(filename="read_xlsx.xlsx")

#activamos la hoja
ws=wb['E0.30']

ws['C1'].value
ws['C2'].value
ws['C3'].value
ws['C4'].value
ws['C5'].value
ws['C6'].value
ws['C7'].value
ws['B8'].value

