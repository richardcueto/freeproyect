Attribute VB_Name = "Módulo1"
Sub TestSelenium()
  
  Dim rng As Range
  Dim FindBy As New Selenium.By
  Dim Browser As New Selenium.ChromeDriver
  
  Set rng = Selection
  
  Browser.Start baseUrl:="https://eldni.com/"
  Browser.Get "/"
  
  If Not Browser.IsElementPresent(FindBy.class("form-input"), 3000) Then
    Browser.Quit
    MsgBox "no encontrado input", vbInformation
    Exit Sub
  End If
  
  For Each celda In rng
    Browser.FindElementByclass("form-input").SendKeys celda
  
  
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
	Browser.FindElementByTag("i").Click
  Next

End Sub
