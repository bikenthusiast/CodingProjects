#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <numeric>  
#include <functional>
#include <stdio.h>
#include <iomanip>
#include <fstream>

using namespace std;

double x[]={20,500,1000,1200,1400,1500},y[]={203,197,191,188,186,184};
const int sizeArray=sizeof(x)/sizeof(x[0]); //Calculate Array Size
double err[sizeArray];
double sum;
int i;

//Calculate squared difference
double squareDif(double* y,double* x){
    for (i=0;i<sizeArray;i++){
        return err[i]=pow(x[i]-y[i],2);
    }
        
}

//Calculate sum of array
double arraySum(double a[],int sizeArray)  
{ 
    double initial_sum  = 0;  
    return accumulate(a, a+sizeArray, initial_sum); 
} 
int main(){
    double difErr[sizeArray]={};
    difErr=squareDif(x,y);
    cout << difError;
}