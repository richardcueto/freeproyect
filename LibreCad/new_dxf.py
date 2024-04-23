import ezdxf
from ezdxf import units

# Crear un nuevo documento DXF
doc = ezdxf.new()

# Set centimeter as document/modelspace units
doc.units = units.M

# Acceder al modelspace
msp = doc.modelspace()
# Agregar entidades al dibujo
line=msp.add_line((0, 0), (1, 0), dxfattribs={"layer": "MyLayer"})
line.rgb = (255, 128, 32) #color

circulo=msp.add_circle(center=(0,0),radius=5,dxfattribs={"layer": "MyLayer"})
line.rgb = (0, 128, 32) #color

# Guardar el archivo DXF
doc.saveas('new_dxf.dxf')