import invApolloniusProblems as iap
import sympy as smp
import sys

lst0 = sys.argv;prob = lst0[1]
app  =  iap.invApolloniusProblems()

if prob == 'PPL':
    # Test invPPL(A,B,C,D)
    # A,B Points
    # Line(C,D)
    app.invPPL()
    #xA = 0;yA = 0;xB = 2;yB = 2;xC = 5;yC = 0;xD = 1;yD = 20/3
    #app.invPPL(xA,yA,xB,yB,xC,yC,xD,yD)
elif prob == 'PPC':
    # Test invPPC(A,B,C,D)
    # A,B Points
    # Circle(C,|CD|)
    app.invPPC()
    #xA = 0;yA = 0;xB = 0;yB = 3;xC = 4;yC = 3;xD = 4;yD = 8
    #xA = 10;yA = 1;xB = -5;yB = -2;xC = 0;yC = 0;xD = 0;yD = 6
    #app.invPPC(xA,yA,xB,yB,xC,yC,xD,yD)
elif prob == 'PCC':
    # Test invPCC
    # Circle(A,|AB|)
    # Circle(C,|CD|)
    # E Point
    app.invPCC()
    #xA = 0;yA = 0;xB = 4;yB = -2;xC = 8;yC = 3;xD = 6;yD = 2;xE = 8;yE = 5  #;xF  =  6;yF  =  6    # 2 solutii    
    #xA = -3;yA = 2;xB = -0.808662286909106;yB = 2;xC = 4;yC = 6;xD = 5.41421356237309;yD = 6;xE = 0;yE = -2
    #xA = -3;yA = 2;xB = 1.60555127546399;yB = 2;xC = 4;yC = 6;xD = 5;yD = 6;xE = 0;yE = -2
    #xA = 0;yA = 0;xB = 5.263164108007687;yB = 0;xC = 13.21;yC = -1.34;xD = 15.1134323656018;yD = -1.34;xE = 7.08;yE = -10.32
    #xA = 10;yA = 1;xB = -5;yB = -2;xC = 0;yC = 0;xD = 0;yD = 4;xE = -5;yE = 0  # 0 solutii
    #xA=0;yA=0;xB=0;yB=5;xC=2;yC=0;xD=2;yD=3;xE=5;yE=0 # infinitate
    #xA=0;yA=0;xB=0;yB=4;xC=6;yC=0;xD=6;yD=3;xE=43/12;yE=smp.sqrt(455)/12
    #app.invPCC(xA,yA,xB,yB,xC,yC,xD,yD,xE,yE)
elif prob == 'PLC':
    # Test invPLC(A,B,C,D,E)
    # Circle(A,|AB|)
    # Line(C,D)
    # E Point
    # xA  =  0;yA  =  0;xB  =  4;yB  =  -2;xC  =  8;yC  =  3;xD  =  6;yD  =  2;xE  =  -8;yE  =  5 #;xF  =  -6;yF  =  6   # 2 solutii
    app.invPLC()
elif prob == 'PLL':
    # Line(A,B), Line(A,C)
    # D Point
    # Test invPLL(A,B,C,D)
    app.invPLL()
else:
    print('Wrong parameter')
    
    
