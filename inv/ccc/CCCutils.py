import sympy as smp
import invApolloniusProblems as iap
import objPltLibrary as opl
import matplotlib.pyplot as plt
import pltObjLib as sopl

app  =  iap.invApolloniusProblems()

def invPPC(xA,yA,xB,yB,xC,yC,xD,yD):       
        A = smp.Point(xA,yA)    
        B = smp.Point(xB,yB)    
        C = smp.Point(xC,yC)    
        D = smp.Point(xD,yD)    
        E = smp.Point(xD+1,yD+1)            
        c = smp.Circle(C,C.distance(D))
        B1 = app.inv(A,E,B)
        e = app.invC(A,E,C,D)

        rez = []
        if type(e) == smp.Circle:
            t = e.tangent_lines(B1)
            if t != []:
                T10 = smp.intersection(e,t[0]);T1 = T10[0]
                T20 = smp.intersection(e,t[1]);T2 = T20[0]
                f = app.invL(A,E,B1,T2)
                g = app.invL(A,E,B1,T1)
                rez.append(f)
                rez.append(g)
                
        elif type(e) == smp.Line2D:
            g = e.parallel_line(B1)
            f = app.invL(A,E,g.p1,g.p2)
            rez.append(f)
            
        return rez
        
def invPCC(xA,yA,xB,yB,xC,yC,xD,yD,xE,yE):
    A  =  smp.Point(xA,yA)    
    B  =  smp.Point(xB,yB)    
    C  =  smp.Point(xC,yC)    
    D  =  smp.Point(xD,yD)    
    E  =  smp.Point(xE,yE)    
    F  =  smp.Point(xE+1,yE+1)

    c  =  smp.Circle(A,A.distance(B))
    d  =  smp.Circle(C,C.distance(D))
    e  =  app.invC(E,F,A,B)
    f  =  app.invC(E,F,C,D)
    
    if type(e) == smp.Line2D and (type(f) == smp.Line2D or type(f) == smp.Segment2D):
        if A.distance(C) == A.distance(E)+C.distance(E):
            print('There exists an inifnity number of solutions')
        else:
            print('The problem does not have solution')
            
        t = []
        
    if (type(e) == smp.Line2D or type(e) == smp.Segment2D) and type(f) == smp.Circle:
        t = app.parallelTangents(f,e)[0]
        
    if type(e) == smp.Circle and (type(f) == smp.Line2D or type(f) == smp.Segment2D):
        t = app.parallelTangents(e,f)[0]

    if type(e) == smp.Circle and type(f) == smp.Circle: 
        M  =  e.center
        P  =  smp.Point2D(M.x+e.radius,M.y)
        N  =  f.center
        Q  =  smp.Point2D(N.x+f.radius,N.y)
        t  =  app.tang(M,P,N,Q);

    rez = []
    for i in range(len(t)):
        h = t[i]    
        P  =  smp.Point2D(smp.N(h.p1.x),smp.N(h.p1.y)) 
        Q  =  smp.Point2D(smp.N(h.p2.x),smp.N(h.p2.y)) 
        s  =  app.invL(E,F,P,Q)
        rez.append(s)

    return rez
                 
def isSolution(O,r,c,d,e):
    iS = 0   
    #0 - No solition;
    #1 - solition with -; 2 - solution with +
    r_E = e.radius
    A = c.center;r1 = c.radius
    C = d.center;r2 = d.radius
    p = smp.Circle(O,r+r_E)
    q = smp.Circle(O,r-r_E)
    
    M = smp.intersection(smp.Line2D(A,O),p)
    N = smp.intersection(smp.Line2D(C,O),p)
    P = smp.intersection(smp.Line2D(A,O),q)
    Q = smp.intersection(smp.Line2D(C,O),q)
    if ((abs(M[0].distance(A)-r1)<10**(-8) or abs(M[1].distance(A)-r1)<10**(-8))
        and 
        (abs(N[0].distance(C)-r2)<10**(-8) or abs(N[1].distance(C)-r2)<10**(-8))
    ):
        return 2
    elif ((abs(P[0].distance(A)-r1)<10**(-8) or abs(P[1].distance(A)-r1)<10**(-8))
        and 
        (abs(Q[0].distance(C)-r2)<10**(-8) or abs(Q[1].distance(C)-r2)<10**(-8))
    ):
        return 1
    else:
        return 0
        
