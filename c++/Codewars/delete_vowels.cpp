#include <iostream>

//Basic math operations
#include <cmath>
#include <string>
using namespace std;

bool is_square(int n)
{
    int d=sqrt(n);
    if (n == 0) 
                {return true;}

    else if (n<0)
                {return false;}

    else if ((n % d ) == 0;)
                {return true;}
return 0;
}

int main()
{
    cout << is_square(1) <<;
return 0;
}