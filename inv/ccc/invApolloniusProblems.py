import sympy as smp
import pltObjLib as opl
import matplotlib.pyplot as plt
import sys

xA,yA,xB,yB,xC,yC,xD,yD,xE,yE = smp.symbols('xA,yA,xB,yB,xC,yC,xD,yD,xE,yE',real = True)

class invApolloniusProblems:
        
    def inv(self,A,B,C):
        R  =  A.distance(B)
        d  =  A.distance(C)
        return A+(R/d)**2*(C-A)
     
    def invL(self,A,B,C,D):
        C1  =  self.inv(A,B,C)
        D1  =  self.inv(A,B,D)
        return smp.Circle(A,C1,D1) 

    def invC(self,A,B,C,D):
        r1  =  A.distance(B)
        r2  =  C.distance(D)
        d  =  smp.Circle(C,r2)
        E0  =  smp.intersection(d,smp.Line(A,C));E1  =  E0[0];E2  =  E0[1]
        s  =  smp.Segment(E1,E2)
        F0  =  smp.intersection(d,s.perpendicular_bisector());F1  =  F0[0];F2  =  F0[1]
        P  =  self.inv(A,B,F1)
        Q  =  self.inv(A,B,F2)
        if(A.distance(C)  ==  r2):
           return smp.Line(P,Q) #{'obj':smp.Line(P,Q),'pnt1':P,'pnt2':Q}
        else:
           return smp.Circle(P,Q,self.inv(A,B,D))

    def tang(self,A,B,C,D):
        c  =  smp.Circle(A,A.distance(B))
        d  =  smp.Circle(C,C.distance(D))
        r1  =  c.radius
        r2  =  d.radius
        r  =  abs(r1-r2)
        if r !=  0:      
            if r1<r2:
                e  =  smp.Circle(C,r)
            else:
                e  =  smp.Circle(A,r)
            
            f  =  smp.Circle((A+C)/2,A.distance(C)/2)
            E0  =  smp.intersection(f,e);
            if len(E0) == 0:
                return []
            else:
                E  =  E0[0] 
                
            if r1<r2:
                F0  =  smp.intersection(d,smp.Ray(C,E));F  =  F0[0]
                g0  =  d.tangent_lines(F);g  =  g0[0]
            else:
                F0  =  smp.intersection(c,smp.Ray(A,E));F  =  F0[0]
                g0  =  c.tangent_lines(F);g  =  g0[0]
                
            h  =  g.reflect(smp.Line(A,C))
            if r1+r2 < A.distance(C):
                r  =  r1/(r1+r2)
                G0  =  smp.intersection(smp.Segment(A,C),smp.Circle(A,r*A.distance(C)));G  =  G0[0]
                l  =  d.tangent_lines(G)
                return [g,h,l[0],l[1]]
            else:
                return [g,h]
                
        else:
            E0  =  smp.intersection(c,smp.Line(A,C).perpendicular_line(A))
            p  =  c.tangent_lines(E0[0])
            q  =  c.tangent_lines(E0[1])
            return [p[0],q[0]]

    def parallelTangents(self,c,l):
        C = c.center
        p = l.perpendicular_line(C)
        T = smp.intersection(p,c)
        t1 = c.tangent_lines(T[0])
        t2 = c.tangent_lines(T[1])
        return [t1,t2]
      
    
    def invPCC(self,xA = 0,yA = 0,xB = 4,yB = -2,xC = 8,yC = 3,xD = 6,yD = 2,xE = -8,yE = 5):
        A  =  smp.Point(xA,yA)    
        B  =  smp.Point(xB,yB)    
        C  =  smp.Point(xC,yC)    
        D  =  smp.Point(xD,yD)    
        E  =  smp.Point(xE,yE)    
        F  =  smp.Point(xE+1,yE+1)

        c  =  smp.Circle(A,A.distance(B))
        d  =  smp.Circle(C,C.distance(D))
        e  =  self.invC(E,F,A,B)
        f  =  self.invC(E,F,C,D)
        
        if type(e) == smp.Line2D and (type(f) == smp.Line2D or type(f) == smp.Segment2D):
            if e.slope == f.slope:
                print('There exists an infinity number of solutions')
                s0=c.tangent_lines(E)
            else:
                print('The problem does not have solution')
                s0=[]
                
            t=[]
         
            
        if (type(e) == smp.Line2D or type(e) == smp.Segment2D) and type(f) == smp.Circle:
            t = self.parallelTangents(f,e)[0]
            
        if type(e) == smp.Circle and (type(f) == smp.Line2D or type(f) == smp.Segment2D):
            t = self.parallelTangents(e,f)[0]
    
        if type(e) == smp.Circle and type(f) == smp.Circle: 
            M  =  e.center
            P  =  smp.Point2D(M.x+e.radius,M.y)
            N  =  f.center
            Q  =  smp.Point2D(N.x+f.radius,N.y)
            t  =  self.tang(M,P,N,Q);

        obj   =   opl.plotObj(
            fig_height  =  12,
            fig_width  =  12,
            xMin  =  -30,
            xMax  =  30,
            yMin  =  -40,
            yMax  =  40,
            title  =  'PCC'
        )

        obj.pltPoint(xE,yE,color  =  'blue')
        obj.pltCircle(c.center.x,c.center.y,c.radius,color  =  'blue')
        obj.pltCircle(d.center.x,d.center.y,d.radius,color  =  'blue')
        
        
        for i in range(len(t)):
            h = t[i]    
            P  =  smp.Point2D(smp.N(h.p1.x),smp.N(h.p1.y)) 
            Q  =  smp.Point2D(smp.N(h.p2.x),smp.N(h.p2.y)) 
            s  =  self.invL(E,F,P,Q)
            obj.pltCircle(s.center.x,s.center.y,s.radius,color  =  'red')
        
        if t == [] and len(s0)>0:
           obj.pltLine(s0[0].p1.x,s0[0].p1.y,s0[0].p2.x,s0[0].p2.y,color = 'red')

        plt.show()

    def invPLC(self,xA = 0,yA = 5,xB = 0,yB = 2,xC = -3,yC = 0,xD = 3,yD = 0,xE = 4,yE = 4):
        A  =  smp.Point(xA,yA)    
        B  =  smp.Point(xB,yB)    
        C  =  smp.Point(xC,yC)    
        D  =  smp.Point(xD,yD)    
        E  =  smp.Point(xE,yE)    
        F  =  smp.Point(xE/2,yE/2)

        c  =  smp.Circle(A,A.distance(B))
        f  =  smp.Line(C,D)
        d = self.invC(E,F,A,B)
        e = self.invL(E,F,C,D)
        G = smp.Point2D(d.center.x+d.radius,d.center.y)
        t = self.tang(d.center,G,e.center,E)
        print(len(t))

        obj   =   opl.plotObj(
            fig_height  =  12,
            fig_width  =  12,
            xMin  =  -10,
            xMax  =  10,
            yMin  =  -1,
            yMax  =  19,
            title  =  'PLC'
        )

        obj.pltPoint(xE,yE,color  =  'blue')
        obj.pltCircle(A.x,A.y,A.distance(B),color  =  'blue')
        obj.pltLine(C.x,C.y,D.x,D.y,color  =  'blue')
        
        for i in range(len(t)):
            h  =  t[i]
            P  =  smp.Point2D(smp.N(h.p1.x),smp.N(h.p1.y)) 
            Q  =  smp.Point2D(smp.N(h.p2.x),smp.N(h.p2.y)) 
            s  =  self.invL(E,F,P,Q)
            obj.pltCircle(s.center.x,s.center.y,s.radius,color  =  'red')

        plt.show()
        
    def invPLL(self,xA = 0,yA = 0,xB = 4,yB = -2,xC = 5,yC = 3,xD = 6,yD = 2):   
        A = smp.Point(xA,yA)    
        B = smp.Point(xB,yB)    
        C = smp.Point(xC,yC)    
        D = smp.Point(xD,yD)    
        E = smp.Point(xD+1,yD+1)    

        f = smp.Line(A,B)
        g = smp.Line(A,C)  
        c = self.invL(D,E,A,B)
        c = smp.N(c)
        d = self.invL(D,E,A,C)
        d = smp.N(d)
        t = self.tang(c.center,D,d.center,D)
        h = t[0]
        i = t[1]
        P = smp.Point2D(smp.N(h.p1.x),smp.N(h.p1.y)) 
        Q = smp.Point2D(smp.N(h.p2.x),smp.N(h.p2.y)) 
        R = smp.Point2D(smp.N(i.p1.x),smp.N(i.p1.y))  
        S = smp.Point2D(smp.N(i.p2.x),smp.N(i.p2.y)) 

        s1 = self.invL(D,E,P,Q)
        s2 = self.invL(D,E,R,S)

        obj  =  opl.plotObj(
            fig_height = 12,
            fig_width = 12,
            xMin = -2,
            xMax = 20,
            yMin = -10,
            yMax = 10,
            title = 'PLL'
        )

        obj.pltPoint(xA,yA,label = 'A')
        obj.pltPoint(xB,yB,label = 'B')
        obj.pltPoint(xC,yC,label = 'C')
        obj.pltPoint(xD,yD,label = 'D',color = 'blue')
        obj.pltLine(xA,yA,xB,yB,color = 'blue')
        obj.pltLine(xA,yA,xC,yC,color = 'blue')
        obj.pltCircle(s1.center.x,s1.center.y,s1.radius,color = 'red')
        obj.pltCircle(s2.center.x,s2.center.y,s2.radius,color = 'red')

        plt.show()
    
    def invPPL(self,xA = 0,yA = 0,xB = 2,yB = 2,xC = 5,yC = 0,xD = 1,yD = 20/3):  
        A = smp.Point(xA,yA)    
        B = smp.Point(xB,yB)    
        C = smp.Point(xC,yC)    
        D = smp.Point(xD,yD)    
        E = smp.Point(xD+1,yD+1)    
            
        c = smp.Circle(A,A.distance(E))
        f = smp.Line2D(C,D)
        B1 = self.inv(A,E,B)
        d = self.invL(A,E,C,D)
        t = d.tangent_lines(B1)
        T10 = smp.intersection(d,t[0]);T1 = T10[0]
        T20 = smp.intersection(d,t[1]);T2 = T20[0]
        e = self.invL(A,E,B1,T2)
        g = self.invL(A,E,B1,T1)

        obj  =  opl.plotObj(
            fig_height = 12,
            fig_width = 12,
            xMin = -7,
            xMax = 7,
            yMin = -6,
            yMax = 8,
            title = 'PPL'
        )

        obj.pltPoint(xA,yA,label = 'A')
        obj.pltPoint(xB,yB,label = 'B')
        obj.pltPoint(xC,yC,label = 'C',color = 'blue')
        obj.pltPoint(xD,yD,label = 'D',color = 'blue')
        obj.pltLine(xC,yC,xD,yD,color = 'blue')
        obj.pltCircle(e.center.x,e.center.y,e.radius,color = 'red')
        obj.pltCircle(g.center.x,g.center.y,g.radius,color = 'red')

        plt.show()
        
    def invPPC(self,xA = 0,yA = 0,xB = 2,yB = 2,xC = 5,yC = 0,xD = 1,yD = 20/3):       
        A = smp.Point(xA,yA)    
        B = smp.Point(xB,yB)    
        C = smp.Point(xC,yC)    
        D = smp.Point(xD,yD)    
        E = smp.Point(xD+1,yD+1)    
            
        c = smp.Circle(C,C.distance(D))
        B1 = self.inv(A,E,B)
        e = self.invC(A,E,C,D)
        obj  =  opl.plotObj(
            fig_height = 12,
            fig_width = 12,
            xMin = -15,
            xMax = 15,
            yMin = -9,
            yMax = 9,
            title = 'PPC'
        )

        obj.pltPoint(xA,yA,label = 'A',color = 'blue')
        obj.pltPoint(xB,yB,label = 'B',color = 'blue')
        obj.pltCircle(xC,yC,C.distance(D),color = 'blue')

        if type(e) == smp.Circle:
            t = e.tangent_lines(B1)
            if t != []:    
                T10 = smp.intersection(e,t[0]);T1 = T10[0]
                T20 = smp.intersection(e,t[1]);T2 = T20[0]
                f = self.invL(A,E,B1,T2)
                g = self.invL(A,E,B1,T1)
                obj.pltCircle(f.center.x,f.center.y,f.radius,color = 'red')
                obj.pltCircle(g.center.x,g.center.y,g.radius,color = 'red')
                
        elif type(e) == smp.Line2D:
            g = e.parallel_line(B1)
            f = self.invL(A,E,g.p1,g.p2)
            obj.pltCircle(f.center.x,f.center.y,f.radius,color = 'red')
            
        plt.show()