def invCCC1(xA,yA,xB,yB,xC,yC,xD,yD,xE,yE,xF,yF):

    A  =  smp.Point(xA,yA)    
    B  =  smp.Point(xB,yB)    
    C  =  smp.Point(xC,yC)    
    D  =  smp.Point(xD,yD)    
    E  =  smp.Point(xE,yE)    
    F  =  smp.Point(xF,yF)
    r_A = A.distance(B);c = smp.Circle(A,r_A) #smp.N(A),smp.N(r_A))
    r_C = C.distance(D);d = smp.Circle(C,r_C) #smp.N(C),smp.N(r_C))
    r_E = E.distance(F);e = smp.Circle(E,r_E) #smp.N(E),smp.N(r_E))
    print('r_A : '+str(smp.N(r_A)))
    print('r_C : '+str(smp.N(r_C)))
    print('r_E : '+str(smp.N(r_E)))

    nrows  =  2
    ncols  =  2
    obj   =   opl.GridObjPlot(
        nrows = nrows,
        ncols = ncols,
        fig_height = 12,
        fig_width = 12,
        xMin = -20,
        xMax = 20,
        yMin = -20,
        yMax = 20,
        title = 'CCC'
    )

    obj_plots  =  [
        [opl.plotObj(obj.axes[row][col]) for col in range(ncols)]
        for row in range(nrows)
    ]

    # Case 1
    print('Case 1')
    r1  =  A.distance(B)+E.distance(F)
    c1  =  smp.Circle(A,r1)
    B1  =  smp.Point2D(A.x+r1,A.y)
    r2  =  C.distance(D)+E.distance(F)
    d1  =  smp.Circle(C,r2)
    D1  =  smp.Point2D(C.x+r2,C.y)
    obj_plots[0][0].pltCircle(A.x,A.y,A.distance(B),color = 'blue')
    obj_plots[0][0].pltCircle(C.x,C.y,C.distance(D),color = 'blue')
    obj_plots[0][0].pltCircle(E.x,E.y,E.distance(F),color = 'blue')
    s = invPCC(smp.N(A.x),smp.N(A.y),smp.N(B1.x),smp.N(B1.y),smp.N(C.x),smp.N(C.y),smp.N(D1.x),smp.N(D1.y),smp.N(E.x),smp.N(E.y))
    print(len(s))
    if len(s) == 0:
        print('Case 1 does not have solution')
    else:
        for i in range(len(s)):    
            O = s[i].center
            r = s[i].radius
            p = isSolution(O,r,c,d,e)
            print(p)
            if p != 0:
                rho = r+(-1)**p*E.distance(F)       
                obj_plots[0][0].pltCircle(O.x,O.y,rho,color  =  'red')

    # Case 2
    print('Case 2')
    r1  =  A.distance(B)-E.distance(F)
    c1  =  smp.Circle(A,r1)
    B1  =  smp.Point2D(A.x+r1,A.y)
    r2  =  C.distance(D)-E.distance(F)
    d1  =  smp.Circle(C,r2)
    D1  =  smp.Point2D(C.x+r2,C.y)
    obj_plots[0][1].pltCircle(A.x,A.y,A.distance(B),color = 'blue')
    obj_plots[0][1].pltCircle(C.x,C.y,C.distance(D),color = 'blue')
    obj_plots[0][1].pltCircle(E.x,E.y,E.distance(F),color = 'blue')
    s = invPCC(smp.N(A.x),smp.N(A.y),smp.N(B1.x),smp.N(B1.y),smp.N(C.x),smp.N(C.y),smp.N(D1.x),smp.N(D1.y),smp.N(E.x),smp.N(E.y))
    print(len(s))
    if len(s) == 0:
        print('Case 2 does not have solution')
    else:
        for i in range(len(s)):
            O = s[i].center
            r = s[i].radius   
            p = isSolution(O,r,c,d,e)
            print(p)
            if p != 0:
                rho = r+(-1)**p*E.distance(F)       
                obj_plots[0][1].pltCircle(O.x,O.y,rho,color  =  'red')
             

    # Case 3
    print('Case 3')
    r1  =  A.distance(B)-E.distance(F)
    c1  =  smp.Circle(A,r1)
    B1  =  smp.Point2D(A.x+r1,A.y)
    r2  =  C.distance(D)+E.distance(F)
    d1  =  smp.Circle(C,r2)
    D1  =  smp.Point2D(C.x+r2,C.y)
    obj_plots[1][0].pltCircle(A.x,A.y,A.distance(B),color = 'blue')
    obj_plots[1][0].pltCircle(C.x,C.y,C.distance(D),color = 'blue')
    obj_plots[1][0].pltCircle(E.x,E.y,E.distance(F),color = 'blue')
    s = invPCC(smp.N(A.x),smp.N(A.y),smp.N(B1.x),smp.N(B1.y),smp.N(C.x),smp.N(C.y),smp.N(D1.x),smp.N(D1.y),smp.N(E.x),smp.N(E.y))
    print(len(s))
    if len(s) == 0:
        print('Case 3 does not has solution')
    else:
        for i in range(len(s)):
            O = s[i].center
            r = s[i].radius   
            p = isSolution(O,r,c,d,e)
            print(p)
            if p != 0:
                rho = r+(-1)**p*E.distance(F)       
                obj_plots[1][0].pltCircle(O.x,O.y,rho,color  =  'red')
                
    # Case 4
    print('Case 4')
    r1  =  A.distance(B)+E.distance(F)
    c1  =  smp.Circle(A,r1)
    B1  =  smp.Point2D(A.x+r1,A.y)
    r2  =  C.distance(D)-E.distance(F)
    d1  =  smp.Circle(C,r2)
    D1  =  smp.Point2D(C.x+r2,C.y)
    obj_plots[1][1].pltCircle(A.x,A.y,A.distance(B),color = 'blue')
    obj_plots[1][1].pltCircle(C.x,C.y,C.distance(D),color = 'blue')
    obj_plots[1][1].pltCircle(E.x,E.y,E.distance(F),color = 'blue')
    s = invPCC(smp.N(A.x),smp.N(A.y),smp.N(B1.x),smp.N(B1.y),smp.N(C.x),smp.N(C.y),smp.N(D1.x),smp.N(D1.y),smp.N(E.x),smp.N(E.y))
    print(len(s))
    if len(s) == 0:
        print('Case 4 does not has solution')
    else:
        for i in range(len(s)):
            O = s[i].center
            r = s[i].radius
            p = isSolution(O,r,c,d,e)
            print(p)
            if p != 0:
                rho = r+(-1)**p*E.distance(F)       
                obj_plots[1][1].pltCircle(O.x,O.y,rho,color  =  'red')
                
    plt.show()
    
