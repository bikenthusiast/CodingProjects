#include <iostream>
using namespace std;

int digital_root(int n)
{
    int digitalRoot=0;
while(n>0){
    int m=n%10;
    digitalRoot=digitalRoot+m;
    n=n/10;
  }
  if(digitalRoot>9)
  int digitalTwin;
  {
    int digitalTwin=digitalRoot;
    while(digitalTwin>0){
    int j=digitalTwin%10;
    digitalRoot=digitalRoot+j;
    digitalTwin=digitalRoot/10;
    cout <<digitalTwin<<endl;
  }
  }
    
  return digitalRoot;
}
int main()
{
    cout <<digital_root(63)<< endl;
}