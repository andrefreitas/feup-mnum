# Diagonal Dominante: http://en.wikipedia.org/wiki/Diagonally_dominant_matrix
def diagonalDominante(matriz):
    for i in range(len(matriz)):
       soma=abs(sum(list(map(abs,matriz[i][:]))) - abs(matriz[i][i]))
       #print(i,": ",abs(matriz[i][i]), " >=", soma)
       if (abs(matriz[i][i])<=soma):
           return 0
    return 1
# Teste
exdd=[[5,-2,1],[1,-8,2],[-1,2,7]]
# print(diagonalDominante(exdd))


# Método de Gauss Seidel
# In this method we use the actual variables calculated
def gaussSeidel(matriz):
    print ("------------------ Gauss Seidel -------------------")
    x=[0]*len(matriz)
    def mul(x,y): return x*y
    continua=1
    while(continua):
        for i in range(len(matriz)):
            # Calcular x[i]
            soma= sum(list(map(mul,x,matriz[i][:len(matriz)]))) - matriz[i][i]*x[i]
            x[i]=(matriz[i][len(matriz)] - soma)/ matriz[i][i];
        # Calcular o resíduo
        continua=0
        for j in range(len(matriz)):
            residuo=abs ( sum(list(map(mul,x,matriz[j][:len(matriz)]))) - matriz[j][len(matriz)])
            print (x[j], " Residuo: ", residuo)
            if(residuo>0.01): continua=1
        print("---------------------------------------------------")
    return x

# Método de Gauss Jacoby, with one small change
# In this method we don't use the actual variables calculated
def gaussJacoby(matriz):
    print ("------------------ Gauss Jacoby -------------------")
    x=[0]*len(matriz)
    def mul(x,y): return x*y
    continua=1
    while(continua):
        import copy
        aux=copy.deepcopy(x)
        for i in range(len(matriz)):
            # Calcular x[i]
            soma= sum(list(map(mul,x,matriz[i][:len(matriz)]))) - matriz[i][i]*x[i]
            aux[i]=(matriz[i][len(matriz)] - soma)/ matriz[i][i];
        # Calcular o resíduo
        x=aux
        continua=0
        for j in range(len(matriz)):
            residuo=abs ( sum(list(map(mul,x,matriz[j][:len(matriz)]))) - matriz[j][len(matriz)])
            print (x[j], " Residuo: ", residuo)
            if(residuo>0.01): continua=1
        print("---------------------------------------------------")
    return x
    
exgs=[[7,2,0,24],[4,10,1,27],[5,-2,8,27]]
#gaussSeidel(exgs)
gaussJacoby(exgs)
