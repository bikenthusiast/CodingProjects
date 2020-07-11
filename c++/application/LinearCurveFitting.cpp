//Linear Curve Fitting
//Input: zi = a0 + a1xi, min square error, coefficient of determination
//https://web.cecs.pdx.edu/~gerry/nmm/course/slides/ch09Slides.pdf

#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <numeric>  
#include <functional>
#include "gnuplot.h"
#include <stdio.h>
#include <iomanip>
//#include "matplotlibcpp.h"

using namespace std;
//namespace plt = matplotlibcpp;

const int sizeArray=6;
double squaresum;
int initial_sum=0;
int i,sum;
double x[]={20,500,1000,1200,1400,1500},y[]={203,197,191,188,186,184},a_0,a_1;
//,y_mean_arr[]={1,1,1,1,1}
int squaredError[sizeArray];
double z[sizeArray];
double err[]={};
//double* squaredError[];

double squareError(double* y,double* x){
    for (i=0;i<sizeArray;i++)
        err[i]=pow(x[i]-y[i],2);
}

double arraySum(double a[])  
{ 
    int initial_sum  = 0;  
    return accumulate(a, a+5, initial_sum); 
} 

int main(){
cout.precision(4);
//Manual Input x-values
//cout <<"Enter the x-axis values:";
//for (i=0;i<sizeArray;i++)
        //cin >> x[i];
//Manual Input y-values
//cout <<"Enter the y-axis values:";
//for (i=0;i<sizeArray;i++)
        //cin >> y[i];
//cout <<y[5];

double xsum=0,x2sum=0,ysum=0,xysum=0;
for (i=0;i<sizeArray;i++)
{
    xsum=xsum+x[i];
    ysum=ysum+y[i];
    x2sum=x2sum+pow(x[i],2);
    xysum=xysum+x[i]*y[i];
}
//Calculate slope
a_1=(sizeArray*xysum-xsum*ysum)/(sizeArray*x2sum-xsum*xsum);
//Calculate intercept              
a_0=(x2sum*ysum-xsum*xysum)/(x2sum*sizeArray-xsum*xsum);                    

// Calculate line
for (i=0;i<sizeArray;i++)
    z[i]=a_1*x[i]+a_0;
    //cout <<x[i];
    //cout <<z[i];
cout <<"\n Intercept: a_0= "<< fixed << a_0;
cout <<"\n Slope: a_1= "<< fixed << a_1;

// Calculate SquareError
squareError(y,z);

squaresum=arraySum(err);

//Calculate Coefficient of Determination
cout<<"\n Summe quadratischer Fehler: "<< fixed <<squaresum;
sum=arraySum(y);
double y_mean=sum/sizeArray;
//cout <<"\n Durchschnitt: "<<y_mean<<endl;

//transform value to array
double y_mean_arr[sizeArray]={ };
for (i=0;i<=sizeArray;i++)
    y_mean_arr[i]=y_mean;
//cout <<y_mean_arr[5];
squareError(y,y_mean_arr);
double meanErr=(arraySum(err));

squareError(y,z);
double fitErr=(arraySum(err));
double coeffDet=1-(fitErr/meanErr);

cout <<"\n Determinante: "<< fixed << coeffDet<<"\n";
//GnuplotPipe gp;
    //gp.sendLine("plot [-5:5] [-5:5] x,0.5*x");

// Graphical Output
// z-values
// data-points: x-y
//plt::plot({1,3,2,4});
    //plt::show();
return 0;
}