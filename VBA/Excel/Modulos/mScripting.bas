Attribute VB_Name = "mScripting"
Public cintaOpciones As IRibbonUI
Public second As Integer
Dim señal As Boolean

Sub pCintaOpciones(miRibbon As IRibbonUI)
  Set cintaOpciones = miRibbon
  señal = True
  second = 30
End Sub

Sub pElDni(ByVal control As IRibbonControl)
  Dim scrp As New cScraping
  
  scrp.elDni
End Sub

Sub pInvierte(ByVal control As IRibbonControl)
  Dim scrp As New cScraping
  scrp.invierte
End Sub

Sub pInvierte_01(control As IRibbonControl, ByRef estadoEnabled)
  If señal Then
    señal = False
    estadoEnabled = True
  ElseIf señal = False Then
    señal = True
    estadoEnabled = False
  End If
End Sub

Sub pGroup(control As IRibbonControl, ByRef visible)
  If señal Then
    señal = False
    visible = True
  ElseIf señal = False Then
    señal = True
    visible = False
  End If
End Sub

Sub pruebas()
  Dim scrp As New cScraping
  
  scrp.invierte
End Sub

Sub OnToggleAction(control As IRibbonControl, pressed As Boolean)
  If pressed Then
      MsgBox "Toggle prendido"
'      cintaOpciones.InvalidateControl ("invierte")
      cintaOpciones.InvalidateControl ("otro1")
  Else
      MsgBox "Toggle apagado"
  End If
End Sub

Sub MyCheckboxMacro(control As IRibbonControl, pressed As Boolean)
  If pressed Then
      MsgBox "Check prendido"
  Else
      MsgBox "Check apagado"
  End If
End Sub

Sub MyTextMacro(control As IRibbonControl, ByRef returnedVal)
  
End Sub

Sub MyEditBoxMacro(control As IRibbonControl, text As String)
  second = text
End Sub

Sub MyComboBoxMacro(control As IRibbonControl, text As String)
  If text = "33455" Then
      MsgBox "combo"
  End If
End Sub

Sub MyLauncherMacro(control As IRibbonControl)
  MsgBox "launcher"
End Sub


