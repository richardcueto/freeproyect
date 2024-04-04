import openseespy.opensees as ops
from numpy import pi

#         modelo  dimensiones grados de libertad
ops.model('basic','-ndm',2,'-ndf',2)

# 		  ntag x y
ops.node(1,0,0)
ops.node(2,1,0)
ops.node(3,1,1)

# 		tag x y
ops.fix(1,1,1)
ops.fix(2,0,1)

secTag_circular=1
E=200.e9
phi=400.e-3
t=4.e-3
A=pi*(phi/2)**2-pi*(phi/2-t)**2
Iz=0.0
ops.section('Elastic',secTag_circular,E,A,Iz)
ops.element('TrussSection',1,1,2,secTag_circular)
ops.element('TrussSection',2,2,3,secTag_circular)
ops.element('TrussSection',3,1,3,secTag_circular)

#times series
tsTag=1
ops.timeSeries('Constant', tsTag,'-factor',1)

#load pattern
patternTag=1
ops.pattern('Plain', patternTag, tsTag,'-factor',1)

#carga
fx=0.
fy=-10e-3
ops.load(3,fx,fy)
ops.load(2,20e10,0)

# ------------------------------
# Start of analysis generation
# ------------------------------

# create SOE
ops.system("BandSPD")

# create DOF number
ops.numberer("RCM")

# create constraint handler
ops.constraints("Plain")

# create integrator
ops.integrator("LoadControl", 1.0)

# create algorithm
ops.algorithm("Linear")

# create analysis object
ops.analysis("Static")

# perform the analysis
ops.analyze(1)

ops.printModel()
# for nodo in range(1,4):
#   d=ops.nodeDisp(nodo)
#   print(f"el nodo {nodo} se desplaza {d}")

# for elemento in range(1,4):
#   f=ops.eleResponse(elemento,"axialForce")
#   print(f"elemento {elemento} resiste una fuerza de {f}")

