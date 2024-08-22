VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "cScraping"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Private miSubtotal As Double
Private Browser As New selenium.ChromeDriver

Public Property Get total() As Double
  total = miSubtotal
End Property

Public Property Let Subtotal(x As Double)
  miSubtotal = x
End Property

Sub esperarCargaCompleta(driver As WebDriver, Optional timeoutInSeconds As Integer = 30)
    Dim startTime As Single
    Dim isComplete As Boolean
    
    startTime = Timer
    isComplete = False
    
    ' Bucle para esperar que la página y todos sus recursos estén completamente cargados
    Do While Timer - startTime < timeoutInSeconds
        On Error Resume Next
        isComplete = (driver.ExecuteScript("return document.readyState") = "complete") And _
                     (driver.ExecuteScript("return jQuery.active") = 0)
        On Error GoTo 0
        
        If isComplete Then Exit Do
        DoEvents
    Loop
    
    If Not isComplete Then
        MsgBox "La página no se cargó completamente en el tiempo especificado.", vbExclamation
        Browser.Quit
    End If
End Sub

Public Sub elDni()
  Dim rng As Range
  Dim FindBy As New selenium.By
  
  Set rng = Selection
  
  Browser.Start baseUrl:="https://eldni.com/"
  Browser.Get "/"
  
  If Not Browser.IsElementPresent(FindBy.Class("form-input"), 3000) Then
    Browser.Quit
    MsgBox "no encontrado input", vbInformation
    Exit Sub
  End If
  
  For Each celda In rng
    Browser.FindElementByClass("form-input").SendKeys celda
   
    If Not Browser.IsElementPresent(FindBy.ID("btn-buscar-datos-por-dni"), 3000) Then
      Browser.Quit
      MsgBox "no encontrado bottom", vbInformation
      Exit Sub
    End If
    
    Browser.FindElementById("btn-buscar-datos-por-dni").Click
    
    If Not Browser.IsElementPresent(FindBy.ID("completos"), 3000) Then
      Browser.Quit
      MsgBox "no encontrado bottom", vbInformation
      Exit Sub
    End If
    
    nombre = Browser.FindElementById("completos").Value
    
    celda.Offset(0, 1).Value = nombre
  Next
  Browser.Quit
End Sub

Public Sub invierte()
  Dim rng As Range
  Dim FindBy As New selenium.By
  
  Set rng = Selection
  
  Browser.Start "chrome"
  For Each celda In rng
    Browser.Get "https://ofi5.mef.gob.pe/ssi/Ssi/Indexm/1000/"
    'Esperar carga de pagina
    esperarCargaCompleta Browser, second
    
    If Not Browser.IsElementPresent(FindBy.ID("txt_cod"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado Input", vbInformation
      Exit Sub
    End If
    Browser.FindElementById("txt_cod").SendKeys celda
  
    If Not Browser.IsElementPresent(FindBy.Css("span[role='button'] img.img_tabs"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado Bottom", vbInformation
      Exit Sub
    End If
    Browser.FindElementByCss("span[role='button'] img.img_tabs").Click
    
    esperarCargaCompleta Browser, second
    '# Traer Datos
    '1
    If Not Browser.IsElementPresent(FindBy.ID("td_snip"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 1", vbInformation
      Exit Sub
    End If
    snip = Browser.FindElementById("td_snip").text
    
    '2
    If Not Browser.IsElementPresent(FindBy.ID("td_fecreg"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 2", vbInformation
      Exit Sub
    End If
    fechaReg = Browser.FindElementById("td_fecreg").text
    
    '3
    If Not Browser.IsElementPresent(FindBy.ID("td_estcu"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 3", vbInformation
      Exit Sub
    End If
    nombInversion = Browser.FindElementById("td_estcu").text
    
    '4
    If Not Browser.IsElementPresent(FindBy.ID("td_tipinv"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 4", vbInformation
      Exit Sub
    End If
    montViab = Browser.FindElementById("td_tipinv").text
    
    '5
    If Not Browser.IsElementPresent(FindBy.ID("td_indpmi"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 5", vbInformation
      Exit Sub
    End If
    isPmi = Browser.FindElementById("td_indpmi").text
    
    '6
    If Not Browser.IsElementPresent(FindBy.ID("td_situinv"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 6", vbInformation
      Exit Sub
    End If
    sitVia = Browser.FindElementById("td_situinv").text
    
    '7
    If Not Browser.IsElementPresent(FindBy.ID("td_fecviab"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 7", vbInformation
      Exit Sub
    End If
    fecVia = Browser.FindElementById("td_fecviab").text
    
    '9
    If Not Browser.IsElementPresent(FindBy.ID("td_benif"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 9", vbInformation
      Exit Sub
    End If
    benef = Browser.FindElementById("td_benif").text
    
    '10
    If Not Browser.IsElementPresent(FindBy.ID("td_indseg"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 10", vbInformation
      Exit Sub
    End If
    seg = Browser.FindElementById("td_indseg").text
    
    '11
    If Not Browser.IsElementPresent(FindBy.ID("val_cta"), 3000) Then
      Browser.Quit
      MsgBox "No encontrado 11", vbInformation
      Exit Sub
    End If
    montAct = Browser.FindElementById("val_cta").text
    
    celda.Offset(0, 1).Value = snip
    celda.Offset(0, 2).Value = fechaReg
    celda.Offset(0, 3).Value = nombInversion
    celda.Offset(0, 4).Value = montViab
    celda.Offset(0, 5).Value = isPmi
    celda.Offset(0, 6).Value = sitVia
    celda.Offset(0, 7).Value = fecVia
    celda.Offset(0, 9).Value = benef
    celda.Offset(0, 10).Value = seg
    celda.Offset(0, 11).Value = montAct
  Next
  Browser.Quit
End Sub
