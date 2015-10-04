#include <iostream>
#include <math.h>
#define debugmode 0
using namespace std;
double f(double x){
	return 14*(exp(2.1*x)-1)+ x -13;
}
int main(){
	// (1) Definir valores iniciais do intervalo
	double a,b, med; // a será o ponto fixo
	double m,c; // y=mx+c
	double erro, aux;
	erro=0.0001;
	a=0.306; b=1;
	// (2) Passo iterativo
	do{
		// (a) Determinar a expressão, y=mx+c
		m=(f(b)-f(a))/(b-a);
		c=f(a)-m*a;
		// (b) Determinar a raíz da recta: 0=mx+c <=> -c/m=x
		med=-c/m;
		// (c) Calcular o módulo da imagem da raíz da recta
		if (f(med)<0) aux=-1*f(med);
		else aux=f(med);
		// --->
			if (debugmode){
				cout << "-------------------------------------------\n";
				cout << "::: Calculos efectuados para a equacao da recta:::\n";
				cout << "c = f(a)-m*a = f("<<a<<")-"<<m<< " * " << a<<" = " << f(a) << " - " << m << " * " << a << " = " << c << endl; 
				cout << "\nEquacao da recta: y=" << m <<"x + " << c << endl;
				cout << "\nRaiz da recta: med= " << med << endl;
				cout << "\nValor estimado: " << f(med) << endl;
				cout << "a: " << a << endl;
				cout << "b: " << b << endl;
				cout << "-------------------------------------------\n\n";
				system("pause");
			}
	    // --->
		// WARNING: O passo do método é muito decisivo! Não enganar! //
		if (f(a)<f(b)) a=med;
		else b=med;
	}
	while(aux>erro);
	cout << "\n\nA raiz aproximada e de: " << med << "\n\n";
	return 0;
}