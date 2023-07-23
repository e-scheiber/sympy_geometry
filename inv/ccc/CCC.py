import sympy as smp
#import objPltLibrary as opl
#import matplotlib.pyplot as plt
#import invApolloniusProblems as iap
import CCCutils as uts

# Case 1
#xP1 = 0;yP1 = 0;xP2 = 0;yP2 = 2;xP3 = 5;yP3 = 5;xP4 = 5;yP4 = 7;xP5 = 3;yP5 = -3;xP6 = 3;yP6 = -1;  
# Case 2
xP1 = 0;yP1 = 0;xP2 = 0;yP2 = 4;xP3 = 10;yP3 = 1;xP4 = 12;yP4 = 1;xP5 = -5;yP5 = -2;xP6 = -5;yP6 = -4  
# Case 3
#xP1 = -3;yP1  = 2;xP2  = -1;yP2  = 5;xP3 = 4;yP3 = 6;xP4 = 6;yP4 = 4;xP5 = 0;yP5 = -2;xP6 = 1;yP6 = -2  
#xP1 = 0;yP1 = 5;xP2  = 0;yP2 = 2;xP3 = -3;yP3 = 0;xP4 = 3;yP4 = 0;xP5 = 4;yP5 = 4;xP6 = 5;yP6 = 3   
#xP1 = 0;yP1 = 0;xP2 = -4.61;yP2 = 5.75;xP3 = 13.21;yP3 = -1.34;xP4 = 10.02;yP4 = 1.09;xP5 = 7.08;yP5 = -10.32;xP6 = 5.18;yP6 = -11.23
#xP1 = 0;yP1 = 0;xP2 = 0;yP2 = 4;xP3 = 3;yP3 = 1;xP4 = 7;yP4 = 1;xP5 = -5;yP5 = -2;xP6 = -5;yP6 = -3
#xP1 = 0;yP1 = 0;xP2 = 0;yP2 = 4;xP3 = 10;yP3 = 1;xP4 = 14;yP4 = 1;xP5 = -5;yP5 = -2;xP6 = -5;yP6 = -3

P1 = smp.Point(xP1,yP1)
P2 = smp.Point(xP2,yP2)
P3 = smp.Point(xP3,yP3)
P4 = smp.Point(xP4,yP4)
P5 = smp.Point(xP5,yP5)
P6 = smp.Point(xP6,yP6)
r1 = P1.distance(P2)
r3 = P3.distance(P4)
r5 = P5.distance(P6)
r = [r1,r5,r3]
s = sorted(r,reverse = True)
if s[0] == s[2]:
    A = P1;B = P2;C = P3;D = P4;E = P5;F = P6
else:
    idx = [1,2,3,4,5,6]

    if s[0] == r1:
        A = P1;B = P2
        idx.remove(1);idx.remove(2)
    elif s[0] == r3:
        A = P3;B = P4
        idx.remove(3);idx.remove(4)
    else:
        A = P5;B = P6
        idx.remove(5);idx.remove(6)
     
    if s[2] == r1:
        E = P1;F = P2
        idx.remove(1);idx.remove(2)
    elif s[2] == r3:
        E = P3;F = P4
        idx.remove(3);idx.remove(4)
    else:
        E = P5;F = P6 
        idx.remove(5);idx.remove(6)

    if idx[0] == 1:
        C = P1;D = P2
    elif idx[0] == 3:
        C = P3;D = P4
    else:
        C = P5;D = P6

#print([A,B,C,D,E,F])
if s[0] >= s[1] and s[1] > s[2]:
    uts.invCCC1(A.x,A.y,B.x,B.y,C.x,C.y,D.x,D.y,E.x,E.y,F.x,F.y)
    
if s[0] > s[1] and s[1] == s[2]:
    uts.invCCC2(A.x,A.y,B.x,B.y,C.x,C.y,D.x,D.y,E.x,E.y,F.x,F.y)
    
if s[0] == s[2]:    
    uts.CCC3(A.x,A.y,B.x,B.y,C.x,C.y,D.x,D.y,E.x,E.y,F.x,F.y)