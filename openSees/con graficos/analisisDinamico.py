from openseespy.opensees import *
import matplotlib.pyplot as plt
import opsvis as opsv
from math import pi

#---------------------------------------------------------------------
# Análisis dinámico lineal de una columna.
# Unidades del modelo [N,m,s]
#---------------------------------------------------------------------

model('basic','-ndm',2,'-ndf',3)

h,m,A,I,E,g=12,5000,1,0.0833,20e9,9.81

node(1,0,0)
node(2,0,h,'-mass',m,0,0)

fix(1,1,1,1)

geomTransf('Linear', 1)

element('elasticBeamColumn',1,1,2,A,E,I,1)

print(nodeDisp(2))
print(nodeReaction(1))
print(eleForce(1))

timeSeries('Linear', 1)

pattern('Plain', 1, 1)

load(2,0,-m*g,0)

# ------------------------------
# Start of analysis generation
# ------------------------------

#definen valores para analisis estatico
constraints('Plain')
numberer('RCM')
system('BandGen')
algorithm('Newton')
test('NormDispIncr',10e-6,10)
integrator('LoadControl', 1.0)
analysis('Static')
analyze(10)

#definen valores para analisis dinamico
loadConst('-time',0.0)

factor,dt,Npuntos=0.01,0.01,15000
acelFile='CUP52203.txt'
dirX=1
accelSeries=f'Series -dt {dt} -filePath {acelFile} -factor {factor}'
pattern('UniformExcitation', 2, dirX, '-accel', accelSeries)

freq=eigen('-fullGenLapack',1)**0.5/(2*pi)

system('UmfPack')
numberer ('RCM')
constraints ('Plain')
test('NormDispIncr' ,1.0e-8 ,10)
integrator('Newmark', 0.5 ,0.25)
algorithm('Newton')
analysis('Transient')
analyze(Npuntos,dt)

opsv.plot_model()
plt.title('plot_model after defining elements')

opsv.plot_loads_2d()
plt.title('plot_model with loads')

opsv.plot_defo()

plt.show()