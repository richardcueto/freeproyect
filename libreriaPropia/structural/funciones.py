# from openpyxl import load_workbook
# from openpyxl.styles import PatternFill
# from sympy import symbols,integrate,solve
# import math
# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# wb=load_workbook('function.xlsx')
# ws=wb.active
# relleno_naranja=PatternFill(start_color='FFA500',end_color='FFA500',fill_type='solid')
# relleno_amarillo=PatternFill(start_color='FFFF00',end_color='FFFF00',fill_type='solid')

# def tabla1_E030_10_2(zona):
#   cel_1,cel_1.fill,cel_1,cel_1.value=ws[zona],relleno_amarillo,ws[zona].offset(row=0,column=-1),'zona'
#   resultado='=IF('+zona+'="Z1",0.45,IF('+zona+'="Z2",0.35,IF('+zona+'="Z3",0.25,0.1)))'
#   res_1,res_1.fill,res_1.value,res_1,res_1.value=ws[zona].offset(row=1,column=0),relleno_naranja,resultado,ws[zona].offset(row=1,column=-1),'Zona(g)'

# def momentoPositivo(wu,ln,tipoExtremo='monolitico'):
#   cel_1,cel_1.fill,cel_1,cel_1.value=ws[wu],relleno_amarillo,ws[wu].offset(row=0,column=-1),'wu'
#   cel_2,cel_2.fill,cel_2,cel_2.value=ws[ln],relleno_amarillo,ws[ln].offset(row=0,column=-1),'ln'
#   #momentos externo
#   if not tipoExtremo=='monolitico':
#     #el extremo discontinuo no esta restringido
#     tramoExtremo='=('+wu+'*POWER('+ln+',2))/11'
#   else:
#     #el extremo discontinuo es monolitico con el apoyo
#     tramoExtremo='=('+wu+'*POWER('+ln+',2))/14'
#   #momentos internos
#   tramoInterno = '=('+wu+'*POWER('+ln+',2))/16'
#   res_1,res_1.fill,res_1.value,res_1,res_1.value=ws[ln].offset(row=1,column=0),relleno_naranja,tramoExtremo,ws[ln].offset(row=1,column=-1),'Momento externo'
#   res_1,res_1.fill,res_1.value,res_1,res_1.value=ws[ln].offset(row=2,column=0),relleno_naranja,tramoInterno,ws[ln].offset(row=2,column=-1),'Momento interno'
#   return

# def cuadratica(a,b,c):
#   """
#   Function to solve: ax2+bx+c=0
#   """
#   x=[0,0]
#   x[0]=(-b+(b**2-4*a*c)**0.5)/(2*a)
#   x[1]=(-b-(b**2-4*a*c)**0.5)/(2*a)
#   return x

# def cableUniformLoad(w0,x,y):
#   """
#   Cable subjected to a uniform distribute load
  
#   Args:
#   w0:distribuida
#   x:longitud
#   y:altura

#   Returns:
#   FH and T
#   """
#   FH=w0*x**2/(2*y)
#   teta=math.atan(w0/FH*x)
#   T=FH/math.cos(teta)
#   return teta*180/math.pi,FH,T

# def curvatura(M,E,I):
#   return '1/p es:'+ M/E*I

# def momento(w,l,x):
#   Ve=w*l/2
#   Mi=Ve*x-w*x**2/2
#   return Ve,Mi

# def SlopeAndDeflection(x,f,E,I,dv_dxi=None,dv_dxf=None,dv2_dx2i=None,dv2_dx2f=None,x_pos=None):
#   """
#   defelxion y pendiente
  
#   Args:
#   x:variable
#   f:funcion
#   x_pos:posicion(x[0-L])
#   dv_dxi:pendiente 0 inicial
#   dv_dxf:pendiente 0 final
#   dv2_dx2i:deflexion 0 inicial
#   dv2_dx2f:deflexion 0 final

