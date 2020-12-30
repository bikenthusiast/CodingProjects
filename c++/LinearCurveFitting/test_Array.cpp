#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <numeric>  
#include <functional>
#include <stdio.h>
#include <iomanip>
#include <fstream>

using namespace std;

double x[]={20,500,1000,1200,1400,1500},y[]={21,510,1006,1203,1405,1502};
const int sizeArray=sizeof(x)/sizeof(x[0]); //Calculate Array Size
double err[sizeArray];
double sum;
int i;
double arr[sizeArray]={};

//Calculate squared difference
double* squareDif(double* y,double* x){
    for (i=0;i<sizeArray;i++){
        double* arr = new double[sizeArray];
        arr[i]=pow(x[i]-y[i],2);
        return arr;
    }
        
}

//Calculate sum of array
double arraySum(double a[sizeArray],int sizeArray)  
{ 
    double initial_sum  = 0;  
    return accumulate(a, a+sizeArray, initial_sum); 
}

int main()
{
    double* ptr=squareDif(y,x);
    //ptr=x;
    for (i=0;i<sizeArray;i++)
        cout << ptr[i]<< endl;

}