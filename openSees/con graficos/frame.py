from openseespy.opensees import *
import numpy as np
import matplotlib.pyplot as plt
import opsvis as opsv

# ------------------------------
# Empezamos a generar el modelo
# -----------------------------
wipe()

model('basic','-ndm',2,'-ndf',3)

E,A,I,Iv=20e9,6e-3,180e-6,1

geomTransf('Linear', 1)

node(1,0,0)
node(2,6, 0)
node(3,6, -6)

fix(1,0,1,0)
fix(2,0,0,0)
fix(3,1,1,1)

element('elasticBeamColumn',1,1,2,A,E,I,1)
element('elasticBeamColumn',2,2,3,A,E,I,1)

timeSeries('Linear', 1)
pattern('Plain', 1, 1)
load(2,20,0,0)

# ------------------------------
# Start of analysis generation
# ------------------------------
constraints('Plain')
numberer('Plain')
system('BandGen')
algorithm('Linear')
integrator('LoadControl', 1.0)
analysis('Static')
analyze(1)

opsv.plot_model()
plt.title('plot_model after defining elements')

opsv.plot_loads_2d()
plt.title('plot_model with loads')

opsv.plot_defo()

sfacn, sfacv, sfacm = 5.e-5, 5.e-5, 5.e-5

# opsv.section_force_diagram_2d('n', sfacn)
# plt.title('axial force distribution')

opsv.section_force_diagram_2d('T', sfacv)
plt.title('shear force distribution')

opsv.section_force_diagram_2d('M', sfacm)
plt.title('bending moment distribution')

plt.show()