#   Returns:
#   Slope and Deflection
#   """
#   C1,C2=symbols('C1 C2')
#   integral1=integrate(f,x)
#   integral1=integral1+ C1
#   print("dv/dx                  :",integral1)
  
#   integral2=integrate(integral1,x)
#   integral2= integral2+ C2
#   print("dv2/dx2                :",integral2)
  
#   if dv_dxi==0 and dv2_dx2i==0:
#     constC1= 0
#     print("C1                     :",constC1)

#     ecuacion1 = integral2.subs(x,0).subs(C1,constC1)-0
#     constC2= solve(ecuacion1, C2)
#     print("C2                     :",constC2)

#     if x_pos==None:
#       integral1=integral1.subs(C1,constC1)
#       print("slope(dv/dx)           :",integral1/(E*I),'radianes')

#       integral2=integral2.subs(C1,constC1).subs(C2,constC2[0])
#       print("deflection(dv2/dx2)    :",integral2/(E*I),'m')
#     else:
#       integral1=integral1.subs(x,x_pos).subs(C1,constC1)
#       print("slope(dv/dx)           :",integral1/(E*I),'radianes')

#       integral2=integral2.subs(x,x_pos).subs(C1,constC1).subs(C2,constC2[0])
#       print("deflection(dv2/dx2)    :",integral2/(E*I),'m')
#   else:
#     ecuacion1 = integral2.subs(x,dv2_dx2i)-0
#     constC2= solve(ecuacion1, C2)

#     ecuacion2 = integral2.subs(x,dv2_dx2f).subs(C2,constC2[0])-0
#     constC1= solve(ecuacion2, C1)
#     print("C1                     :",constC1)
#     print("C2                     :",constC2)

#     if x_pos==None:
#       integral1=integral1.subs(C1,constC1[0])
#       print("slope(dv/dx)           :",integral1/(E*I),'radianes')

#       integral2=integral2.subs(C1,constC1[0]).subs(C2,constC2[0])
#       print("deflection(dv2/dx2)    :",integral2/(E*I),'m')
#     else:
#       integral1=integral1.subs(x,x_pos).subs(C1,constC1[0])
#       print("slope(dv/dx)           :",integral1/(E*I),'radianes')

#       integral2=integral2.subs(x,x_pos).subs(C1,constC1[0]).subs(C2,constC2[0])
#       print("deflection(dv2/dx2)    :",integral2/(E*I),'m')

# def VirtualAxialEnergy(E,A):
#   tabla = pd.DataFrame(columns=['Member','n(KN)','N(KN)','L(m)'])
  
#   cantTruss=int(input('Ingrese cantidad Truss: '))
#   i = 0
#   while i<cantTruss:
#     fila = []
#     for columna in tabla.columns:
#       valor = input(f"Ingrese el valor para [{columna}]: ")
#       fila.append(valor)
#     tabla.loc[len(tabla)] = fila
#     i=i+1

#   tabla['nNL(KN2.m)']=pd.to_numeric(tabla['n(KN)'])*pd.to_numeric(tabla['N(KN)'])*pd.to_numeric(tabla['L(m)'])
#   resultado=tabla['nNL(KN2.m)'].sum()/(E*A)
#   print(tabla)
#   print(tabla['nNL(KN2.m)'].sum())
#   print('Energia',resultado,'KN.m o KN.rad')
#   print('Energia',resultado*1000,'KN.mm o KN.rad*10-3')
#   print('----------------------------------------------------')
#   return resultado

# def VirtualBendingEnergy(m,M,E,I,b,a=0):
#   """
#   virtual energia
  
#   Args:
#   x:simbolo
#   m:momento unitario
#   M:momento real
#   E:(N/m2)
#   I:(m4)
#   [a b]:limites de integracion

#   Returns:
#   Energia en KN.m
#   """
#   x=symbols('x')
#   f=m*M/(E*I)
#   resultado=integrate(f,(x,a,b))
#   print('Energia',resultado,'KN.m o KN.rad')
#   print('Energia',resultado*1000,'KN.mm o KN.rad*10-3')
#   print('----------------------------------------------------')
#   return resultado

