
#include <iostream>
#include <cmath>
#include <numeric> 
using namespace std; 

double x[]={20,500,1000,1200,1400,1500},y[]={21,510,1006,1203,1405,1502},z[]={23,540,1056,1243,1408,1508};
int i;
const int sizeArray=sizeof(x)/sizeof(x[0]); //Calculate Array Size
double err[sizeArray]={};


double* squareDif(double* x,double* y) 
{ 
    double* ptr = new double[sizeArray]; 
    for (i=0;i<sizeArray;i++)
    {
        err[i] = pow(x[i]-y[i],2);
        ptr=err;
    }
    return ptr;
}

//Calculate sum of array
double arraySum(double a[],int sizeArray)  
{ 
    double initial_sum  = 0;  
    return accumulate(a, a+sizeArray, initial_sum); 
} 

int main() 
{
cout << "xy" <<endl;
double* ptrxy;
ptrxy= squareDif(x,y);
for (i=0;i<sizeArray;i++){
cout << (ptrxy)[i] <<endl;
}
double sumxy;
sumxy=arraySum(ptrxy,sizeArray);
cout << "xy-sum" <<endl;
cout << sumxy <<endl;

cout << "xz" <<endl;
double* ptrxz;
ptrxz=squareDif(x,z);
for (i=0;i<sizeArray;i++){
cout << ptrxz[i] <<endl;
}
double sumxz;
sumxz=arraySum(ptrxz,sizeArray);
cout << "xz-sum" <<endl;
cout << sumxz <<endl;

cout << "yz" <<endl;
double* ptryz;
ptryz=squareDif(y,z);
for (i=0;i<sizeArray;i++){
cout << ptryz[i] <<endl;
}
double sumyz;
sumyz=arraySum(ptryz,sizeArray);
cout << "yz-sum" <<endl;
cout << sumyz <<endl;
return 0; 
} 
