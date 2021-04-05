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

double x[]={20,500,1000,1200,1400,1500},y[]={203,197,191,188,186,184};
//Calc Array Size
const int arrSize=sizeof(x)/sizeof(x[0]);
int squaredDif[arrSize];
double z[arrSize];
double err[arrSize]={},squaredErr[arrSize]={},erryz[arrSize]={};
double squaresum,a_0,a_1;
int initial_sum=0,i,sum;

//Calculate squared difference
double squareDif(double* y,double* x){
    for (i=0;i<arrSize;i++)
        err[i]=pow(x[i]-y[i],2);
}

//Calculate sum of array
double arraySum(double a[],int arrSize)  
{ 
    double initial_sum  = 0;  
    return accumulate(a, a+arrSize, initial_sum); 
} 

int main(){

//Calculate necessary terms of slope and interception 
double xsum=0,x2sum=0,ysum=0,xysum=0;
for (i=0;i<arrSize;i++)
{
    xsum=xsum+x[i];
    ysum=ysum+y[i];
    x2sum=x2sum+pow(x[i],2);
    xysum=xysum+x[i]*y[i];
}
//Calculate slope
a_1=(arrSize*xysum-xsum*ysum)/(arrSize*x2sum-xsum*xsum);
//Calculate interception              
a_0=(x2sum*ysum-xsum*xysum)/(x2sum*arrSize-xsum*xsum);                    
//Output
cout.precision(4);
cout <<"\nIntercept: a_0= "<< fixed << a_0;
cout <<"\nSlope: a_1= "<< fixed << a_1<<endl;

// Calculate z-values of line
for (i=0;i<arrSize;i++)
    z[i]=a_1*x[i]+a_0;
    //cout << z[i];

//Calculate Coefficient of Determination
sum=arraySum(y,arrSize);
double y_mean=sum/arrSize;

//Transform single value to array
double y_mean_arr[arrSize]={ };
for (i=0;i<=arrSize;i++)
    y_mean_arr[i]=y_mean;

squareDif(y,y_mean_arr);
double meanErr=(arraySum(err,arrSize));

squareDif(y,z);
double fitErr=(arraySum(err,arrSize));
double coeffDet=1.0-(fitErr/meanErr);

// Calculate SquareError
squareDif(y,z);
for (i=0;i<arrSize;i++)
    //cout << err[i] << endl;
squaresum=arraySum(err,arrSize);

//Output to terminal
cout << pow(y[3]-z[3],2)<<endl;
cout<<"\nSum of Squared Errors: "<< fixed <<squaresum << endl;
cout <<"Coefficient of Determination: "<< fixed << coeffDet<<"\n";

// Create and open a text file
ofstream MyFile("values.txt");
// Write to file
MyFile << "x y z squErr: \n";
for (i=0;i<arrSize;i++)
    MyFile <<x[i]<<" "<<y[i]<<" "<<z[i]<<" "<< err[i] << endl;
// Close file
MyFile.close();

return 0;
}