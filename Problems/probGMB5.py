
"""
In the triangle $ABC$, the side $AC$ is divided by the points $B_1, B_2$
into three congruent parts, $AB_2=B_2B_1=B_1C,$ and side $AB$ is divided
of the points $C_1,C_2$ also in three congruent parts, $AC_1=C_1C_2=C_2B.$ The intersection
segments $BB_1, BB_2, CC_1, CC_2$ determine a quadrilateral inside the triangle.
Show that the area of the quadrilateral is $\frac{9}{70}$ of the area of the triangle $ABC.$
"""

from sympy import *
x,y,xA,yA,xB,yB,xC,yC=symbols('x,y,xA,yA,xB,yB,xC,yC',real=True)

A=Point(xA,yA)
B=Point(xB,yB)
C=Point(xC,yC)
B1=C+(A-C)/3
B2=C+2*(A-C)/3
C1=B+2*(A-B)/3
C2=B+(A-B)/3
M0=intersection(Line(B,B2),Line(C,C1));M=M0[0]
N0=intersection(Line(B,B2),Line(C,C2));N=N0[0]
P0=intersection(Line(B,B1),Line(C,C2));P=P0[0]
Q0=intersection(Line(B,B1),Line(C,C1));Q=Q0[0]
S=Triangle(A,B,C).area
s=factor(Triangle(M,N,P).area+Triangle(M,P,Q).area)
print('s/S = '+str(simplify(abs(s/S))))

