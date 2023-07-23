from sympy import *
#from geom import *
xA,yA,xB,yB,xC,yC=symbols('xA,yA,xB,yB,xC,yC',real=True)

A=Point2D(xA,yA)
B=Point2D(xB,yB)
C=Point2D(xC,yC)
N=Line(A,B).random_point()
P=Line(A,C).random_point()
S0=intersection(Line(C,N),Line(B,P));S=S0[0]
M0=intersection(Line(A,S),Line(B,C));M=M0[0]
r1=(M.distance(B)/M.distance(C))
r2=(P.distance(C)/P.distance(A))
r3=(N.distance(A)/N.distance(B))
r=simplify(r1*r2*r3)
print(r)

