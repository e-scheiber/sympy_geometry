from sympy import *
from geom2D import *
from sympy.vector import CoordSys3D

R = CoordSys3D('R')
xA,yA,xB,yB,xC,yC=symbols('xA,yA,xB,yB,xC,yC',real=True)
A=Point(xA,yA)
B=Point(xB,yB)
C=Point(xC,yC)
rA=A.x*R.i+A.y*R.j
rB=B.x*R.i+B.y*R.j
rC=C.x*R.i+C.y*R.j
H=Hcenter(A,B,C)
O=Ocenter(A,B,C)
rH=H.x*R.i+H.y*R.j
rO=O.x*R.i+O.y*R.j
r=rA+rB+rC-2*rO-rH
print('Rezultat : '+str(simplify(r)))