Attribute VB_Name = "PDF"
Sub hoja2PDF(control As IRibbonControl)
    Dim Path, name_file As String

    Path = ActiveWorkbook.Path
    name_file = ActiveWorkbook.Name
    name_file = Replace(name_file, ".docx", "")
    name_file = name_file & "_" & Time & "_" & Date & ".pdf"
    name_file = Replace(name_file, ":", ".")
    name_file = Replace(name_file, "/", ".")
    
    ActiveSheet.ExportAsFixedFormat xlTypePDF, Filename:=Path & "\" & _
    name_file, openAfterPublish:=True
End Sub

Sub libro2PDF(control As IRibbonControl)
    Dim Path, name_file As String

    Path = ActiveWorkbook.Path
    name_file = ActiveWorkbook.Name
    name_file = Replace(name_file, ".docx", "")
    name_file = name_file & "_" & Time & "_" & Date & ".pdf"
    name_file = Replace(name_file, ":", ".")
    name_file = Replace(name_file, "/", ".")
    
    ActiveWorkbook.ExportAsFixedFormat xlTypePDF, Filename:=Path & "\" & _
    name_file, openAfterPublish:=True
End Sub

