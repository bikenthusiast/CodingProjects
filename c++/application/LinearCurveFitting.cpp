//Least Squares Curve-Fitting
//Line: zi = a0 + a1*x, sum square error, coefficient of determination
//https://web.cecs.pdx.edu/~gerry/nmm/course/slides/ch09Slides.pdf

#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <numeric>  
#include <functional>
#include <stdio.h>
#include <iomanip>
#include <fstream>

using namespace std;

const int sizeArray=6;
double squaresum;
int initial_sum=0;
int i,sum;
double x[]={20,500,1000,1200,1400,1500},y[]={203,197,191,188,186,184},a_0,a_1;
int squaredError[sizeArray];
double z[sizeArray];
double err[]={},squaredErr[]={};


//Calculate square error
double squareError(double* y,double* x){
    for (i=0;i<sizeArray;i++)
        err[i]=pow(x[i]-y[i],2);
}

//Calculate sum of array
double arraySum(double a[],int sizeArray)  
{ 
    double initial_sum  = 0;  
    return accumulate(a, a+sizeArray, initial_sum); 
} 

int main(){

//Set precision of output data
cout.precision(4);

//Claculate necessary terms of slope and interception 
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

// Calculate z-values of line
for (i=0;i<sizeArray;i++)
    z[i]=a_1*x[i]+a_0;
cout <<"\nIntercept: a_0= "<< fixed << a_0;
cout <<"\nSlope: a_1= "<< fixed << a_1;

//Calculate Coefficient of Determination
sum=arraySum(y,sizeArray);
double y_mean=sum/sizeArray;

//Transform single value to array
double y_mean_arr[sizeArray]={ };
for (i=0;i<=sizeArray;i++)
    y_mean_arr[i]=y_mean;

squareError(y,y_mean_arr);
double meanErr=(arraySum(err,sizeArray));

squareError(y,z);
double fitErr=(arraySum(err,sizeArray));
double coeffDet=1.0-(fitErr/meanErr);

// Calculate SquareError
squareError(y,z);
for (i=0;i<sizeArray;i++)

squaresum=arraySum(err,sizeArray);

//Output to terminal
cout<<"\nSum of Squared Errors: "<< fixed <<squaresum << endl;
cout <<"Coefficient of Determination: "<< fixed << coeffDet<<"\n";
// Create and open a text file
ofstream MyFile("values.txt");
// Write to file
MyFile << "x y z squErr: \n";
for (i=0;i<sizeArray;i++)
    MyFile <<x[i]<<" "<<y[i]<<" "<<z[i]<<" "<< err[i] << endl;
// Close file
MyFile.close();

return 0;
}