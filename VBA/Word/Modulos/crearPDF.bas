Attribute VB_Name = "NewMacros"
Sub Crear_PDF()
    Dim Path, name_file As String
    
    Path = ActiveDocument.Path
    name_file = ActiveDocument.Name
    name_file = Replace(name_file, ".docx", "")
    name_file = name_file & "_" & Time & "_" & Date & ".pdf"
    name_file = Replace(name_file, ":", ".")
    name_file = Replace(name_file, "/", ".")
    
    ActiveDocument.ExportAsFixedFormat OutputFileName:=Path & "\" & name_file, ExportFormat:=17
End Sub
