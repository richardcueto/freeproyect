Attribute VB_Name = "noCategoria"
'#####################FUNCIONES#####################
Function predPlacas(vBasal, f´c, L, Optional phi = 0.85)
    'Segun libro Ing.Antonio Blanco y R.N.E Norma E.060 Art. 21.9.3.2
    'Aplicando formula para determinar espesor
    espesor = vBasal / (phi * 0.53 * WorksheetFunction.Power(f´c, 0.5) * L * 0.8)
    predPlacas = espesor
End Function
Function rigidezBarraEmpotradas(E, i, h, Optional g = 0)
    k = 12 * E * i / (WorksheetFunction.Power(h, 3) * (1 + 2 * g))
    rigidezBarraEmpotradas = k
End Function
Function E060_5_2(f´c, ss)
    Dim f´cr As Double
    f´cr = f´c + 2.33 * ss - 35
    E060_5_2 = f´cr
End Function
Function E060_8_2(wc, f´c)
    Dim Ec As Double
    Ec = WorksheetFunction.Power(wc, 1.5) + 0.136 * WorksheetFunction.Power(f´c, 0.5)
    E060_8_2 = Ec
End Function
Function E060_8_3(f´c)
    Dim Ec As Double
    Ec = 15000 * WorksheetFunction.Power(f´c, 0.5)
    E060_8_3 = Ec
End Function
Function E060_9_12(f´c)
    'num. 10_5_1
    Dim f´r As Double
    fr = 2 * WorksheetFunction.Power(f´c, 0.5)
    E060_9_12 = fcr
End Function
Function E060_9_16(fy, beta, alfafm)
    Dim h As Double
    h = WorksheetFunction.ln(0.8 + fy / 14000) / (36 + 5 * beta * (alfafm - 0.2))
    E060_9_16 = h
End Function
Function E060_9_17(fy, beta)
    Dim h As Double
    h = WorksheetFunction.ln(0.8 + fy / 14000) / (36 + 9 * beta)
    E060_9_17 = h
End Function
Function E060_9_20(fs, Cc)
    's<=38(2500/fs)-2.5Cc
    Dim s As Double
    s = 38 * (2500 / fs) - 2.5 * Cc
    E060_9_20 = s
End Function
Function E060_9_21(fs)
    's<=30(2500/fs)
    Dim s As Double
    s = 30 * (2500 / fs)
    E060_9_21 = s
End Function
Function E060_10_3(f´c, bw, d, fy)
    's<=30(2500/fs)
    Dim s As Double
    Asmin = 0.7 * WorksheetFunction.Power(f´c, 0.5) * bw * d / fy
    E060_10_3 = Asmin
End Function
Function E060_11_3(f´c, bw, d)
    Vc = 0.53 * WorksheetFunction.Power(f´c, 0.5) * bw * d
    E060_11_3 = Vc
End Function
Function E060_11_4(f´c, bw, d, Nu, Ag)
    Vc = 0.53 * WorksheetFunction.Power(f´c, 0.5) * (1 + Nu / (140 * Ag)) * bw * d
    E060_11_4 = Vc
End Function
Function E060_11_5(f´c, bw, d, den_w, Vu, Mu)
    Vc = (0.5 * WorksheetFunction.Power(f´c, 0.5) + 176 * den_w * Vu * d / Mu) * bw * d
    If Not Vc < 0.93 * WorksheetFunction.Power(f´c, 0.5) * bw * d Then
        Vc = "Excede 0.93*f´c^0.5*bw*d"
    End If
    E060_11_5 = Vc
End Function
Function E060_11_7(f´c, bw, d, Nu, Ag)
    Vc = 0.93 * WorksheetFunction.Power(f´c, 0.5) * bw * d * WorksheetFunction.Power(1 + Nu / (35 * Ag), 0.5)
    E060_11_7 = Vc
End Function
Function E060_11_8(f´c, bw, d, Nu, Ag)
    Vc = 0.53 * WorksheetFunction.Power(f´c, 0.5) * (1 - Nu / (35 * Ag)) * bw * d
    E060_11_8 = Vc
End Function
Function E060_11_9(f´c, bw, d, dp, Vu, Mu)
    Vc = (0.16 * WorksheetFunction.Power(f´c, 0.5) + 49 * Vu * dp / Mu) * bw * d
    E060_11_9 = Vc
