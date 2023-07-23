from sympy import *
x,y=symbols('x,y',real=True)

def parallelLine(A,line):
    l=line.equation()
    a=diff(l,x)
    b=diff(l,y)
    x1=A.x;y1=A.y
    return Line(simplify(a*(x-x1)+b*(y-y1)))
    
def angleBisector(B,A,C):
    xA=A.x;yA=A.y
    xB=B.x;yB=B.y
    xC=C.x;yC=C.y
    b=sqrt((xA-xC)**2+(yA-yC)**2)
    c=sqrt((xA-xB)**2+(yA-yB)**2)
    M=B+c*(C-B)/(b+c)
    return simplify(Line(A,M))

def Hcenter(A,B,C):
    hB=Line(A,C).perpendicular_line(B)
    hC=Line(A,B).perpendicular_line(C)
    return simplify(hB.intersection(hC)[0])
    
def Ocenter(A,B,C):
    sAC=Segment(A,C)
    sAB=Segment(A,B)
    mB=sAC.perpendicular_bisector()
    mC=sAB.perpendicular_bisector()
    return simplify(mB.intersection(mC)[0])
    
def Icenter(A,B,C):
    lB=angleBisector(A,B,C)
    lC=angleBisector(B,C,A)
    return simplify(lB.intersection(lC)[0])    
     
def Gcenter(A,B,C):
    return simplify((A+B+C)/3)     

def circumCircleRadius(A,B,C):
#    S=abs(area(A,B,C))
#    a=segment(B,C)
#    b=segment(A,C)
#    c=segment(A,B)
#    return simplify(a*b*c/(4*S))
    O=Ocenter(A,B,C)
    return A.distance(O)
    
    
def inCircleRadius(A,B,C):    
    S=Triangle(A,B,C).area
    a=B.distance(C)
    b=A.distance(C)
    c=A.distance(B)
    p=(a+b+c)/2
    return simplify(S/p)
    
