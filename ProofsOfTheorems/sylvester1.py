from sympy import *
from geom2D import *
from sympy.vector import CoordSys3D

R = CoordSys3D('R')
xA,yA,xB,yB,xC,yC,xM,yM=symbols('xA,yA,xB,yB,xC,yC,xM,yM',real=True)
A=Point(xA,yA)
B=Point(xB,yB)
C=Point(xC,yC)
M=Point(xM,yM)

def symExpr(M,A,B,C):
    #rA=A.x*R.i+A.y*R.j
    #rB=B.x*R.i+B.y*R.j
    #rC=C.x*R.i+C.y*R.j
    rM=M.x*R.i+M.y*R.j
    H=Hcenter(A,B,C)
    rH=H.x*R.i+H.y*R.j
    O=Ocenter(A,B,C)
    rO=O.x*R.i+O.y*R.j
    return 2*rO+rH-3*rM 
    
 
    
H=Hcenter(A,B,C)
rH=H.x*R.i+H.y*R.j
O=Ocenter(A,B,C)
rO=O.x*R.i+O.y*R.j
exp1=simplify(symExpr(O,A,B,C)-rH+rO)
print('M=O : '+ str(exp1))  

G=(A+B+C)/3
exp2=simplify(symExpr(G,A,B,C))
print('M=G : '+ str(exp2)) 

exp3= simplify(symExpr(H,A,B,C)-2*(rO-rH))
print('M=H : '+ str(exp3))