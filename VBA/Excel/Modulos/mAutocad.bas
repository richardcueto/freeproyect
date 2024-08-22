Attribute VB_Name = "mAutocad"
Sub muroPrimerPiso()
    pto = AutoCAD.ActiveDocument.Utility.GetPoint(, "seleccione aqui")
    x0 = pto(0): y0 = pto(1)
    Dim ws As Worksheet
    Set ws = ActiveSheet
    'ultimaFila = ws.Cells(20, "B").End(xlUp).Row
    For i = 0 To 10
        Call crearRect(x0, y0, ws.Cells(16 + i, "B"), ws.Cells(16 + i, "C"), ws.Cells(16 + i, "D"), ws.Cells(16 + i, "E"))
    Next
End Sub
Sub muroSegundoPiso()
    pto = AutoCAD.ActiveDocument.Utility.GetPoint(, "seleccione aqui")
    x0 = pto(0): y0 = pto(1)
    Dim ws As Worksheet
    Set ws = ActiveSheet
    ultimaFila = ws.Cells(54, "B").End(xlUp).Row
    For i = 0 To ultimaFila
        Call crearRect(x0, y0, ws.Cells(34 + i, "B"), ws.Cells(34 + i, "C"), ws.Cells(34 + i, "D"), ws.Cells(34 + i, "E"))
    Next
End Sub

Function crearRect(x0, y0, x, y, x_, y_) As AcadPolyline
    
    Dim poliRec(0 To 11) As Double
    Dim rectangulo As AcadPolyline
    poliRec(0) = x0 + x: poliRec(1) = y0 + y
    poliRec(3) = x0 + x: poliRec(4) = y0 + y + y_
    poliRec(6) = x0 + x + x_: poliRec(7) = y0 + y + y_
    poliRec(9) = x0 + x + x_: poliRec(10) = y0 + y
       
    Call creaDim(x0 + x, y0 + y, x0 + x + x_, y0 + y, x0 + x, y0 + y)
    Set rectangulo = AutoCAD.ActiveDocument.ModelSpace.AddPolyline(poliRec)

    With rectangulo
        .Closed = True
        .Update
    End With
    Set crearRect = rectangulo
End Function

Sub creaDim(pt0x, pt0y, pt1x, pt1y, tx, ty)
Dim dimen As AcadDimAligned
Dim starPto(0 To 2) As Double
Dim endPto(0 To 2) As Double
Dim textPto(0 To 2) As Double

starPto(0) = pt0x: starPto(1) = pt0y
endPto(0) = pt1x: endPto(1) = pt1y
textPto(0) = tx: textPto(1) = ty

Set dimen = AutoCAD.ActiveDocument.ModelSpace.AddDimAligned(starPto, endPto, textPto)

With dimen
    .HorizontalTextPosition = acHorzCentered
    .ArrowheadSize = 0.1
    .VerticalTextPosition = acVertCentered
    .TextHeight = 0.2
    .Update
End With

End Sub
Sub viga()

End Sub
Sub columna()

End Sub
Sub estribo(db)
    Dim pto0(0 To 2) As Double
    Dim pto1(0 To 2) As Double
    Dim pto2(0 To 2) As Double
    Dim pto3(0 To 2) As Double
    Dim pto4(0 To 2)  As Double
    Dim R, espx, espy As Double
    pto0(0) = 0: pto0(1) = 0
    R = 5: espx = 50: espy = 50
    'If 8 * db > 75 Then
        pto1(0) = pto0(0) + db + R: pto1(1) = pto0(1) + db + R
        pto2(0) = pto1(0) + espx: pto2(1) = pto1(1)
        pto3(0) = pto1(0) + espx: pto3(1) = pto1(1) + espy
        pto4(0) = pto1(0): pto4(1) = pto1(1) + espy
        AutoCAD.ActiveDocument.ModelSpace.AddCircle pto1, R
        AutoCAD.ActiveDocument.ModelSpace.AddCircle pto2, R
        AutoCAD.ActiveDocument.ModelSpace.AddCircle pto3, R
        AutoCAD.ActiveDocument.ModelSpace.AddCircle pto4, R
        Dim rectangulo As AcadPolyline
        Set rectangulo = crearRect(pto0(0), pto0(1), db, db, 2 * R + espx, 2 * R + espy)
        rectangulo.Offset -db
        Dim pto5(0 To 2) As Double
        Dim pto6(0 To 2) As Double
        Dim linea As AcadLine
        pto5(0) = pto4(0): pto5(1) = pto4(1) + R
        pto6(0) = pto4(0): pto6(1) = pto4(1) + R + 8 * db
        Set linea = AutoCAD.ActiveDocument.ModelSpace.AddLine(pto5, pto6)
        linea.Rotate pto5, -3.14 * 3 / 4
        linea.Offset -2 * R
'    Else
'    End If
End Sub
Sub pruebas()
    estribo (5)
End Sub