# def VirtualShearEnergy(v,V,G,A,b,a=0,K=1.2):
#   """
#   virtual energia
  
#   Args:
#   v:virtual shear
#   V:real shear
#   G:(N/m2)
#   A:(m2)
#   K:1.2(rectangular)
#   [a b]:limites de integracion

#   Returns:
#   Energia en KN.m 
#   """
#   x=symbols('x')
#   f=K*v*V/(G*A)
#   resultado=integrate(f,(x,a,b))
#   print('desplazamiento',resultado,'KN.m o KN.rad')
#   print('desplazamiento',resultado*1000,'KN.mm o KN.rad*10-3')
#   print('----------------------------------------------------')
#   return resultado

# def slopeDeflectionEquation(teta_A,teta_B,desp_A,desp_B,FEM_AB,FEM_BA,L,E,I):
#   MAB=[2*E*(I/L)*(2*teta_A+teta_B-3*(desp_B/L))+FEM_AB,2*E*(I/L)*(2*teta_B+teta_A-3*(desp_A/L))+FEM_BA]
#   print(MAB)
#   return MAB

# def FEM_W_Distribuid(type,w,l):
#   """
#   virtual energia
  
#   Args:
#   type:triangular,recatgular
#   w:carga
#   l:longitud

#   Returns:
#   carga ditribuida
#   """
#   if type=='trianguleL':
#     FEM=(w*l**2/20,-w*l**2/30)
#   elif type=='trianguleC':
#     FEM=(-5*w*l**2/96,5*w*l**2/96)
#   elif type=='trianguleR':
#     FEM=(-w*l**2/30,w*l**2/20)
#   elif type=='rectangular':
#     FEM=(-w*l**2/12,w*l**2/12)
#   print(FEM)
#   return FEM

Mnode={}
Mfix={}
Mload={}
Melemmt={}

def node(ntag,*node):
  Mnode[ntag]=node
  return Mnode

def fix(ntag,*arg):
  if model[1][1]==3:
    Mfix[ntag]=arg[0],arg[1],arg[2]
  else:
    Mfix[ntag]=arg[0],arg[1]
  return Mfix

model={}
def Model(dm,dof):
  model[1]=dm,dof
  return dof

def gdl_totales():
  result=len(Mnode)*model[1][1]
  return result

def gdl_libres():
  gdl_f=0
  if model[1][1]==3:
    for value in Mfix.values():
        if value[0]==0:
            gdl_f+=1
        if value[1]==0:
            gdl_f+=1
        if value[2]==0:
            gdl_f+=1
  else:
    for value in Mfix.values():
        if value[0]==0:
            gdl_f+=1
        if value[1]==0:
            gdl_f+=1
  return gdl_f

def gdl_barra():
  gdl_t=gdl_totales()+1
  gdl_xi=0
  gdl_xf=gdl_t
  Mbarra=[]

  if model[1][1]==3:
      for i in range(len(Mfix)):
        if Mfix[i+1][0]==0:
          gdl_xi+=1
          Mbarra.append(gdl_xi)
          # print(gdl_xi)
        elif Mfix[i+1][0]==1:
          gdl_xf-=1
          Mbarra.append(gdl_xf)
          # print(gdl_xf)

        if Mfix[i+1][1]==0:
          gdl_xi+=1
          gdl_yi=gdl_xi
          Mbarra.append(gdl_yi)
          # print(gdl_yi)
        elif Mfix[i+1][1]==1:
          gdl_xf-=1
          gdl_yf=gdl_xf
          Mbarra.append(gdl_yf)
        
        if Mfix[i+1][2]==0:
          gdl_xi+=1
          gdl_yi=gdl_xi
          Mbarra.append(gdl_yi)
          # print(gdl_yi)
        elif Mfix[i+1][2]==1:
          gdl_xf-=1
          gdl_yf=gdl_xf
          Mbarra.append(gdl_yf)
          # print(gdl_yf)
      return Mbarra
  else:
      for i in range(len(Mfix)):
        if Mfix[i+1][0]==0:
          gdl_xi+=1
          Mbarra.append(gdl_xi)
          # print(gdl_xi)
        elif Mfix[i+1][0]==1:
          gdl_xf-=1
          Mbarra.append(gdl_xf)
          # print(gdl_xf)

        if Mfix[i+1][1]==0:
          gdl_xi+=1
          gdl_yi=gdl_xi
          Mbarra.append(gdl_yi)
          # print(gdl_yi)
        elif Mfix[i+1][1]==1:
          gdl_xf-=1
          gdl_yf=gdl_xf
          Mbarra.append(gdl_yf)
          # print(gdl_yf)
      return Mbarra

  
