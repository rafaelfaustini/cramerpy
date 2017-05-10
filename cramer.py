from time import gmtime, strftime
data = strftime("%Y-%m-%d %H:%M:%S", gmtime())

#Inicialização de variáveis
a1=0
b1=0
c1=0
r1=0
a2=0
b2=0
c2=0
r2=0
a3=0
b3=0
c3=0
r3=0
d1=0
d2=0
d3=0
dx1=0
dx2=0
dx3=0
dx=0
dy1=0
dy2=0
dy3=0
dy=0
dz1=0
dz2=0
dz3=0
dz=0
def entrada():
  # <--Entrada de dados-->
  a1= input('Digite o valor correspondente a a1') 
  b1= input('Digite o valor correspondente a b1')
  c1= input('Digite o valor correspondente a c1')
  r1= input('Digite o valor correspondente a r1')

  a2= input('Digite o valor correspondente a a2')
  b2= input('Digite o valor correspondente a b2')
  c2= input('Digite o valor correspondente a c2')
  r2= input('Digite o valor correspondente a r2')

  a3= input('Digite o valor correspondente a a3')
  b3= input('Digite o valor correspondente a b3')
  c3= input('Digite o valor correspondente a c3')
  r3= input('Digite o valor correspondente a r3')
  # <-------------------->
  
def tutorial():
  # <--Tutorial-->
  print('Sendo o modelo:')
  print('----------------------------')
  print(' (a1)x + (b1)y + (c1)z = r1 ')
  print(' (a2)x + (b2)y + (c2)z = r2 ')
  print(' (a3)x + (b3)y + (c3)z = r3 ')
  print('----------------------------')
  # <------------>
  
def main():
  # <--Execução do cálculo-->
  d1= (a1*b2*c3)+(b1*c2*a3)+(c1*a2*b3)
  d2= (a3*b2*c1)+(b3*c2*a1)+(c3*a2*b1)
  d3= d1-(d2)
  dx1= (r1*b2*c3)+(b1*c2*r3)+(c1*r2*b3)
  dx2= (r3*b2*c1)+(b3*c2*r1)+(c3*r2*b1)
  dx3= dx1-(dx2)
  try:
    dx = dx3/ d3
  except: 
    dx=0


    
  dy1= (a1*r2*c3)+(r1*c2*a3)+(c1*a2*r3)
  dy2= (a3*r2*c1)+(r3*c2*a1)+(c3*a2*r1)
  dy3= dy1-(dy2); 
  try:
      dy = dy3/ d3
  except: 
      dy=0


    
    
  dz1= (a1*b2*r3)+(b1*r2*a3)+(r1*a2*b3)
  dz2= (a3*b2*r1)+(b3*r2*a1)+(r3*a2*b1)
  dz3= dz1-(dz2)
  try:
      dz = dz3/ d3
  except: 
      dz=0

  # <----------------------->

def output():
  # <--Saída de dados-->

  print('\nSnizer Cramer By Rafael Faustini')
  print(data)
  print('Equação Com 3 Variaveis')
  print('------------------------------------------------------------')
  print('A diagonal Principal D é %d'%d1)
  print('A diagonal Secundaria D é %d'%d2)
  print('O valor de D é %d'%d3)
  print('------------------------------------------------------------')
  print('A diagonal Principal Dx é %d'%dx1)
  print('A diagonal Secundaria Dx é %d'%dx2)
  print('O valor de Dx é %d'%dx3)
  print('O valor de X é %d'%dx)
  print('------------------------------------------------------------')
  print('A diagonal Principal  de Dy é %d'%dy1)
  print('A diagonal Secundaria de Dy é %d'%dy2)
  print('O valor de Dy é %d'%dy3)
  print('O valor de Y é %d'%dy)
  print('------------------------------------------------------------')
  print('A diagonal Principal  de Dz é %d'%dz1)
  print('A diagonal Secundaria de Dz é %d'%dz2)
  print('O valor de Dz é %d'%dz3)
  print('O valor de Z é %d'%dz)
  print('------------------------------------------------------------')
1

tutorial()
entrada()
main()
output()



