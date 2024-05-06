Attribute VB_Name = "Módulo1"
Sub AbrirAutoCAD()
    pto = AutoCAD.Application.ActiveDocument.Utility.GetPoint(, "indique punto")
    x = pto(0): y = pto(1)
    
    ancho = Hoja2.Cells(1, 2)
    largo = Hoja2.Cells(2, 2)
    
Call dibujo(x, y, ancho, largo)
End Sub

Sub dibujo(x, y, ancho, largo)
Dim polrec(0 To 11) As Double
Dim rectangulo As AcadPolyline

polrec(0) = x: polrec(1) = y
polrec(3) = x + ancho: polrec(4) = y
polrec(6) = x + ancho: polrec(7) = y - largo
polrec(9) = x: polrec(10) = y - largo

Set rectangulo = AutoCAD.Application.ActiveDocument.ModelSpace.AddPolyline(polrec)
rectangulo.Closed = True

End Sub