End Function
Function E060_11_10(f´c, bw, dp, Vd, Vi, Mcre, Mmax)
    Vci = 0.16 * WorksheetFunction.Power(f´c, 0.5) * bw * dp + Vd + Vi * Mcre / Mmax
    E060_11_10 = Vci
End Function
Function E060_11_11(i, Yt, f´c, fpe, fd)
    Mcre = (i / Yt) * (1.6 * WorksheetFunction.Power(f´c, 0.5) + fpe - fd)
    E060_11_11 = Mcre
End Function
Function E060_11_12(f´c, fpc, bw, dp, Vp)
    Vcw = (0.93 * WorksheetFunction.Power(f´c, 0.5) + 0.3 * fpc) * bw * dp + Vp
    E060_11_12 = Vcw
End Function
Function E060_11_13(f´c, bw, s, fyt)
    Avmin = 0.2 * WorksheetFunction.Power(f´c, 0.5) * bw * s / fyt
    If Avmin < 3.5 * bw * s / fyt Then
        Avmin = "No debe ser menor que 3.5*bw*s/fyt"
    End If
    E060_11_13 = Avmin
End Function
Function E060_11_17(f´c, bw, d, Av, alfa, fyt)
    Vs = Av * fyt * Math.Sin(alfa)
    If Not Vs <= 0.8 * WorksheetFunction.Power(f´c, 0.5) * bw * d Then
        Vs = "No debe ser mayor que 0.8*f´c^0.5*bw*d"
    End If
    E060_11_17 = Vs
End Function
'#####################PROCEDIMIENTOS#####################
Sub predimensionViga()
Attribute predimensionViga.VB_Description = "Este procedimiento predimensiona las dimensiones bxh de una viga para una luz libre dada."
Attribute predimensionViga.VB_ProcData.VB_Invoke_Func = " \n14"
    'Segun libro Ing.Antonio Blanco y R.N.E Norma E.060 art 21.5.1.3
    Dim celda As Range
    Dim h1, h2, b1, b2 As Double
    L = InputBox("Ingrese longitud de luz libre", "Luz libre")
    Set celda = Range(InputBox("Ingrese celda donde colocaremos comentario", "Celda"))
    If celda.Comment Is Nothing Then
        celda.AddComment
    End If
    h1 = Round(L / 10, 2): h2 = Round(L / 12, 2)
    b1 = Round(h1 * 0.3, 2): b2 = Round(h2 * 0.5, 2)
    Select Case L
        Case Is <= 5.5
             celda.Comment.Text "h1: " & h1 & ",h2: " & h2 & vbLf & "b1: " & b1 & ",b2: " & b2 & vbLf & "Dimensiones de vigas usuales: " & "25x50,30x50"
        Case Is <= 6.5
             celda.Comment.Text "h1: " & h1 & ",h2: " & h2 & vbLf & "b1: " & b1 & ",b2: " & b2 & vbLf & "Dimensiones de vigas usuales: " & "25x60,30x60,40x60"
        Case Is <= 7.5
             celda.Comment.Text "h1: " & h1 & ",h2: " & h2 & vbLf & "b1: " & b1 & ",b2: " & b2 & vbLf & "Dimensiones de vigas usuales: " & "25x70,30x70,40x70,50x70"
        Case Is <= 8.5
             celda.Comment.Text "h1: " & h1 & ",h2: " & h2 & vbLf & "b1: " & b1 & ",b2: " & b2 & vbLf & "Dimensiones de vigas usuales: " & "30x75,40x75,30x80,40x80"
        Case Is <= 9.5
             celda.Comment.Text "h1: " & h1 & ",h2: " & h2 & vbLf & "b1: " & b1 & ",b2: " & b2 & vbLf & "Dimensiones de vigas usuales: " & "30x85,30x90,40x85,40x90"
    End Select
    With celda.Comment.Shape
        .TextFrame.AutoSize = True
    End With
End Sub
Sub predimensionLosaALigerda()
    predLosa.Show
