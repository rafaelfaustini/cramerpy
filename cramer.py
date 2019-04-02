from time import gmtime, strftime
import sys

class Equacao:
  a = []
  b = []
  c = []
  r = []
  d3 = 0
  data = ''

  def __init__(self,a1,a2,a3,b1,b2,b3,c1,c2,c3,r1,r2,r3):
    self.setA(1, a1)
    self.setA(2, a2)
    self.setA(3, a3)

    self.setB(1, b1)
    self.setB(2, b2)
    self.setB(3, b3)

    self.setC(1, c1)
    self.setC(2, c2)
    self.setC(3, c3)

    self.setR(1, r1)
    self.setR(2, r2)
    self.setR(3, r3)

    self.calculaD3()
    self.output(self.calculaX(), self.calculaY(), self.calculaZ())

  def getA(self,n):
    return self.a[n-1]
  def getB(self,n):
    return self.b[n-1]
  def getC(self,n):
    return self.c[n-1]
  def getR(self,n):
    return self.r[n-1]
  def setA(self,n, value):
    self.a.insert(n-1,value)
  def setB(self,n, value):
    self.b.insert(n-1,value)
  def setC(self,n, value):
    self.c.insert(n-1,value)  
  def setR(self,n, value):
    self.r.insert(n-1,value)

  def setD3(self,value):
    self.d3 = value
  def getD3():
    return self.d3

  def calculaD3(self):
    d1= (self.getA(1)*self.getB(2)*self.getC(3))+(self.getB(1)*self.getC(2)*self.getA(3))+(self.getC(1)*self.getA(2)*self.getB(3))
    d2= (self.getA(3)*self.getB(2)*self.getC(1))+(self.getB(3)*self.getC(2)*self.getA(1))+(self.getC(3)*self.getA(2)*self.getB(1))
    d3= d1-(d2)
    self.setD3(d3)
      
  def calculaX(self):
    dx1= (self.getR(1)*self.getB(2)*self.getC(3))+(self.getB(1)*self.getC(2)*self.getR(3))+(self.getC(1)*self.getR(2)*self.getB(3))
    dx2= (self.getR(3)*self.getB(2)*self.getC(1))+(self.getB(3)*self.getC(2)*self.getR(1))+(self.getC(3)*self.getR(2)*self.getB(1))
    dx3= dx1-(dx2)
    print(dx3)
    try:
      dx = dx3/self.getD3()
    except: 
      dx=0
    return dx;

  def calculaY(self):
    dy1= (self.getA(1)*self.getR(2)*self.getC(3))+(self.getR(1)*self.getC(2)*self.getA(3))+(self.getC(1)*self.getA(2)*self.getR(3))
    dy2= (self.getA(3)*self.getR(2)*self.getC(1))+(self.getR(3)*self.getC(2)*self.getA(1))+(self.getC(3)*self.getA(2)*self.getR(1))
    dy3= dy1-(dy2); 
    try:
      dy = dy3/ self.getD3()
    except: 
      dy=0
    return dy

  def calculaZ(self):
    dz1= (self.getA(1)*self.getB(2)*self.getR(3))+(self.getB(1)*self.getR(2)*self.getA(3))+(self.getR(1)*self.getA(2)*self.getB(3))
    dz2= (self.getA(3)*self.getB(2)*self.getR(1))+(self.getB(3)*self.getR(2)*self.getA(1))+(self.getR(3)*self.getA(2)*self.getB(1))
    dz3= dz1-(dz2)
    try:
      dz = dz3/ self.getD3()
    except: 
      dz=0
    self.data = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return dz

  def output(self,x,y,z):
    file = open("output.txt", "a")
    file.write("[{}] X={} Y={} Z={}\n".format(self.data, x, y, z))
    file.close()

file = open("input.txt", "r")
res = file.readlines()
for i in range(0, len(res)):
  c = res[i].split()
  print(len(c))
  if(len(c) == 12):
    equacao = Equacao(int(c[0]),int(c[1]),int(c[2]),int(c[3]),int(c[4]),int(c[5]),int(c[6]),int(c[7]),int(c[8]),int(c[9]),int(c[10]),int(c[11]))
    
