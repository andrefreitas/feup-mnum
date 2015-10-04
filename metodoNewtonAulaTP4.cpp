#include <iostream>
#include <math.h>
#define DELTA 0.000000001
using namespace std;
double f(double x){
	return 14*(exp(2.1*x)-1)+ x -13;
}
int main(){
	double x=0.0;
	double derivada;
	double modulof;
	do{
		
		derivada=(f(x+DELTA)-f(x))/DELTA;
		x=x-f(x)/derivada;
		if(f(x)<0) modulof=-f(x);
		else modulof=f(x);
	}while(modulof>0.000001);
	cout << "A Raiz numerica e: " << x << endl;
}