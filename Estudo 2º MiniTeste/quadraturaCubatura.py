# -*- coding: cp1252 -*-
#  Método dos trapézios
def intTrapezios(f,a,b,h=0.0001):
    soma=f(a)+f(b)
    a=a+h
    while(a<(b-h)):
        soma=soma+2*f(a)
        a=a+h
    soma=(soma*h)/2.0
    return soma

# Coeciente de Convergência   
def erroTrapezio(f,a,b,h):
    s=intTrapezios(f,a,b,h)
    s1=intTrapezios(f,a,b,h/2.0)
    s2=intTrapezios(f,a,b,h/4.0)
    return (s1-s)/(s2-s1)

def testTrapezios():
   import math
   def g(x): return 1/(1-math.sin(x))
   print "S: ",intTrapezios(math.sin,0,math.pi/2.0)
   h=1.963495e-2
   print "Cociente de Convergência:", erroTrapezio(math.sin,0,math.pi/2.0,h)
   

# Método de Simpson
def intSimpson(f,a,b,h=0.0001):
    soma=f(a)+f(b)
    a=a+h
    i=0
    while(a<(b-h)):
        if((i%2)==0): soma=soma+4*f(a)
        else: soma=soma+2*f(a)
        a=a+h
        i=i+1
    soma=(soma*h)/3.0
    return soma

def erroSimpson(f,a,b,h):
    s=intSimpson(f,a,b,h)
    s1=intSimpson(f,a,b,h/2.0)
    s2=intSimpson(f,a,b,h/4.0)
    return (s1-s)/(s2-s1)

def testSimpson():
   import math
   def g(x): return 1/(1-math.sin(x))
   print "S: ",intSimpson(math.sin,0,math.pi/2.0)
   h=1.963495e-2
   print "Cociente de Convergência:", erroSimpson(math.sin,0,math.pi/2.0,h)

# Quadratura usando a Regra de Simpson (muito lento e pouco preciso)
def intDuploSimpson1(f,xi,xf,yi,yf,h=0.0001):
    somaTotal=0
    # Função que será muito útil
    def intSimpsony(f,x,yi,yf,h=0.0001):
        soma=f(x,yi)+f(x,yf)
        i=0
        yi=yi+h
        while(yi<(yf-h)):
            if((i%2)==0): soma=soma+4*f(x,yi)
            else: soma=soma+2*f(x,yi)
            yi=yi+h
            i=i+1
        return (soma*h)/3.0
    somaTotal=intSimpsony(f,xi,yi,yf)+intSimpsony(f,xf,yi,yf)
    # Soma de Simpson
    xi=xi+h
    i=0
    while(xi<(xf-h)):
         if((i%2)==0): somaTotal=somaTotal+4*intSimpsony(f,xi,yi,yf)
         else: somaTotal=somaTotal+2*intSimpsony(f,xi,yi,yf)
         xi=xi+h
         i=i+1
    return (somaTotal*h)/3.0

def testDuplo():
    import math
    def f1(x,y): return x**2+y**2
    print intDuploSimpson1(f1,0,0.05,0,0.05)
    
# Regra de Simpson com Recursividade = Super Eficiência
def intDuploSimpson(f,xi,xf,yi,yf,p=2):
    hx=(xf-xi)/2.0
    hy=(yf-yi)/2.0
    #p= profundidade
    if (p==1):
        soma0=f(xi,yi)+f(xi,yf)+f(xf,yi)+f(xf,yf)
        soma1=4*(f(xi,yi+hy)+f(xi+hx,yi)+f(xf,yi+hy)+f(xi+hx,yf))
        soma2=16*f(xi+hx,yi+hy)
        return (hx*hy)/9.0*(soma0+soma1+soma2)
    soma= intDuploSimpson(f,xi,xi+hx,yi,yi+hy,p-1)
    soma=soma+intDuploSimpson(f,xi+hx,xf,yi,yi+hy,p-1)
    soma= soma+ intDuploSimpson(f,xi,xi+hx,yi+hy,yf,p-1)
    soma=soma+intDuploSimpson(f,xi+hx,xf,yi+hy,yf,p-1)
    return soma

def testDuploFinal():
    import math
    def f1(x,y): return x**2+y**2
    print intDuploSimpson(f1,0,1,0,1)
    
testDuploFinal()
