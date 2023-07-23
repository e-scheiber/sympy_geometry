from sympy import *
from geom2D import *
xA,yA,xB,yB,xC,yC=symbols('xA,yA,xB,yB,xC,yC',real=True)

A=Point2D(xA,yA)
B=Point2D(xB,yB)
C=Point2D(xC,yC)
H=Hcenter(A,B,C)
G=Gcenter(A,B,C)
O=Ocenter(A,B,C)
rez=G.is_collinear(O,H)
print('The points are collinear : '+str(rez))
r=simplify(G.distance(H)/G.distance(O))
print('HG/GO : '+str(r))

