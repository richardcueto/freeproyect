from openseespy.opensees import *
import numpy as np
import matplotlib.pyplot as plt
import opsvis as opsv
# ------------------------------
# Empezamos a generar el modelo
# -----------------------------

# regenera model
wipe()

# modelo constructor
model('basic','-ndm',2,'-ndf',3)#ndm:dimensiones,ndf:grados de libertad

#uniaxialMaterial('Elastic', matTag, E, eta=0.0, Eneg=E)
E,A,Ic,Iv=20e9,0.09,0.000675,10e12
numModos=2
m=4500
# uniaxialMaterial('Elastic', 1, E)

# #section('Elastic', secTag, E_mod, A, Iz, G_mod=None, alphaY=None
# section('Elastic', 1, E, A, Iz)

#geomTransf('Linear', transfTag, '-jntOffset', *dI, *dJ)
geomTransf('Linear', 1)

# creamos nodos(ndm)
#     ntag,x,y
node(1,0,0)
node(2,8, 0)
node(3,0, 4)
node(4,8, 4)
node(5,0, 8)
node(6,8, 8)

# establecemos condicion de restriccion(dnf)
#    ntag,x,y
fix(1,1,1,1)
fix(2,1,1,1)

mass(3,m,0,0)
mass(4,m,0,0)
mass(5,m/2,0,0)
mass(6,m/2,0,0)

#definimos elementos
#element(eleType, eleTag, *eleNodes,sectTag)
#element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, Iz, transfTag)
element('elasticBeamColumn',1,1,3,A,E,2*Ic,1)
element('elasticBeamColumn',2,3,5,A,E,Ic,1)
element('elasticBeamColumn',3,2,4,A,E,2*Ic,1)
element('elasticBeamColumn',4,4,6,A,E,Ic,1)
element('elasticBeamColumn',5,3,4,A,E,Iv,1)
element('elasticBeamColumn',6,5,6,A,E,Iv,1)
    
eigenvalores=eigen(numModos)
#creamos una serie de tiempo
#timeSeries(tsType, tsTag, *tsArgs)
#timeSeries('Linear', tag, '-factor', factor=1.0, '-tStart', tStart=0.0)
timeSeries('Linear', 1)

#creamos un patron de carga simple
#pattern(patternType, patternTag, *patternArgs)
#pattern('Plain', patternTag, tsTag, '-fact', fact)
pattern('Plain', 1, 1)

#carga puntual   
#       ntag,depende direccion
Px = 2.e+3
Wy = -10.e+3
Wx = 0.

Ew = {5: ['-beamUniform', Wy, Wx]}
for etag in Ew:
  print(etag)
#eleLoad('-ele', *eleTags, '-range', eleTag1, eleTag2, '-type', '-beamUniform', Wy, <Wz>, Wx=0.0, '-beamPoint', Py, <Pz>, xL, Px=0.0, '-beamThermal', *tempPts)
  eleLoad('-ele', etag, '-type', Ew[etag][0], Ew[etag][1],Ew[etag][2])

load(5,Px,Wy,Wx)

# ------------------------------
# Start of analysis generation
# ------------------------------

#       create constraint handler
#constraints(constraintType, *constraintArgs)
#constraints('Plain')
constraints('Plain')

#       create DOF number
#numberer(numbererType, *numbererArgs)
numberer('Plain')
# numberer('RCM')

#       create SOE
#system(systemType, *systemArgs)
system('BandGen')
# system('ProfileSPD')

#       create test
#test(testType, *testArgs)
#test('NormDispIncr', tol, iter, pFlag=0, nType=2)
# test('NormDispIncr', 1e-12,10)

#       create algorithm
#algorithm(algoType, *algoArgs)
#algorithm('Newton', secant=False, initial=False, initialThenCurrent=False)
algorithm('Linear')

#       create integrator
#integrator(intType, *intArgs)
#integrator('LoadControl', incr, numIter=1, minIncr=incr, maxIncr=incr)
integrator('LoadControl', 1.0)

#       create analysis object
#analysis(analysisType)
analysis('Static')

#analyze(numIncr=1, dt=0.0, dtMin=0.0, dtMax=0.0, Jd=0)
analyze(1)

# printModel()
# for node in getNodeTags():
#   d=nodeDisp(node)
#   # f=nodeReaction(node)
#   print(f"el nodo {node} se desplaza: {d}")
#   # print(f"el nodo {node} tiene reaccion: {f}")

# for ele in getEleTags():
#     a=eleResponse(ele,"axialForce")
#     print(f"el elemento {ele} tiene fuerza axial: {a}")

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
  
# plot()


# printModel()

opsv.plot_model()
plt.title('plot_model after defining elements')

opsv.plot_loads_2d()
plt.title('plot_model with loads')




opsv.plot_defo()

# sfacN, sfacV, sfacM = 5.e-5, 5.e-5, 5.e-5

# opsv.section_force_diagram_2d('N', sfacN)
# plt.title('Axial force distribution')

# opsv.section_force_diagram_2d('T', sfacV)
# plt.title('Shear force distribution')

# opsv.section_force_diagram_2d('M', sfacM)
# plt.title('Bending moment distribution')

plt.show()
