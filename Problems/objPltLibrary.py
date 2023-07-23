import matplotlib.pyplot as plt
import numpy as np

class plotObj:
  INCH_TO_CM = 1/2.54
  
  def __init__(self, fig_height, fig_width, title='',xMin=-15, xMax=-15, yMin=-15, yMax=15):
    self.xMin = xMin
    self.xMax = xMax
    self.yMin = yMin
    self.yMax = yMax
    figsize = (fig_height * plotObj.INCH_TO_CM, fig_width * plotObj.INCH_TO_CM)
    figure, axes = plt.subplots(figsize=figsize)
    self.figure = figure
    self.axes = axes
    self.axes.set_xlim(xMin,xMax)
    self.axes.set_ylim(yMin,yMax)
    self.axes.set_aspect(1)
    figure.suptitle(title)
  
  def pltPoint(self,x,y,label='',color='black'):
    self.axes.plot(x,y,color=color,marker='o')
    self.axes.annotate(label, xy=(x + 0.1, y + 0.2)) #,xycoords='data',fontsize=10)
      
  def pltSegment(self,xA,yA,xB,yB,label='',color='black'):
    n=5
    t=np.linspace(0,1,n)
    if xA==xB:
        x=xA*np.ones(n)
        y=yA++t*(yB-yA)
    else:
        x=xA+t*(xB-xA)
        y=yA+(yB-yA)/(xB-xA)*(x-xA)
        
    self.axes.plot(x,y,color=color)
    self.axes.annotate(label, xy=(0.5*(xA+xB)+0.5, 0.5*(yA+yB) - 0.5))
      
  def pltLine(self,xA,yA,xB,yB,label='',color='black'):  
    if xA == xB:
        x1=x2=xA
        y1=self.yMin
        y2=self.yMax
        self.pltSegment(x1,y1,x2,y2,label=label,color=color)
    else:
        m=(yB-yA)/(xB-xA)
        n=yA-xA*m
        x=np.linspace(self.xMin,self.xMax,20)
        y=m*x+n
        self.axes.plot(x,y,color=color)
        self.axes.annotate(label, xy=(self.xMin+0.1, m*self.xMin+n+0.1))
        self.pltPoint(xA,yA,'')
        self.pltPoint(xB,yB,'')

  def pltCircle(self,xC,yC,r,label='',color='black'):    
    crcl=plt.Circle((xC,yC),r,fill=False,color=color)
    self.axes.add_artist(crcl)
    #axes.add_patch(crcl)
    self.axes.annotate(label, xy=(xC+0.1, yC-r+0.1),color=color)
     
  def pltPolygonalLine(self,x,y,label,color='black'):
    n=len(x)
    for i in range(n-1):
        self.pltSegment(x[i],y[i],x[i+1],y[i+1],label[i],color=color)
        