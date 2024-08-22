VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} fMuestraTabla 
   Caption         =   "UserForm1"
   ClientHeight    =   5136
   ClientLeft      =   48
   ClientTop       =   396
   ClientWidth     =   8748.001
   OleObjectBlob   =   "fMuestraTabla.frx":0000
   StartUpPosition =   1  'Centrar en propietario
End
Attribute VB_Name = "fMuestraTabla"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Public Sub muestraTabla(datosTabla)
    Dim i As Variant
    ' Datos de ejemplo para la tabla
    'Dim datosTabla As Variant
    'datosTabla = table
'    datosTabla = Array(Array("Nombre", "Edad", "Ciudad"), _
'                       Array("Juan", 25, "Madrid"), _
'                       Array("Ana", 30, "Barcelona"), _
'                       Array("Carlos", 22, "Valencia"))
  
    ' Llenar la tabla
    For i = LBound(datosTabla) To UBound(datosTabla)
        Me.ListBox1.AddItem datosTabla(i)
    Next i

End Sub


Private Sub ListBox1_Click()

End Sub
