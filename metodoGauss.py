# -*- coding: cp1252 -*-
# André Freitas
mt=[[800,5,10,-5,3,835],[1,5,10,-5,500,2511],[0.1,0.5,1,-0.5,47,49.1],[1,10,5,1,2,50],[2,20,10,-600,4,-2308]];
simples=[[1,2,1,4],[3,8,7,20],[2,7,9,23]];
# http://www.leandroengenharia.com.br/materias/algebralinear/Aula_04_AlgLinear.pdf

def gauss(matriz):
    pivot=[0,0];
    soma1=lambda x :x+1;
    def divide(x,y): return x/y;
    def subtrai(x,y):return x-y;
    # For each pivot
    for total in range(len(matriz)):
        escalarPivot=matriz[pivot[0]][pivot[1]];
       # print("Pivot: ",escalarPivot);
        # Solve when pivots are zero!
        if(escalarPivot==0 and (total+1)<len(matriz)):
            # Exchange rows!
            aux=matriz[total][:];
            matriz[total][:]=matriz[total+1][:];
            matriz[total+1][:]=aux;
            escalarPivot=matriz[pivot[0]][pivot[1]];
        # For each line
        for i in range(total+1,len(matriz)):
            escala=matriz[i][total]/escalarPivot;
            multiplica=lambda x:x*escala;
            matriz[i][total:]=list(map(subtrai,matriz[i][total:],list(map(multiplica,matriz[pivot[0]][total:]))));
        pivot=list(map(soma1,pivot));
    return matriz;

def mostraMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i][:]);        

def solucoes(matriz):
    if(impossivel(matriz)):
        return "Impossível!";
    matriz=gauss(matriz);
    variaveis=[0];
    variaveis=variaveis*len(matriz);
    subtrai1=lambda x:x-1;
    def multiplica(x,y): return x*y;
    # Used for index
    i=len(matriz)-1;
    while(i>=0):
        # First
        variaveis[i]=matriz[i][len(matriz)];
        # Use vars 
        preVars=matriz[i][i+1:len(matriz)]
        if(len(preVars)>0):
            aux=[0]*(len(matriz)-len(preVars));
            aux=aux+preVars;
            aux=list(map(multiplica,variaveis,aux));
            variaveis[i]=variaveis[i]-sum(aux);
        # Third
        variaveis[i]=variaveis[i]/matriz[i][i];
        i=i-1;
    return variaveis;

# Verifica se o sistema é impossível
def impossivel(matriz):
    matriz=gauss(matriz);
    for i in range(len(matriz)):
        if(sum(list(map(abs,matriz[i][:])))==0):
            return 1;
    return 0;
ex1=[[7,8,9,24],[8,9,10,27],[9,10,8,27]];
# Estabilidade Externa
def estExt(matriz,erro):
    # (1) Determinar o vector X das soluções
    import copy
    aux=copy.deepcopy(matriz);
    x=solucoes(aux); # IF aux is a copy of matrix, why the matrix is changed??
    # (2) Calcular o vector da.X
    daX=[sum(x)*erro]*len(x);
    # (3) Calcular db-da.X
    db=[erro]*len(x);
    def subtrai(x,y):return x-y;
    coluna=list(map(subtrai,db,daX));
    # (4) Alterar a matriz
    for i in range(len(matriz)):
        matriz[i][len(matriz)]=coluna[i];
    return solucoes(matriz);

ex2=[[7,8,9,24],[8,9,10,27],[9,10,8,27]];
print(estExt(ex2,0.5))
    

        
        
