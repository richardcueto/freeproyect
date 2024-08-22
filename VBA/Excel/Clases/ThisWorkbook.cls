VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisWorkbook"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Private Sub Workbook_Open()
    'E020
'    Application.MacroOptions Macro:="predViga", Description:="Predimensionamiento de la viga", Category:="Pedimensionamiento", ArgumentDescriptions:="Luz libre"
   
    
    'E030
    Application.MacroOptions Macro:="tabla1_E030_10_2", Description:="Zonificación", Category:="E030", ArgumentDescriptions:="Zona"
    Application.MacroOptions Macro:="perfil_E030_10_2", Description:="Obtener el perfil del suelo", Category:="E030", ArgumentDescriptions:=Array("Velocidad de onda", "Numero de golpes", "Su")
    Application.MacroOptions Macro:="tabla3_S_E030_13", Description:="Suelo(S)", Category:="E030", ArgumentDescriptions:=Array("Perfil de suelo", "Zona")
    Application.MacroOptions Macro:="tabla4_Tp_E030_13", Description:="Tp", Category:="E030", ArgumentDescriptions:=Array("Perfil de suelo")
    Application.MacroOptions Macro:="tabla4_TL_E030_13", Description:="TL", Category:="E030", ArgumentDescriptions:=Array("Perfil de suelo")
    Application.MacroOptions Macro:="C_E030_14", Description:="Coeficiente de amplificación sismica", Category:="E030", ArgumentDescriptions:=Array("periodo natural", "perdiodo plataforma", "periodo largo")
    Application.MacroOptions Macro:="tabla5_E030_15", Description:="Categoria(U)", Category:="E030", ArgumentDescriptions:=Array("U")
    Application.MacroOptions Macro:="tabla7_R0_E030_18", Description:="Sistema estructural para R0", Category:="E030", ArgumentDescriptions:=Array("Sistema estructural")
    Application.MacroOptions Macro:="tabla8_factor_Ia_E030_20", Description:="Factor que se aplica a irregularidad en altura", Category:="E030", ArgumentDescriptions:=Array("Irregularidad en altura")
    Application.MacroOptions Macro:="tabla9_factor_Ip_E030_20", Description:="Factor que se aplica a irregularidad en planta", Category:="E030", ArgumentDescriptions:=Array("Irregularidad en planta")
    Application.MacroOptions Macro:="R_E030_22", Description:="Calcula el factor de reducción", Category:="E030", ArgumentDescriptions:=Array("Factor de reducción")
    Application.MacroOptions Macro:="V_E030_28", Description:="Calcula la cortante en la base", Category:="E030", ArgumentDescriptions:=Array("Cortante en la base")
    
    'E050
'    Application.MacroOptions Macro:="predColumna", Description:="Predimensionamiento de Columna", Category:="Pedimensionamiento", ArgumentDescriptions:=Array("Ubicación de Columna: columna centrada o columna esquinada", "Categoria del Edificio: A,B,C", "Area tributaria", "Numero de Pisos", "Resistencia a la Compresión del Concreto")
'    Application.MacroOptions Macro:="rigidezBarraEmpotradas", Description:="Predimensionamiento de la viga", ArgumentDescriptions:="Luz libre"
    
    'E060
    
    
    'E070
'    Application.MacroOptions Macro:="viga2009", Description:="Predimensionamiento de la viga", ArgumentDescriptions:="Luz libre"
'    Application.MacroOptions Macro:="E060_5_2", Description:="La resistencia promedio a la compresión requerida,", ArgumentDescriptions:=Array("Resistencia a la Compresión del Concreto", "desviación estandar de la muestra")
'    Application.MacroOptions Macro:="E060_8_2", Description:="Módulo de elasticidad para peso unitario wc comprendido entre 1450 y 2500 kg/m3", ArgumentDescriptions:=Array("Peso unitario", "Resistencia a la Compresión del Concreto")
'    Application.MacroOptions Macro:="E060_8_3", Description:="Módulo de elasticidad para concretos de peso unitario normal (wc „l 2300 kg/m3)", ArgumentDescriptions:="Resistencia a la Compresión del Concreto"
'    Application.MacroOptions Macro:="E060_9_12", Description:="Resistencia del concreto a tracción por flexión (Módulo de Rotura)", ArgumentDescriptions:="Resistencia a la Compresión del Concreto"
'    Application.MacroOptions Macro:="E060_9_16", Description:="El espesor mínimo h para losas con vigas que se extienden entre los apoyos en todos los lados" & vbLf _
'    & "Para 0,2 ƒ<alfafm< 2,0 h no debe ser menor que", ArgumentDescriptions:=Array("Esfuerzo de fluencia", "beta", "afm")
'    Application.MacroOptions Macro:="E060_9_20", Description:="Predimensionamiento de la viga", ArgumentDescriptions:="Luz libre"
End Sub