End Sub
Sub predLosaMaciza(Lmayor, Lmenor, Haligerado)
    'Segun libro Ing.Antonio Blanco y R.N.E Norma E.060 Art. 9.6.3.2
    Dim celda As Range
    Set celda = Application.Caller
    If celda.Comment Is Nothing Then
        celda.AddComment
    End If
    'primer criterio:Espesor minimo
    emin = Lmayor / 40
    'segundo criterio:Espesor maximo
    emax = Haligerado - 0.05
    'relacion beta=lmayor/lmenor
    beta = Lmayor / Lmenor
    If beta >= 2 Then
        celda.Comment.Text "losa en una direccion:" & vbLf & "h = " & Lmayor / 30
    Else
        celda.Comment.Text "losa en dos direcciones:" & vbLf & "h = " & Lmayor / 40 & " o " & Round((Lmayor + Lmenor) / 90, 2)
    End If
    With celda.Comment.Shape
        .TextFrame.AutoSize = True
        .Width = 150
        .TextFrame.Characters.Font.Bold = False
    End With
End Sub
Function predColumna(ubiColum, catEdif, areaT, Npisos, Optional f´c = 210)
    'Segun libro Ing.Antonio Blanco
    'categoria A=1500kg/m2
    'categoria B=1250kg/m2
    'categoria C=1000kg/m2
    Dim P As Double
    Dim celda As Range
    Set celda = Application.Caller
    If celda.Comment Is Nothing Then
        celda.AddComment
    End If
    Select Case catEdif
        Case "A"
            P = 1500
        Case "B"
            P = 1250
        Case "C"
            P = 1000
    End Select
    Select Case ubiColum
        Case "columna centrada"
            areaRequerida = Round(P * areaT * Npisos / (0.45 * f´c), 2)
            celda.Comment.Text "Area Requerida: " & areaRequerida & "cm2" & vbLf & "Dimensiones de columnas: " & "25x50,30x60,30x40,30x50"
        Case "columna esquinada"
            areaRequerida = Round(P * areaT * Npisos / (0.35 * f´c), 2)
            celda.Comment.Text "Area Requerida: " & areaRequerida & "cm2" & vbLf & "Dimensiones de columnas: " & "25x50,30x60,30x40,30x50"
    End Select
    With celda.Comment.Shape
        .TextFrame.AutoSize = True
        .Width = 150
        .TextFrame.Characters.Font.Bold = False
    End With
    predColumna = areaRequerida
End Function
Function viga2009(h, d, db, de)
Attribute viga2009.VB_Description = "Predimensionamiento de la viga"
Attribute viga2009.VB_ProcData.VB_Invoke_Func = " \n14"
    'requisitos para vigas con sistema resistente de muros (R=6) y dual tipo I(E0.060-2009)
    Dim confinamiento As Double
    Dim celda As Range
    Set celda = Application.Caller
    If celda.Comment Is Nothing Then
        celda.AddComment
    End If
    confinamiento = 2 * h
    celda.Comment.Text "a) " & d / 4 & "mm o 150mm" & vbLf & _
    "b): " & 10 * db & vbLf & _
    "c): " & 24 * de & vbLf & _
    "d): 300mm" & vbLf & _
    "valor minimo: " & WorksheetFunction.Min(d / 4, 150, 10 * db, 24 * de, 300) & vbLf & _
    "confinamiento" & confinamiento & vbLf & _
    "cantidad: " & confinamiento / WorksheetFunction.Min(d / 4, 150, 10 * db, 24 * de, 300)
    With celda.Comment.Shape
        .TextFrame.AutoSize = True
        .Width = 150
        .Height = 90
        .TextFrame.Characters.Font.Bold = False
    End With
End Function
Function viga2019(h, d, db, de)
    'requisitos para vigas con sistema resistente de muros (R=6) (E0.060-2019)
    Dim confinamiento As Double
    Dim celda As Range
    Set celda = Application.Caller
    If celda.Comment Is Nothing Then
        celda.AddComment
    End If
    confinamiento = 2 * h
    celda.Comment.Text "a) " & d / 4 & "mm o 100mm" & vbLf & _
    "b): " & 8 * db & vbLf & _
    "c): " & 24 * de & vbLf & _
    "d): 300mm" & vbLf & _
    "valor minimo: " & WorksheetFunction.Min(d / 4, 150, 10 * db, 24 * de, 300) & vbLf & _
    "confinamiento" & confinamiento & vbLf & _
    "cantidad: " & confinamiento / WorksheetFunction.Min(d / 4, 150, 10 * db, 24 * de, 300)
    With celda.Comment.Shape
        .TextFrame.AutoSize = True
        .Width = 150
        .Height = 90
        .TextFrame.Characters.Font.Bold = False
    End With
End Function