def orden_gdl_Locales():
  gdl_t=gdl_totales()
  gdl_f=gdl_libres()
  print(gdl_t-gdl_f)
  gdlbarra=gdl_barra()
  print(gdlbarra)
  # Q=np.zeros((gdl_f,1))
  # gdl_local=gdlbarra[2*(nTag-1):2*nTag]
  return 

def load(nTag,*arg):
  gdl_f=gdl_libres()
  gdlbarra=gdl_barra()
  Q=np.zeros((gdl_f,1))
  gdl_local=gdlbarra[2*(nTag-1):2*nTag]
  Q[gdl_local[0]-1]=arg[0]
  Q[gdl_local[1]-1]=arg[1]
  Mload[nTag]=Q
  return Mload

def element(type,eleTag,*args,E,A=0,I=0):
  gdlbarra=gdl_barra()
  print(gdlbarra)
  if model[1][1]==3:
    gdlbarra=gdlbarra[3*(args[0]-1):3*args[0]]+gdlbarra[3*(args[1]-1):3*args[1]]
  else:
    gdlbarra=gdlbarra[2*(args[0]-1):2*args[0]]+gdlbarra[2*(args[1]-1):2*args[1]]
  xi,yi=Mnode[args[0]]
  xf,yf=Mnode[args[1]]
  L=((xf-xi)**2+(yf-yi)**2)**0.5

  if type=='Truss':
    lam_x,lam_y=(xf-xi)/L,(yf-yi)*(E/A)/L
    k_b_local=np.array([[1,-1],
                        [-1,1]])*(E/A)/L
    k_tra=np.array([-lam_x,-lam_y,lam_x,lam_y])*E*A/L
    k_b_global=np.array([[lam_x**2,lam_x*lam_y,-lam_x**2,-lam_x*lam_y],
                    [lam_x*lam_y,lam_y**2,-lam_x*lam_y,-lam_y**2],
                    [-lam_x**2,-lam_x*lam_y,lam_x**2,lam_x*lam_y],
                    [-lam_x*lam_y,-lam_y**2,lam_x*lam_y,lam_y**2]])*(E/A)/L
    Melemmt[eleTag]=k_b_local,k_tra,k_b_global,gdlbarra,args

  if type=='Beam':
    k_tra=0
    k_b_local=np.array([[1,-1],
                        [-1,1]])*(E/I)/L
    # k_tra=np.array([-lam_x,-lam_y,lam_x,lam_y])*E*I/L
    k_b_global=np.array([[12/L**3,6/L**2,-12/L**3,6/L**2],
                         [6/L**2,4/L,-6/L**2,2/L],
                         [-12/L**3,-6/L**2,12/L**3,-6/L**2],
                         [6/L**2,2/L,-6/L**2,4/L]])*(E*I)
    Melemmt[eleTag]=k_b_local,k_tra,k_b_global,gdlbarra,args,type
  
  if type=='elasticBeamColumn':
    lam_x,lam_y=(xf-xi)/L,(yf-yi)*(E/A)/L
    k_tra=0
    k_b_local=np.array([[1,-1],
                        [-1,1]])*(E/I)/L
    a11=(A*E*lam_x**2/L+12*E*I*lam_y**2/L**3)
    a12=(A*E/L-12*E*I/L**3)*lam_x*lam_y
    a21=a12
    a13=-6*E*I*lam_y/L**2
    a31=a13
    a14=-(A*E*lam_x**2/L+12*E*I*lam_y**2/L**3)
    a41=a14
    a15=-(A*E/L-12*E*I/L**3)*lam_x*lam_y
    a51=a15
    a16=-6*E*I*lam_y/L**2
    a61=a16
    a22=(A*E*lam_y**2/L+12*E*I*lam_x**2/L**3)
    a23=6*E*I*lam_x/L**2
    a32=a23
    a24=-(A*E/L-12*E*I/L**3)*lam_x*lam_y
    a42=a24
    a25=-(A*E*lam_y**2/L+12*E*I*lam_x**2/L**3)
    a52=a25
    a26=6*E*I*lam_x/L**2
    a62=a26
    a33=4*E*I/L
    a34=6*E*I/L**2*lam_y
    a43=a34
    a35=-6*E*I/L**2*lam_x
    a53=a35
    a36=2*E*I/L
    a63=a36
    a44=(A*E*lam_x**2/L+12*E*I*lam_y**2/L**3)
    a45=(A*E/L-12*E*I/L**3)*lam_x*lam_y
    a54=a45
    a46=6*E*I/L**2*lam_y
    a64=a46
    a55=(A*E*lam_y**2/L+12*E*I*lam_x**2/L**3)
    a56=-6*E*I/L**2*lam_x
    a65=a56
    a66=4*E*I/L
    k_b_global=np.array([[a11,a12,a13,a14,a15,a16],
                         [a21,a22,a23,a24,a25,a26],
                         [a31,a32,a33,a34,a35,a36],
                         [a41,a42,a43,a44,a45,a46],
                         [a51,a52,a53,a54,a55,a56],
                         [a61,a62,a63,a64,a65,a66]])
    Melemmt[eleTag]=k_b_local,k_tra,k_b_global,gdlbarra,args,type

  return Melemmt

