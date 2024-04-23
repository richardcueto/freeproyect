import openseespy.opensees as ops
# ------------------------------
# Empezamos a generar el modelo
# -----------------------------

# wipe model
ops.wipe()

# modelo constructor
ops.model('basic','-ndm',2,'-ndf',2)

# definimos materiales
E=1000 #tn/cm2
#   uniaxialMaterial('Elastic', matTag, E, eta=0.0, Eneg=E)
ops.uniaxialMaterial('Elastic',1,E)

# creamos nodos
#     ntag,x,y
ops.node(1,0,0)
ops.node(2,3.6,0)
ops.node(3,0,2.7)
ops.node(4,3.6,2.7)

# establecemos condicion de restriccion
#    ntag,x,y
ops.fix(1,1,1)
ops.fix(2,0,0)
ops.fix(3,1,1)
ops.fix(4,1,1)

# definimos elementos
A1=15 #cm2
A2=10 #cm
#   element('Truss', eleTag, *eleNodes, A, matTag, <'-rho', rho>, <'-cMass', cFlag>, <'-doRayleigh', rFlag>)
ops.element('Truss', 1,1,2,A1,1)
ops.element('Truss', 2,2,3,A2,1)
ops.element('Truss', 3,2,4,A2,1)

# creamos una serie de tiempo
#                 tsType,tsTag,*
ops.timeSeries('Constant', 1)

# creamos un patron de carga simple
#       patternType,patternTag,tsTag,*
ops.pattern('Plain', 1, 1)

#carga   
#       ntag,fx,fy
ops.load(2,0,-10)

ops.recorder('Node', '-file', 'NodeDisp.out','-time','-node',2,'-dof',1,2,'disp')
ops.recorder('Node', '-file', 'reaction.out','-time','-node',2,'-dof',1,2,'reaction')
ops.recorder('Element', '-file', 'element.out','-time','-ele',2,'-dof',1,2,'forces')
# ------------------------------
# Start of analysis generation
# ------------------------------

ops.system("BandSPD")
ops.numberer("RCM")
ops.constraints("Plain")
ops.integrator("LoadControl", 1.0)
ops.algorithm("Linear")
ops.analysis("Static")
ops.analyze(1)

for node in ops.getNodeTags():
  d=ops.nodeDisp(node)
  # f=ops.nodeReaction(node)
  print(f"el nodo {node} se desplaza: {d}")
  # print(f"el nodo {node} tiene reaccion: {f}")

for ele in ops.getEleTags():
    a=ops.eleResponse(ele,"axialForce")
    print(f"el elemento {ele} tiene fuerza axial: {a}")

