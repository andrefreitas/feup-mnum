#include <iostream>
#include <math.h>
#define DELTA 0.000000001
using namespace std;
double f(double x){
	return 14*(exp(2.1*x)-1)+ x -13;
}
double g(double x){
	return 14*(exp(2.1*x)-1)+ 2*x -13;
}
int main(){
	double x=0.0;
	double diferenca;
	double derivada;
	double moduloDerivada; 
	do{
		x=g(x);
		// Calcular Derivada
		derivada=(g(x+DELTA)-g(x))/DELTA;
		if (derivada<0) moduloDerivada=-derivada;
		else moduloDerivada=derivada;
		
	}while(moduloDerivada<=1);
	cout << "A Raiz numerica e: " << x << endl;
}