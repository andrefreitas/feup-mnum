#include <iostream>
#include <math.h>
using namespace std;
double f1(double v){
	return -(14*(exp(2.1*v) -1)+v-13);
}
int main(){
	double a=-4.0;
	double b=4.0;
	double meio=(b+a)/2;
	double delta=0.001;
	double aux;
	cout << "----------------------------\n";

	do{
		// Debug Information
		cout << "a= " << a << '\n';
		cout << "b= " << b << '\n';
		cout << "f1(a)=" << f1(a) <<'\n';
		cout << "f1(b)=" << f1(b) << '\n';
		cout << "f1(meio)=" << f1(meio) << "\n\n\n";
		// Decisão dos novos limites
		if((f1(meio)>0 & f1(b) >0) || (f1(meio)<0 & f1(b) <0)){
			b=meio;
		}
		else {
			a=meio;	
		}
		meio=(b+a)/2;
		// Conversao da imagem do meio para positiva 
		// caso for negativa para a condicao de terminacao
		if (f1(meio) <0)
			aux=-1*f1(meio);
		else aux= f1(meio);

	} while (aux>delta);
	cout << "\na=" << a << " e b= " << b <<  " f(meio) " << f1(meio) << endl;
	return 0;
}