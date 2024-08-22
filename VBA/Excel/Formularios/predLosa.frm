VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} predLosa 
   Caption         =   "Predimensionamiento de Losa"
   ClientHeight    =   2880
   ClientLeft      =   108
   ClientTop       =   456
   ClientWidth     =   3612
   OleObjectBlob   =   "predLosa.frx":0000
   StartUpPosition =   1  'Centrar en propietario
End
Attribute VB_Name = "predLosa"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
    'Segun libro Ing.Antonio Blanco y R.N.E Norma E.060
    Dim vcelda As String
    Dim L As Double
    Dim h As Double
    L = TextBox1.Value
    vcelda = TextBox2.Value
    Unload Me
    'L = InputBox("Ingrese longitud de luz libre", "Luz libre" & vbCrLf & "ingrese otro")
    Set celda = Range(vcelda)
    If celda.Comment Is Nothing Then
        celda.AddComment
    End If
    h = Round(L / 25, 2)
    Select Case L
        Case Is <= 4
             celda.Comment.Text "h: " & h & vbLf & "Dimensiones de losa aligerada: " & "0.17m"
        Case Is <= 5
            celda.Comment.Text "h: " & h & vbLf & "Dimensiones de losa aligerada: " & "0.20m"
        Case Is <= 6
            celda.Comment.Text "h: " & h & vbLf & "Dimensiones de losa aligerada: " & "0.25m"
        Case Is <= 7
            celda.Comment.Text "h: " & h & vbLf & "Dimensiones de losa aligerada: " & "0.30m" & "o tambien puede usar losas nervadas"
    End Select
    With celda.Comment.Shape
        .TextFrame.AutoSize = True
    End With
End Sub

Private Sub label1_Click()

End Sub

Private Sub Label2_Click()

End Sub
