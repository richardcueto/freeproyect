from openseespy.opensees import *
import numpy as np
import matplotlib.pyplot as plt
# ------------------------------
# Empezamos a generar el modelo
# -----------------------------

# wipe model
wipe()

# modelo constructor
model('basic','-ndm',2,'-ndf',2)

# definimos materiales
E=1 #tn/cm2
#   uniaxialMaterial('Elastic', matTag, E, eta=0.0, Eneg=E)
uniaxialMaterial('Elastic',1,E)

# creamos nodos
#     ntag,x,y
node(1,0,0) 
node(2,2,0)
node(3,2,2)
node(4,0,2)

# establecemos condicion de restriccion
#    ntag,x,y
fix(1,0,0)
fix(2,1,0)
fix(3,1,1)
fix(4,0,0)

# definimos elementos
A=1 #cm2
#   element('Truss', eleTag, *eleNodes, A, matTag, <'-rho', rho>, <'-cMass', cFlag>, <'-doRayleigh', rFlag>)
element('Truss',1,1,2,A,1)
element('Truss',2,1,3,A,1)
element('Truss',3,1,4,A,1)
element('Truss',4,4,3,A,1)
element('Truss',5,2,4,A,1)
element('Truss',6,2,3,A,1)

# creamos una serie de tiempo
#                 tsType,tsTag,*
timeSeries('Constant', 1)

# creamos un patron de carga simple
#       patternType,patternTag,tsTag,*
pattern('Plain', 1, 1)

#carga   
#       ntag,fx,fy
load(4,2,-4)

# recorder('Node', '-file', 'NodeDisp.out','-time','-node',2,'-dof',1,2,'disp')
# recorder('Node', '-file', 'reaction.out','-time','-node',2,'-dof',1,2,'reaction')
# recorder('Element', '-file', 'element.out','-time','-ele',2,'-dof',1,2,'forces')
# ------------------------------
# Start of analysis generation
# ------------------------------

system("BandSPD")
numberer("RCM")
constraints("Plain")
integrator("LoadControl", 1.0)
algorithm("Linear")
analysis("Static")
analyze(1)

scale=10
D=0.2

for node in getNodeTags():
  d=nodeDisp(node)
  # f=nodeReaction(node)
  print(f"el nodo {node} se desplaza: {d}")
  # print(f"el nodo {node} tiene reaccion: {f}")

for ele in getEleTags():
    a=eleResponse(ele,"axialForce")
    print(f"el elemento {ele} tiene fuerza axial: {a}")

def plot():
  for node in getNodeTags():
    if True:
      plt.scatter(nodeCoord(node)[0],nodeCoord(node)[1],color='red',label=node)
      plt.text(nodeCoord(node)[0],nodeCoord(node)[1],node,ha='left',va='bottom',fontsize=10)
  
  for ele in getEleTags():
    F=round(eleResponse(ele,"axialForce")[0],2)
    x1,y1=nodeCoord(eleNodes(ele)[0])
    x2,y2=nodeCoord(eleNodes(ele)[1])
    plt.plot([x1,x2],[y1,y2],color='green',linestyle='-')
    deltx=x2-x1
    delty=y2-y1
    x=np.linspace(x1,x2,scale)
    y=np.linspace(y1,y2,scale)
    if deltx==0:
      plt.text(x1,y1+delty/3,ele,ha='left',va='bottom')
      plt.plot(x+D,y,color='blue',linestyle='-')
      plt.text(x1+D,y1+2*delty/3,F,ha='right',va='bottom',fontsize=9) 
    else:
      m=delty/deltx
      plt.text(x1+deltx/3,y1+m*1/3*deltx,ele,ha='left',va='bottom')
      plt.plot(x,y1+m*(x-x1)+D,color='red',linestyle='-')
      plt.fill_between(x,y1+m*(x-x1)+D,y,where=(y1+m*(x-x1)>=y),interpolate=True,color='lightblue',alpha=0.5)
      plt.text(x1+2/3*deltx,y1+m*2/3*deltx+D,F,ha='left',va='bottom',fontsize=9)
    
  plt.title('estructura')
  plt.xlabel('eje x')
  plt.ylabel('eje y')
  plt.grid(True)
  # plt.legend()
  plt.show()
  
plot()