def analyze():
  gdl_t=gdl_totales()
  gdl_f=gdl_libres()
  K_global=np.zeros((gdl_t,gdl_t))
  for i in range(1,len(Melemmt)+1):
    rigidez_global_barra(Melemmt[i][2],Melemmt[i][3],K_global)

  #globales
  Q=np.zeros((gdl_f,1))
  print('**********Vector de cargas*************************')
  for carga in Mload.values():
    Q+=carga

  print(Q)
  print('**********Rigidez global de desplazamientos********')
  K11=K_global[:gdl_f,:gdl_f]
  print(K11)

  print('**********Desplazamiento global*******************')
  D=np.linalg.inv(K11)@Q
  print(D)

  print('**********Rigidez global de fuerzas****************')
  K21=K_global[gdl_f:gdl_t,:gdl_f]
  print(K21)

  print('**********Reaccion global*************************')
  QU=K21@D
  print(QU)
  return D,QU

def rigidez_global_barra(ke,gdlbarra,K_global):
  for igdl in range(len(gdlbarra)):
    ifila=gdlbarra[igdl]
    for jgdl in range(len(gdlbarra)):
      jcolumna=gdlbarra[jgdl]
      K_global[ifila-1,jcolumna-1]=K_global[ifila-1,jcolumna-1]+ke[igdl,jgdl]
  return K_global

