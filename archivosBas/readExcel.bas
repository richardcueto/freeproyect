Attribute VB_Name = "M�dulo1"
Sub readExcel()
Dim wb As Excel.Workbook
Dim ws As Excel.Worksheet

Set wb = Excel.Workbooks.Open("D:\Users\User(D)\Escritorio\freeproyect\Excel\dese�oCasa_1.0.3.xlsm", ReadOnly = True)
Set ws = wb.Sheets("Analisis_Estructural")

ms = ws.Range("B2")

MsgBox ms
End Sub
