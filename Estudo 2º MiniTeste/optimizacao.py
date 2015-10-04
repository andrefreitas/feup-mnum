import math
f=lambda x: math.sin(x)
f2=lambda x:x**3-100*x

def unidimensional(f,a,h=0.01):
    encontrou=0
    while(not(encontrou)):
        f1=f(a)
        f2=f(a+h)
        if(f2>f1):
            h=h/2.0
            if(h<=0.000001): encontrou=1
        else:
            a=a+h
    return [a,f(a)]


print unidimensional(f,3)
print unidimensional(f2,0)

def 
