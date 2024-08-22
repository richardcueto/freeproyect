VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "nombclass"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Private miSubtotal As Double

Public Property Get total() As Double
  total = miSubtotal
End Property

Public Property Let Subtotal(x As Double)
  miSubtotal = x
End Property
