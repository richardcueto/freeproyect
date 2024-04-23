import openseespy.opensees as ops

# ------------------------------
# Empezamos a generar el modelo
# -----------------------------

# regenera model
ops.wipe()

# modelo constructor
ops.model('basic','-ndm',2,'-ndf',2)

# creamos nodos
#     ntag,x,y
ops.node(1, 0, 0, 0)
ops.node(2, 4, 0, 0)
ops.node(3, 8, 0, 0)
ops.node(4, 12, 0, 0)
ops.node(5, 2, 1.1560693641618, 0)
ops.node(6, 6, 3.4682080924855, 0)
ops.node(7, 10, 1.1560693641618, 0)

# establecemos condicion de restriccion
#    ntag,x,y
ops.fix(1,1,1)
ops.fix(4,0,1)



# definimos elementos
eleType = 'truss'
# element(eleType, eleTag, *eleNodes,sectTag)
ops.element(eleType,1, 1, 5,secTag)
ops.element(eleType,2, 6, 5,secTag)
ops.element(eleType,3, 5, 2,secTag)
ops.element(eleType,4, 6, 7,secTag)
ops.element(eleType,5, 4, 7,secTag)
ops.element(eleType,6, 7, 3,secTag)
ops.element(eleType,7, 2, 3,secTag)
ops.element(eleType,8, 6, 2,secTag)
ops.element(eleType,9, 6, 3,secTag)
ops.element(eleType,10, 1, 2,secTag)
ops.element(eleType,11, 3, 4,secTag)

# creamos una serie de tiempo
#                 tsType,tsTag,*
ops.timeSeries('Constant', 1,'-factor',1)

# creamos un patron de carga simple
#       patternType,patternTag,tsTag,*
ops.pattern('Plain', 1, 1,'-factor',1)

#carga puntual   
#       ntag,fx,fy
ops.load(5,0,-3)
ops.load(6,0,-2)
ops.load(7,0,-3)
  

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

# for node in ops.getNodeTags():
#   d=ops.nodeDisp(node)
#   # f=ops.nodeReaction(node)
#   print(f"el nodo {node} se desplaza: {d}")
#   # print(f"el nodo {node} tiene reaccion: {f}")

# for ele in ops.getEleTags():
#     a=ops.eleResponse(ele,"axialForce")
#     print(f"el elemento {ele} tiene fuerza axial: {a}")
print(ops.nodeReaction(4))