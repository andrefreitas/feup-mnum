# Usando o método dos trapézios
def trapezios(f,a,b,h=0.001):
    soma=f(a)
    while (a<(b-h)):
        soma=soma+2*f(a)
        a=a+h
    soma=soma+f(b)
    soma=(soma*h)/2.0
    return soma;

# Usando o método de simpson
def simpson(f,a,b,h=0.001):
    soma=f(a)
    coef=2
    while (a<(b-h)):
        if(coef==2):
            coef =4
        else:
            coef=2
        soma=soma+coef*f(a)
        a=a+h
    soma=soma+f(b)
    soma=(soma*h)/3.0
    return soma;
 
# Cociente de convergência para estimar erro
def erroTrapezio(f,a,b):
    s=[0]*3
    import math
    h=abs(b-a)
    for i in range(3):
        h=h/math.pow(2,i)
        print "h/", math.pow(2,i)
        s[i]=trapezios(f,a,b,h)
    co=(s[1]-s[0])/(s[2]-s[1])
    return co
            
        
# Funçõees de Teste
def g(x):
    import math
    return 1/(1-math.sin(x))

def h(x):
    return 2*x

print trapezios(g,0,0.5)
print simpson(g,0,0.5)
print (erroTrapezio(g,0,0.5))
