def f1(v):
    import math
    return (14*(math.exp(2.1*v)-1)+v-13);

def f1G(v):
    import math
    return +14*(math.exp(2.1*v)-1)-13;

def f3(x):
    import math
    return math.log(x)+1;

# Função Sinal que é útil
def sinal(a,b):
    if((a<0 and b>0) or (a>0 and b<0)): return 0;
    else: return 1;
    
# (1) Método da bisseccção   
def bisseccao(funcao,a,b):
    import math;
    med=(a+b)/2;
    while(abs(funcao(med))>0.0001):
        if(sinal(funcao(med),funcao(a))):
            a=med;
        else:
            b=med;
        print("O valor medio é: ",med);
        med=(a+b)/2;
    return med;

# (2) Método da Corda
def corda(funcao,a,b):
    import math;
    zeroRecta=a;
    while(abs(funcao(zeroRecta))>0.0001):
        m=(funcao(b)-funcao(a))/(b-a);
        c=funcao(b)-m*b;
        zeroRecta=-c/m;
        a=zeroRecta;
    return zeroRecta;

#(3) Método de Newton
def newton(funcao,x):
    import math;
    while(abs(funcao(x))>0.0001):
        h=0.0001;
        derivadaNumerica=(funcao(x+h)-funcao(x))/h;
        x=x-funcao(x)/derivadaNumerica;
    return x;

#(4) Método de Picard-Peano f(x)=0 <=> g(x)-x=0; x=?
def picardPeano(funcaoG,x):
    h=0.0001;
    derivadaNumerica=(funcaoG(x+h)-funcaoG(x))/h;
    while(abs(derivadaNumerica)>1):
        x=funcaoG(x);
        derivadaNumerica=(funcaoG(x+h)-funcaoG(x))/h;
    return x;

def fPP(x):
    return (4*abs(x))/((1+x*x)*(1+x*x));
        
        