def plot(scale=10,D=0.2):
  for node in Mnode:
    # plt.scatter(Mnode[node][0],Mnode[node][1],color='red',label=node)
    # plt.text(Mnode[node][0],Mnode[node][1],node,ha='center',va='bottom')
    plt.scatter(Mnode[node][0],Mnode[node][1],color='red',label=node)
    plt.text(Mnode[node][0],Mnode[node][1],node,ha='left',va='bottom',fontsize=10)

  for ele in Melemmt:
    x1,y1=Mnode[Melemmt[ele][4][0]]
    x2,y2=Mnode[Melemmt[ele][4][1]]
    plt.plot([x1,x2],[y1,y2],color='green',linestyle='-')

    plt.quiver(x1, y1,0.4,0, angles='xy', scale_units='xy', scale=1)
    plt.quiver(x1, y1,0,0.4, angles='xy', scale_units='xy', scale=1)
    plt.text(x1+0.2,y1-0.2,Melemmt[ele][3][0],ha='left',va='bottom',fontsize=9)
    plt.text(x1-0.2,y1+0.2,Melemmt[ele][3][1],ha='left',va='bottom',fontsize=9)

    deltx=x2-x1
    delty=y2-y1
    x=np.linspace(x1,x2,scale)
    y=np.linspace(y1,y2,scale)

    if Melemmt[1][3]=='Truss':
      if deltx==0:
        plt.text(x1,y1+delty/3,ele,ha='left',va='bottom')
        plt.plot(x+D,y,color='blue',linestyle='-')
        # plt.text(x1+D,y1+2*delty/3,F,ha='right',va='bottom',fontsize=9) 
      else:
        m=delty/deltx
        plt.text(x1+deltx/3,y1+m*1/3*deltx,ele,ha='left',va='bottom')
        plt.plot(x,y1+m*(x-x1)+D,color='red',linestyle='-')
        plt.fill_between(x,y1+m*(x-x1)+D,y,where=(y1+m*(x-x1)>=y),interpolate=True,color='lightblue',alpha=0.5)
        # plt.text(x1+2/3*deltx,y1+m*2/3*deltx+D,F,ha='left',va='bottom',fontsize=9)

  plt.quiver(x2, y2,0.4,0, angles='xy', scale_units='xy', scale=1)
  plt.quiver(x2, y2,0,0.4, angles='xy', scale_units='xy', scale=1)
  plt.text(x2+0.2,y2-0.2,Melemmt[ele][3][2],ha='left',va='bottom',fontsize=9)
  plt.text(x2-0.2,y2+0.2,Melemmt[ele][3][3],ha='left',va='bottom',fontsize=9)
  
  # plt.title('estructura')
  # plt.xlabel('eje x')
  # plt.ylabel('eje y')
  # plt.grid()
  # plt.legend()
  plt.show()

def graficas(q1,q2,x1,x2,x,u1,u2,u3,u4):
  A=(q2-q1)/(x2-x1)
  B=q1-(q2-q1)/(x2-x1)*x1
  EIdu4_dx4=-A*x-B
  EIdu3_dx3=-A*x**2/2-B*x+C1
  EIdu2_dx2=-A*x**3/6-B*x**2/2+C1*x+C2
  EIdu1_dx1=-A*x**4/24-B*x**3/6+C1*x**2/2+C2*x+C3
  EIu=-A*x**5/120-B*x**4/24+C1*x**3/6+C2*x**2/2+C3*x+C4
  #EI,A,B=C*X
  [c1,c2,c3,c4]
  X=[[x1**3/6,x1**2/2,x1,1],
      [x1**3/6,x1**2/2,x1,1],
      [x1**3/6,x1**2/2,x1,1],
      [x1**3/6,x1**2/2,x1,1],]
  [[E*I*u1+A*x1**5/120+B*x1**4/24],
    [E*I*u2+A*x1**4/24+B*x1**3/6],
    [E*I*u3+A*x2**5/120+B*x2**4/24],
    [E*I*u4+A*x2**4/24+B*x2**4/6]]
  
def DMV(X,A,B,C1):
  V=-A*X**2/2-B*X+C1
  return V

def DMF(X,A,B,C1,C2):
  M=-A*X**3/6-B*X**2/2+C1*X+C2
  return M

def Dpend(X,A,B,C1,C2,C3,C4):
  pend=-A*X**4/24-B*X**3/6+C1*X**2/2+C2*X+C3
  return pend

def DMu(X,A,B,C1,C2,C3,C4):
  u=-A*X**5/120-B*X**4/24+C1*X**3/6+C2*X**2/2+C3*X+C4
  return u

