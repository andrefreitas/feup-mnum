# Um bom guess inicial é 3.5 e 2.3
def f1(x,y):
    return 2*x*x-x*y-5*x+1;
def f2(x,y):
    import math;
    return x+3*math.log(x,10)-y*y;

# Derivadas Numericas

def derivadaNumX(f,x,y):
    h=0.0001;
    return (f(x+h,y)-f(x,y))/h;

def derivadaNumY(f,x,y):
    h=0.0001;
    return (f(x,y+h)-f(x,y))/h;

# Determinante da Matriz Jacobiana
def det(m):
     return m[0][0]*m[1][1]-m[0][1]*m[1][0];
    
def Jacobiana(f1,f2,x,y):
    a=[[derivadaNumX(f1,x,y),derivadaNumY(f1,x,y)],[derivadaNumX(f2,x,y),derivadaNumY(f2,x,y)]];
    return a;

# Termos hn e kn
def hn(f1,f2,x,y,jacob):
    a=[[f1(x,y),derivadaNumY(f1,x,y)],[f2(x,y),derivadaNumY(f2,x,y)]];
    return -det(a)/det(jacob);

def kn(f1,f2,x,y,jacob):
    a=[[derivadaNumX(f1,x,y),f1(x,y)],[derivadaNumX(f2,x,y),f2(x,y)]];
    return -det(a)/det(jacob);
    
def sistemaNewton(f1,f2,x,y):
    while(abs(f1(x,y))>0.0001 and abs(f2(x,y))>0.0001):
        matrizJacobiana=Jacobiana(f1,f2,x,y);
        x=x+hn(f1,f2,x,y,matrizJacobiana);
        y=y+kn(f1,f2,x,y,matrizJacobiana);
    zeros=[];
    # Valores aproximados
    zeros.append(x);
    zeros.append(y);
    # Resíduos
    residuos=[];
    residuos.append(f1(x,y));
    residuos.append(f2(x,y));
    return [zeros,residuos];
