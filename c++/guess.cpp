#include <iostream>
using namespace std;

int main() {

int number = rand() % 100+1;
int guess = 0;
//srand (time(NULL));

do {
  cout << number << endl; //debug
  cout << "Guess a number between 1 and 100: ";
  cin >> guess;
  if ( guess > number) { cout << "Too high.\n" << endl; }
  else if ( guess < number ) { cout << "Too low.\n" << endl; }
  else {
    cout << "That's right!\n" << endl;
    exit(0);
        } // fi
 } 
while ( number != guess );
return 0;
	}
