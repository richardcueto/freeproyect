import openseespy.opensees as op
# Definir propiedades de materiales

E = 200000  # Módulo de elasticidad en MPa
A = 1000  # Área transversal en mm^2
I = 1000000  # Momento de inercia en mm^4

# Definir propiedades de la sección
op.uniaxialMaterial('Elastic', 1, E)
op.section('Ag', 1, A, I)

# Definir nodos
op.node(1, 0, 0)
op.node(2, 5000, 0)

# Fijar nodos
op.fix(1, 1, 1, 1)
op.fix(2, 0, 1, 0)

# Definir elementos
op.element('elasticBeamColumn', 1, 1, 2, 1, 'Ag')

# Aplicar carga puntual en el nodo 2
op.load(2, 1000, 0, 0)

# Resolver análisis estático
op.system('SparseGeneral')
op.constraints('Plain')
op.numberer('RCM')
op.test('NormDispIncr', 1e-6, 6)
op.algorithm('Newton')
op.integrator('LoadControl', 0.1)
op.analysis('Static')

op.analyze(10)