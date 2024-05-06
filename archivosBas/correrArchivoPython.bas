Attribute VB_Name = "Python"
Sub Python()
Attribute Python.VB_ProcData.VB_Invoke_Func = " \n14"
    Dim rutaPython As String
    Dim rutaScript As String
    Dim comando As String
    
    ' Ruta al ejecutable de Python
    rutaPython = "C:\Python\Python39\python3.9.exe -i"
    
    ' Ruta al script de Python
    rutaScript = "D:\Users\User(D)\Escritorio\freeproyect\Etabs\excel.py"
    
    ' Comando para ejecutar el script de Python
    comando = rutaPython & " " & rutaScript
    VBA.CreateObject("WScript.Shell").Run (comando)
End Sub
