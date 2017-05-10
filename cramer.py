# <--Tutorial-->
printf('Sendo o modelo:')
printf('----------------------------')
printf(' (a1)x + (b1)y + (c1)z = r1 ')
printf(' (a2)x + (b2)y + (c2)z = r2 ')
printf(' (a3)x + (b3)y + (c3)z = r3 ')
printf('----------------------------')
# <------------>

# <--Execução do cálculo-->
d1= (a1*b2*c3)+(b1*c2*a3)+(c1*a2*b3)
d2= (a3*b2*c1)+(b3*c2*a1)+(c3*a2*b1)
d3= d1-(d2)
dx1= (r1*b2*c3)+(b1*c2*r3)+(c1*r2*b3)
dx2= (r3*b2*c1)+(b3*c2*r1)+(c3*r2*b1)
dx3:= dx1-(dx2)
try
  dx := dx3/ d3; // Sendo que o divisor pode ser zero
except
  dx := 0; // Ou seja, se o total for divido por zero, então atribui zero para a variável valor;

    
dy1= (a1*r2*c3)+(r1*c2*a3)+(c1*a2*r3)
dy2= (a3*r2*c1)+(r3*c2*a1)+(c3*a2*r1)
dy3= dy1-(dy2);   
try
  dy := dy3/ d3;
except
  dy := 0;  
    
    
dz1= (a1*b2*r3)+(b1*r2*a3)+(r1*a2*b3)
dz2= (a3*b2*r1)+(b3*r2*a1)+(r3*a2*b1)
dz3= dz1-(dz2)
try
  dz := dz3/d3
except
  dz := 0;
# <----------------------->

# <--Entrada de dados-->
a1= input('Digite o valor correspondente a a1') 
b1= input('Digite o valor correspondente a b1')
c1= input('Digite o valor correspondente a c1')
r1= input('Digite o valor correspondente a r1')

a2= input('Digite o valor correspondente a a1')
b2= input('Digite o valor correspondente a b1')
c2= input('Digite o valor correspondente a c1')
r2= input('Digite o valor correspondente a r2')

a3= input('Digite o valor correspondente a a1')
b3= input('Digite o valor correspondente a b1')
c3= input('Digite o valor correspondente a c1')
r3= input('Digite o valor correspondente a r3')
# <-------------------->


 
