import openseespy.opensees as ops

# ------------------------------
# Empezamos a generar el modelo
# -----------------------------

# modelo constructor
ops.model('basic','-ndm',2,'-ndf',2)

# creamos nodos
#     ntag,x,y
ops.node(1,0,0)
ops.node(2,1,0)

# establecemos condicion de restriccion
#    ntag,x,y
ops.fix(1,1,1)
ops.fix(2,0,1)

# definimos materiales
#             secType,secTag,E,A,Iz
ops.section('Elastic',1,5,1,0 )

# definimos elementos
#                 eleType,eletag,eleNodes,secTag
ops.element('TrussSection', 1,1,2,1)

# creamos una serie de tiempo
#                 tsType,tsTag,*
ops.timeSeries('Constant', 1,'-factor',1)

# creamos un patron de carga simple
#       patternType,patternTag,tsTag,*
ops.pattern('Plain', 1, 1,'-factor',1)

#carga   
#       ntag,fx,fy
ops.load(2,1,0)

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

d=ops.nodeDisp(2)
print(f"el nodo 2 se desplaza {d}")