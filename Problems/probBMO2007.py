"""
 In the convex quadrilateral $ABCD,$ points $M,N$ lie on the side $AB$ 
 such that $AM = MN =NB,$ and points $P, Q$ lie on the side $CD$ such 
 that $CP = PQ = QD.$ Prove that Area of $AMCP$ = Area of $MNPQ = \frac{1}{3}$ 
 Area of $ABCD.$
"""



from sympy import *
# from geom import *
xA,yA,xB,yB,xC,yC,xD,yD=symbols('xA,yA,xB,yB,xC,yC,xD,yD',real=True)

A=Point(xA,yA)
B=Point(xB,yB)
C=Point(xC,yC)
D=Point(xD,yD)
M=A+(B-A)/3
N=A+2*(B-A)/3
Q=D+(C-D)/3
P=D+2*(C-D)/3
    
S=Polygon(A,B,C,D).area

# areaOfTriangle of APCM
s1=Polygon(A,P,C,M).area
print('s1/S = '+str(simplify(abs(s1/S))))

# areaOfTriangle of MQPN
s2=Polygon(M,Q,P,N).area
print('s2/S = '+str(simplify(abs(s2/S))))

