# -*- coding: cp1252 -*-
# Método de Euler
def euler(f,a,b,h=0.0001):
    F=0
    while (a<=b):
        F=F+f(a)*h
        a=a+h
    return F
    
def testEuler():
    import math
    print euler(math.sin,0,1)
# Método de Runge Kutta
def rk2(f,xi,xf,yi,h=0.01):
    print xi," ", yi
    while(xi<xf):
        k1=h*f(xi,yi)
        k2=h*f(xi+h/2.0,yi+k1/2.0)
        yi=yi+k2
        xi=xi+h
        print xi," ", yi
    return [xi,yi]

def testRk():
    import math
    def f(x,y):
        return 2*x*(math.pow(y,2))
    def f2(x,y):
        return x**2+y**2
    rk2(f,1,3,1,0.1)

# Método de euler de segunda ordem
def euler2nd(f,xi,yi,y1i,passos,h=0.0001):
    # Condições Iniciais xi,yi,y1i
    # Ciclo para observar a evolução da equação
    fich=open("eulerData.csv",'w')
    for i in range(passos):
        stxi=str(xi)
        stxi=stxi.replace(".",",")
        styi=str(yi)
        styi=styi.replace(".",",")
        sty1i=str(y1i)
        sty1i=sty1i.replace(".",",")
        fich.write(stxi+';'+styi+';'+sty1i)
        fich.write('\n')
        print i,"-> ",xi,yi,y1i
        yaux=yi
        yi=yi+y1i*h
        y1i=y1i+f(xi,yaux,y1i)
        xi=xi+h
    return [xi,yi,y1i]

def testEuler2nd():
    def f1(x,y,y1): return 2*x**2*y+y1
    print euler2nd(f1,0,1,1,20)


# Método de Runge Kutta  4
def rk4(f,x,y,n,h=0.0001):
    for i in range(n):
        print x,y
        dy1=h*f(x,y)
        dy2=h*f(x+h/2.0,y+dy1/2.0)
        dy3=h*f(x+h/2.0,y+dy2/2.0)
        dy4=h*f(x+h,y+dy3)
        y=y+1/6.0*dy1+1/3.0*dy2+1/3.0*dy3+1/6.0*dy4
        x=x+h
    return [x,y]

def testRk4():
    import math
    def f(x,y):
        return 2*x*(math.pow(y,2))
    print rk4(f,0,0,10)

testRk4()
