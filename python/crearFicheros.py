f=open("myfile.txt","w")#sobrescribe un archivo en python
L=["esto es \n","esto no es \n","esto si es \n"]
f.write("mi chico bonito coge flores\n")#escribe texto
f.writelines(L)#lee de una lista
f.close()#solo para cambiar modo de acceso a archivo

f=open("myfile.txt","r+")#leer y escribe un archivo en python

if not f:
  f=open("myfile.txt","r")#leer un archivo en python
  f=open("myfile.txt","x")#crea un archivo en python
  
f.seek(0)#mueve el puntero hacia byte indicado

print(f.read())