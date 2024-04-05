import openseespy.opensees as ops

#modelo
ops.model('basic','-ndm',2,'-ndf',2)

node1=[0,0]
node2=[1,0]
# 		  tag x y
ops.node(1,*node1)
ops.node(2,*node2)

# 		tag x y
fixed1=[1,1]
fixed2=[0,1]
ops.fix(1,*fixed1)
ops.fix(2,*fixed2)

secType = 'Elastic'
secTag = 1
E=1
A=1
Iz=0
secArgs = [E, A, Iz]
ops.section(secType, secTag, *secArgs)

eleNodes=[1,2]
ops.element('TrussSection', 1,*eleNodes, secTag)

#times series
tsTag=1
ops.timeSeries('Constant', tsTag,'-factor',1)

#load pattern
patternTag=1
ops.pattern('Plain', patternTag, tsTag,'-factor',1)

#carga
fx=0.
fy=-10e-3
ops.load(1,fx,fy)
ops.load(2,2,0.3)

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