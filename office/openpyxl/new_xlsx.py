from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import PatternFill
wb=Workbook()

#activamos la hoja de trabajo
ws = wb.active

# agregamos color al tab
ws.sheet_properties.tabColor = "1072BA"

#cambiamos nombre a la hoja
ws.title = "E0.30"

ws1 = wb.create_sheet("E0.60") # insert at the end (default)
ws2 = wb.create_sheet("E0.70")

#asignamos valores
ws['A1'] = "seleccionamos el valor de Z"
ws['A2'] = "seleccionamos el valor de U"
ws['A3'] = "seleccionamos el valor de C"
ws['A4'] = "seleccionamos el valor de S"
ws['A5'] = "seleccionamos el valor de R0"
ws['A6'] = "seleccionamos el valor de Ia"
ws['A7'] = "seleccionamos el valor de Ip"

#Datavalition
opciones=['Z1','Z2','Z3','Z4']
dv=DataValidation(type='list',formula1='"'+','.join(opciones)+'"',allow_blank=True)
ws.add_data_validation(dv)
dv.add(ws['B1'])

#celdas con valores
relleno_naranja=PatternFill(start_color='FFA500',end_color='FFA500',fill_type='solid')
relleno_amarillo=PatternFill(start_color='FFFF00',end_color='FFFF00',fill_type='solid')
ws['C1'].fill=relleno_naranja
ws['C2'].fill=relleno_amarillo
ws['C3'].fill=relleno_amarillo
ws['C4'].fill=relleno_amarillo
ws['C5'].fill=relleno_amarillo
ws['C6'].fill=relleno_amarillo
ws['C7'].fill=relleno_amarillo
ws['B8'].fill=relleno_naranja

#condicion y resultados
ws['C1']='=IF(B1="Z1",0.45, IF(B1="Z2",0.35,IF(B1="Z3",0.25,0.10)))'
ws['B8']='=C1*C2*C3*C4/(C5*C6*C7)'

# Save the file
wb.save("new_xlsx.xlsx")
