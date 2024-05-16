import ezdxf
from ezdxf import units

# Crear un nuevo documento DXF
doc = ezdxf.new()

# Set centimeter as document/modelspace units
doc.units = units.M

# Acceder al modelspace
msp = doc.modelspace()

inser_points=[(0,0),
              (5,0),
              (5,10),
              (0,10)
]

# Crear el rectángulo
def rectangle(insert_point,width,height,layer):
  rectangulo=msp.add_lwpolyline([insert_point,
                      (insert_point[0] + width, insert_point[1]),
                      (insert_point[0] + width, insert_point[1] + height),
                      (insert_point[0], insert_point[1] + height),
                      insert_point], close=True,dxfattribs={"layer": layer})
  return rectangulo

for rec in inser_points:
  rectangle(rec,2,2,'frames')

# Guardar el archivo DXF
doc.saveas('new_dxf.dxf')