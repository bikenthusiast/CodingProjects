#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <numeric>  
#include <functional>
#include <stdio.h>
#include <iomanip>
#include <fstream>

using namespace std;

double x[]={20,500,1000,1200,1400,1500},y[]={203,197,191,188,186,184},a_0,a_1;
const int sizeArray=6;
int i;
int squaredError[sizeArray];
double z[sizeArray],dif[sizeArray];
double err[]={};

double squareError(double* y,double* x){
    for (i=0;i<sizeArray;i++)
        err[i]=pow((x[i]-y[i]),2);
}
int main(){
for(i=0;i<sizeArray;i++){
    z[i]=203.3319-0.0126*x[i];}
squareError(y,z);
for (i=0;i<sizeArray;i++)
    cout << err[i]<<endl;
}