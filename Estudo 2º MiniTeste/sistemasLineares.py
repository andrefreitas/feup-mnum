# Determinante de uma Matriz, usando recursividade
def det(m):
    # Caso seja uma matriz 2x2 o determinante e imediato
    if (len(m)==2): return m[0][0]*m[1][1]-m[1][0]*m[0][1]
    soma=0
    import math
    for i in range(len(m)):
        # (1) Determinar a submatriz
        submatriz=[]
        for j in range(len(m)):
            if(i!=j): submatriz.append(m[j][1:])
        # (2) Efectuar a soma 
        soma=soma+math.pow(-1,i%2)*m[i][0]*det(submatriz)
    return soma

# Metodo de eliminacao de gauss
def eliminacaoGauss(matriz):
    import copy
    m=copy.deepcopy(matriz)
    if (det(m)==0): return "Sem Solucao!"
    # (1) Para cada pivot
    for i in range(len(m)):
        pivot=m[i][i]
        # a) Se o pivot for 0 tem-se que trocar as linhas
        if(pivot==0 and (i+1)<len(m)):
            aux=m[i]
            m[i]=m[i+1]
            m[i+1]=aux
            pivot=m[i][i]
        # b) Dividir a linha por sim mesma para o pivot ser 1
        dividir=lambda(x): x/pivot
        def subtrair(x,y):return x-y
        m[i]=map(dividir,m[i])
        # c) Subtrair as outras linhas pela linha do pivot
        for j in range(i+1,len(m)):
            multiplica=lambda(x):x*m[j][i]
            m[j]=map(subtrair,m[j],map(multiplica,m[i]))
    return m

# Determina uma solução de uma matriz triangular com diagonal =0
def solucaoGauss(m):
    m=eliminacaoGauss(m)
    x=[0]*len(m)
    i=len(m)-1
    def multiplica(x,y): return x*y;
    while(i>=0):
        x[i]=m[i][i]
        x[i]=m[i][len(m)] + m[i][i] - sum(map(multiplica,x,m[i][:len(m)]))
        i=i-1
    return x

def testeGauss():
    simples=[[1,2,1,4],[3,8,7,20],[2,7,9,23]]
    print solucaoGauss(simples)

# Estabilidade Externa
def estabilidadeExterna(m,db=0.5,da=0.5):
    import copy
    matriz=copy.deepcopy(m)
    # (1) Obter o vector de solucoes
    x=solucaoGauss(matriz)
    # (2) Fazer o dot entre dA e x
    daX=[sum(x)*da]*len(m)
    # (3) Substrair db -dA.X
    def subtrair(x,y): return x-y
    sub=map(subtrair,[db]*len(m),daX)
    # (4) Associar a uma matriz erro
    for i in range(len(m)):
        m[i][len(m)]=sub[i]
    # (5) Devolver as solucoes de gauss
    return solucaoGauss(m)

def testeErros():
    m=[[7,8,9,24],[8,9,10,27],[9,10,8,27]]
    print estabilidadeExterna(m)

# Metodo iterativo de Gauss-Seidel
def gaussSeidel(m):
    # Guess Inicial
    x=[0]*len(m)
    continua=1
    def multiplica(x,y): return x*y
    while(continua):
        # Descobre solucao
        for i in range(len(m)):
            soma=sum(map(multiplica,x,m[i][:len(m)]))-m[i][i]*x[i]
            x[i]=(m[i][len(m)]-soma)/(m[i][i]*1.0)
        # Calcula residuo
        continua=0
        for i in range(len(m)):
            res=abs(sum(map(multiplica,x,m[i][:len(m)]))-m[i][len(m)])
            print "x",i, "= ",x[i], " Residuo: ", res
            if (res>0.01): continua=1
        print "---------------------------------------------------"
    return x

def testeSeidel():
    exgs=[[7,2,0,24],[4,10,1,27],[5,-2,8,27]]
    print gaussSeidel(exgs)
    
# Metodo iterativo de Gauss-Jacoby
def gaussJacoby(m):
    # Guess Inicial
    x=[0]*len(m)
    continua=1
    def multiplica(x,y): return x*y
    while(continua):
        # Descobre solucao
        aux=[0]*len(m)
        for i in range(len(m)):
            soma=sum(map(multiplica,x,m[i][:len(m)]))-m[i][i]*x[i]
            aux[i]=(m[i][len(m)]-soma)/(m[i][i]*1.0)
        x=aux
        # Calcula residuo
        continua=0
        for i in range(len(m)):
            res=abs(sum(map(multiplica,x,m[i][:len(m)]))-m[i][len(m)])
            print "x",i, "= ",x[i], " Residuo: ", res
            if (res>0.01): continua=1
        print "---------------------------------------------------"
    return x

def testeJacoby():
    exgs=[[7,2,0,24],[4,10,1,27],[5,-2,8,27]]
    print gaussJacoby(exgs)    


