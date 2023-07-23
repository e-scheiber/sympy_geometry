"""
Let the parallelogram $ABCD.$ Let $CE\perp BC,\ AE \perp AB.$ Shown that
$ED \perp AC.$
"""


import sympy as smp
from geom2D import *
xA,yA,xB,yB,xC,yC=smp.symbols('xA,yA,xB,yB,xC,yC',real=True)

# ----------------------------------------------------------------------------
A=smp.Point(xA,yA)
B=smp.Point(xB,yB)
C=smp.Point(xC,yC)
l1=smp.Line(A,B)
l2=smp.Line(B,C)
l3=parallelLine(C,l1)
l4=parallelLine(A,l2)
D0=smp.intersection(l3,l4);D=D0[0]
E0=smp.intersection(l2.perpendicular_line(C),l1.perpendicular_line(A));E=E0[0]
# ----------------------------------------------------------------------------
rez=smp.Line(A,C).is_perpendicular(smp.Line(D,E))
print('The lines are perpendicular : '+str(rez))

import objPltLibrary as opl
import matplotlib.pyplot as plt

xA=0;yA=0
xB=4;yB=0
xC=5;yC=2
# ----------------------------------------------------------------------------
A=smp.Point(xA,yA)
B=smp.Point(xB,yB)
C=smp.Point(xC,yC)
l1=smp.Line(A,B)
l2=smp.Line(B,C)
l3=parallelLine(C,l1)
l4=parallelLine(A,l2)
D0=smp.intersection(l3,l4);D=D0[0]
E0=smp.intersection(l2.perpendicular_line(C),l1.perpendicular_line(A));E=E0[0]
# ----------------------------------------------------------------------------

obj = opl.plotObj(
    fig_height=10,
    fig_width=10,
    xMin=-2,
    xMax=8,
    yMin=-2,
    yMax=8,
    title='Prob10p9'
)

obj.pltPoint(xA,yA,label='A')
obj.pltPoint(xB,yB,label='B')
obj.pltPoint(xC,yC,label='C')
xD=D.x;yD=D.y
xE=E.x;yE=E.y
obj.pltPoint(xD,yD,label='D')
obj.pltPoint(xE,yE,label='E')
x=[xA,xB,xC,xD,xA]
y=[yA,yB,yC,yD,yA]
label=['','','','']
obj.pltPolygonalLine(x,y,label)

obj.pltLine(xD,yD,xE,yE,label='p',color='blue')
obj.pltSegment(xA,yA,xC,yC,label='q',color='red')

plt.show()
