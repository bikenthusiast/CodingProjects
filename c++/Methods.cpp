#include <string>
//1. Encapsulation

using namespace std;
class Employee{
    private:
    int Age;
    string Company;
    string Name;

    public:
    void setName(string name){
        Name=name;
    }
    string getName(){
        return Name;
    }
    Employee(string name, string company,int age){
        Name=name;
        Company=company;
        Age=age;
    }
    };
    
    int main(){
        Employee 

    }