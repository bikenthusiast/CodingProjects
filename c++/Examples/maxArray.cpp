#include <iostream>
using namespace std;
#include <algorithm>
# include <cmath>
int tryout[5]={10,34,3,4,56};
int num_elements;


//Find maximum value in array
double maxArray(int array[], int num_elements)
{
    return *max_element(array,array+num_elements);
}

int main()
{
    //TODO: implement this into function
    num_elements=(sizeof(tryout) / sizeof(tryout[0]));
    cout <<"Max. value is: " <<maxArray(tryout,num_elements)<< endl;
    cout <<"Number of elements is: " <<num_elements;
    return 0;
}