def invCCC2(xA,yA,xB,yB,xC,yC,xD,yD,xE,yE,xF,yF):
    A  =  smp.Point(xA,yA)    
    B  =  smp.Point(xB,yB)    
    C  =  smp.Point(xC,yC)    
    D  =  smp.Point(xD,yD)    
    E  =  smp.Point(xE,yE)    
    F  =  smp.Point(xF,yF)
    r_A = A.distance(B);c = smp.Circle(A,r_A) 
    r_C = C.distance(D);d = smp.Circle(C,r_C) 
    r_E = E.distance(F);e = smp.Circle(E,r_E) 
    print('r_A : '+str(smp.N(r_A)))
    print('r_C : '+str(smp.N(r_C)))
    print('r_E : '+str(smp.N(r_E)))
        
    nrows  =  1
    ncols  =  2
    obj   =   opl.GridObjPlot(
        nrows = nrows,
        ncols = ncols,
        fig_height = 18,
        fig_width = 18,
        xMin = -20,
        xMax = 20,
        yMin = -20,
        yMax = 20,
        title = 'CCC'
    )

    obj_plots  =  [
        [opl.plotObj(obj.axes[row][col]) for col in range(ncols)]
        for row in range(nrows)
    ]

    # Case 1
    print('Case 1')
    r1  =  A.distance(B)+E.distance(F)
    c1  =  smp.Circle(A,r1)
    B1  =  smp.Point2D(A.x+r1,A.y)
    obj_plots[0][0].pltCircle(A.x,A.y,A.distance(B),color = 'blue')
    obj_plots[0][0].pltCircle(C.x,C.y,C.distance(D),color = 'blue')
    obj_plots[0][0].pltCircle(E.x,E.y,E.distance(F),color = 'blue')
    s = invPPC(smp.N(C.x),smp.N(C.y),smp.N(E.x),smp.N(E.y),smp.N(A.x),smp.N(A.y),smp.N(B1.x),smp.N(B1.y))
    print(len(s))
    if len(s) == 0:
        print('Case 1 does not have solution')
    else:
        for i in range(len(s)):    
            O = s[i].center
            r = s[i].radius 
            p = isSolution(O,r,c,d,e)
            print(p)
            if p != 0:
                rho = r+(-1)**p*E.distance(F)       
                obj_plots[0][0].pltCircle(O.x,O.y,rho,color  =  'red')

    # Case 2
    print('Case 2')
    r1  =  A.distance(B)-E.distance(F)
    c1  =  smp.Circle(A,r1)
    B1  =  smp.Point2D(A.x+r1,A.y)
    obj_plots[0][1].pltCircle(A.x,A.y,A.distance(B),color = 'blue')
    obj_plots[0][1].pltCircle(C.x,C.y,C.distance(D),color = 'blue')
    obj_plots[0][1].pltCircle(E.x,E.y,E.distance(F),color = 'blue')
    s = invPPC(smp.N(C.x),smp.N(C.y),smp.N(E.x),smp.N(E.y),smp.N(A.x),smp.N(A.y),smp.N(B1.x),smp.N(B1.y))
    print(len(s))
    if len(s) == 0:
        print('Case 2 does not have solution')
    else:
        for i in range(len(s)):
            O = s[i].center
            r = s[i].radius 
            print('i : '+str(smp.N(r)))
            print(smp.N(O))
            p = isSolution(O,r,c,d,e)
            print(p)
            if p != 0:
                rho = r+(-1)**p*E.distance(F)       
                obj_plots[0][1].pltCircle(O.x,O.y,rho,color  =  'red')
                        
    plt.show()

def CCC3(xA,yA,xB,yB,xC,yC,xD,yD,xE,yE,xF,yF):
    A = smp.Point2D(xA,yA)
    B = smp.Point2D(xB,yB)
    C = smp.Point2D(xC,yC)
    E = smp.Point2D(xE,yE)
    r = A.distance(B)

    c = smp.Circle(A,C,E)
    print('c : '+str(type(c)))
    print(c)
    O = c.center
    rho = c.radius
    p = smp.Circle(O,r+rho)
    q = smp.Circle(O,rho-r)

    obj   =   sopl.plotObj(
                fig_height  =  12,
                fig_width  =  12,
                xMin  =  -5,
                xMax  =  15,
                yMin  =  -10,
                yMax  =  10,
                title  =  'CCC'
            )
            
    obj.pltCircle(A.x,A.y,r,color = 'blue')
    obj.pltCircle(C.x,C.y,r,color = 'blue')
    obj.pltCircle(E.x,E.y,r,color = 'blue')
    obj.pltCircle(p.center.x,p.center.y,p.radius,color = 'red')
    obj.pltCircle(q.center.x,q.center.y,q.radius,color = 'red')

    plt.show()