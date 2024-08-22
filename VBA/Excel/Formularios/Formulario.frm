VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Formulario 
   Caption         =   "UserForm1"
   ClientHeight    =   6636
   ClientLeft      =   48
   ClientTop       =   396
   ClientWidth     =   11280
   OleObjectBlob   =   "Formulario.frx":0000
   StartUpPosition =   1  'Centrar en propietario
End
Attribute VB_Name = "Formulario"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub CheckBox1_Click()
  Range("H1") = CheckBox1.Value
End Sub


Private Sub ComboBox1_Change()

End Sub

Private Sub CommandButton1_Click()

End Sub

Private Sub ListBox1_Click()

End Sub

Private Sub OptionButton1_Click()
  Range("H2") = OptionButton1.Value
End Sub

Private Sub UserForm_Initialize()
  ComboBox1.AddItem "Mi primera chamba"
  ListBox1.AddItem "mi primera chamba"
  TextBox1.Value = "mi primera chamba"
  Image2.BorderColor = RGB(0, 0, 0)
  
End Sub

