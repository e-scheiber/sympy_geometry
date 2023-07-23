from sympy import *
#from geom import *
xA,yA,xB,yB,xC,yC=symbols('xA,yA,xB,yB,xC,yC',real=True)

A=Point2D(xA,yA)
B=Point2D(xB,yB)
C=Point2D(xC,yC)
c=Circle(A,B,C)
print('c : '+str(c))
S=c.random_point()
print('S : '+str(S))
M=intersection(Line(B,C),Line(B,C).perpendicular_line(S))
print('M : '+str(M))
N=intersection(Line(A,C),Line(A,C).perpendicular_line(S))
print('N : '+str(N))
P=intersection(Line(A,B),Line(A,B).perpendicular_line(S))
print('P : '+str(P))
rez=M.is_collinear(N,P)
print('Are collinear : '+str(rez))


