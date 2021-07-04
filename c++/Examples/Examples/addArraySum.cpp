#include<iostream>
using namespace std;

int get_sumArray(){
    int arr[] = {2, 4, 5, 9};
    int sum = 0;
    for (int i=0; i < 4;i++){
           sum+=arr[i];
       }
return sum;
}

int main(){
get_sumArray()
}