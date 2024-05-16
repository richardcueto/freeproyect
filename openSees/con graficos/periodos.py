from openseespy.opensees import *
import numpy as np
import matplotlib.pyplot as plt
import opsvis as opsv
from math import pi
# ------------------------------
# Empezamos a generar el modelo
# -----------------------------

# wipe()

model('basic','-ndm',2,'-ndf',3)

E,A,Ic,Iv=20e9,0.09,0.000675,10e12
m,numModos=4500,2

geomTransf('Linear', 1)

node(1,0,0)
node(2,8, 0)
node(3,0, 4)
node(4,8, 4)
node(5,0, 8)
node(6,8, 8)

fix(1,1,1,1)
fix(2,1,1,1)

mass(3,m,0,0)
mass(4,m,0,0)
mass(5,m/2,0,0)
mass(6,m/2,0,0)

element('elasticBeamColumn',1,1,3,A,E,2*Ic,1)
element('elasticBeamColumn',2,3,5,A,E,Ic,1)
element('elasticBeamColumn',3,2,4,A,E,2*Ic,1)
element('elasticBeamColumn',4,4,6,A,E,Ic,1)
element('elasticBeamColumn',5,3,4,A,E,Iv,1)
element('elasticBeamColumn',6,5,6,A,E,Iv,1)

eigenvalores=eigen(numModos)#w**2
print(eigenvalores)
T=[2*pi/(eigenval)**0.5 for eigenval in eigenvalores]
print(T)

opsv.plot_model()
plt.title('plot_model after defining elements')

opsv.plot_loads_2d()
plt.title('plot_model with loads')

# opsv.plot_defo()

plt.show()