# import matplotlib.pyplot as plt
# X=np.linspace(0,10,20)
# V=DMV(X,1,1,1)
# M=DMF(X,1,1,1,2)

# plt.plot(X,V,label='V')
# plt.plot(X,M,label='M')

# plt.show()




# #aplicando fomulas
# tabla1_E030_10_2('B1')
# momentoPositivo('B8','B9')

# wb.save("function.xlsx")
# # frozenset({'DGET', 'MIDB', 'MIN', 'DAYS360', 'EXP', 'VARP', 'ODD', 'COUNTIF', 'GESTEP', 'UPPER', 'BIN2OCT', 'RAND', 'PRICE', 'NORMSINV', 'JIS', 'NOMINAL', 'QUOTIENT', 'FACTDOUBLE', 'CHOOSE', 'IMLOG10', 'DATEVALUE', 'WEEKNUM', 'BINOMDIST', 'NEGBINOMDIST', 'YEARFRAC', 'SUMIFS', 'TIMEVALUE', 'TYPE', 'INDEX', 'DPRODUCT', 'NPER', 'MINA', 'TRANSPOSE', 'CUBEMEMBER', 'SUBSTITUTE', 'MAX', 'ROUNDUP', 'HYPERLINK', 'DISC', 'HEX2BIN', 'ODDFYIELD', 'INDIRECT', 'TODAY', 'PRICEMAT', 'SEARCHB', 'IMSUB', 'HEX2OCT', 'IMCOS', 'CELL', 'IMARGUMENT', 'COVAR', 'MID', 'DEVSQ', 'MIRR', 'YEAR', 'LINEST', 'FTEST', 'ABS', 'IMLOG2', 'MULTINOMIAL', 'CORREL', 'ACOS', 'ROWS', 'LOWER', 'LARGE', 'CUBESETCOUNT', 'SUMX2MY2', 'RANK', 'ROW', 'SERIESSUM', 'ZTEST', 'SUMXMY2', 'CHITEST', 'BESSELK', 'POWER', 'COUNT', 'NORMDIST', 'IMSIN', 'DMAX', 'DATE', 'CONVERT', 'LOGINV', 'STDEVP', 'ISBLANK', 'ASINH', 'FIND', 'ODDFPRICE', 'YIELDMAT', 'IMPOWER', 'BIN2HEX', 'EDATE', 'SUM', 'PERMUT', 'GAMMADIST', 'SUBTOTAL', 'ASC', 'HARMEAN', 'SUMSQ', 'FVSCHEDULE', 'PEARSON', 'FINDB', 'ISREF', 'ROMAN', 'RANDBETWEEN', 'EXACT', 'SLOPE', 'MAXA', 'MDURATION', 'FLOOR', 'AVERAGE', 'SQRTPI', 'FALSE', 'SEARCH', 'ISNUMBER', 'COUPNUM', 'ECMA.CEILING', 'RATE', 'RTD', 'CHIDIST', 'STDEVPA STEYX', 'DB', 'INTRATE', 'HYPGEOMDIST', 'FDIST', 'PROB', 'NETWORKDAYS.INTL', 'ISODD', 'N', 'DATEDIF', 'RSQ', 'MINUTE', 'MROUND', 'IF', 'GETPIVOTDATA', 'CONCATENATE', 'ISERR', 'SIN', 'BETADIST', 'CUMPRINC', 'ISERROR', 'SMALL', 'COUPDAYS', 'DOLLARDE', 'MDETERM', 'DOLLAR', 'ISPMT', 'REPT', 'PERCENTRANK', 'BAHTTEXT', 'WEIBULL', 'IRR', 'AMORLINC', 'COLUMN', 'PRICEDISC', 'FINV', 'TRUNC', 'EXPONDIST', 'DAVERAGE', 'LOGNORMDIST', 'AND', 'DCOUNT', 'ERROR.TYPE', 'FISHER', 'FREQUENCY', 'COSH', 'AVERAGEA', 'PPMT', 'POISSON', 'ISNA', 'SUMIF', 'TBILLYIELD', 'ROUND', 'ERFC', 'DURATION', 'DEC2HEX', 'CRITBINOM', 'ERF', 'SIGN', 'CONFIDENCE', 'DDB', 'ISTEXT', 'CUBEKPIMEMBER', 'TBILLEQ', 'ISLOGICAL', 'COLUMNS', 'FIXED', 'CUBEVALUE', 'FV', 'YIELDDISC', 'COUPDAYBS', 'ODDLYIELD', 'MOD', 'DVARP', 'DCOUNTA', 'FISHERINV', 'PI', 'CHIINV', 'LOG10', 'PHONETIC', 'NOW', 'ISNONTEXT', 'EFFECT', 'BESSELJ', 'REPLACE', 'DEC2BIN', 'TRIMMEAN', 'RECEIVED', 'SYD', 'VAR', 'IMAGINARY', 'MATCH', 'TBILLPRICE', 'IMREAL', 'PV', 'CHAR', 'ATAN2', 'CODE', 'DEC2OCT', 'FACT', 'HOUR', 'TAN', 'GEOMEAN', 'TTEST', 'ACCRINT', 'AVERAGEIF', 'COUPPCD', 'COUNTIFS', 'KURT', 'FORECAST', 'LEN', 'HEX2DEC', 'TANH', 'MODE', 'BESSELY', 'LOGEST', 'VALUE', 'STANDARDIZE', 'EVEN', 'DAY', 'GAMMALN', 'AVEDEV', 'SINH', 'COMPLEX', 'IMSQRT', 'AMORDEGRC', 'LCM', 'AVERAGEIFS', 'TIME', 'GROWTH', 'RIGHT', 'BETAINV', 'OCT2DEC', 'BIN2DEC', 'OFFSET', 'OR', 'TRUE ADDRESS', 'RADIANS', 'QUARTILE', 'IMLN', 'PRODUCT', 'YIELD', 'MEDIAN', 'ROUNDDOWN', 'ACOSH', 'VDB', 'DSTDEV', 'COUNTBLANK', 'SQRT', 'CUBESET', 'RIGHTB', 'IMABS', 'SECOND', 'XIRR', 'PMT', 'VLOOKUP', 'VARPA', 'TINV', 'NORMSDIST', 'ASIN', 'GAMMAINV', 'DOLLARFR', 'LENB', 'DELTA', 'IFERROR', 'IPMT', 'IMSUM', 'AREAS', 'SUMPRODUCT', 'IMPRODUCT', 'COUNTA', 'DSUM', 'IMEXP', 'T', 'OCT2BIN', 'TREND', 'NA', 'VARA', 'PERCENTILE', 'OCT2HEX', 'COUPNCD', 'NOT', 'IMDIV', 'MINVERSE', 'DVAR', 'NORMINV', 'WORKDAY.INTL', 'CUBERANKEDMEMBER', 'LOG', 'NETWORKDAYS', 'DEGREES', 'LN', 'ISO.CEILING', 'HLOOKUP', 'SLN', 'NPV', 'INFO', 'REPLACEB', 'LOOKUP', 'XNPV', 'GCD', 'CLEAN', 'ISEVEN', 'ODDLPRICE', 'COS', 'TEXT', 'COMBIN', 'LEFT', 'STDEV STDEVA', 'CUBEMEMBERPROPERTY', 'SUMX2PY2', 'TRIM', 'TDIST', 'PROPER', 'ATAN', 'CUMIPMT', 'ACCRINTM', 'CEILING', 'LEFTB', 'BESSELI', 'EOMONTH', 'MONTH', 'COUPDAYSNC', 'INTERCEPT', 'DSTDEVP', 'SKEW', 'INT', 'DMIN', 'WEEKDAY', 'IMCONJUGATE', 'WORKDAY ', 'ATANH'})

