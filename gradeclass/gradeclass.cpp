// Write a program that inputs two grades separated by a space.

// If both grades are below a score of sixty then the program should output the message:

// Student Failed:(

// If both grades are greater than or equal to ninety five then the program should output the message:

// Student Graduated with Honors:)

// Otherwise the program should output the message:

// Student Graduated!

// For example, an execution could look like this:

// Please enter 2 grades, separated by a space: 59 95

// Student Graduated!
#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cout << "Please enter 2 grades, separated by a space: ";
    cin >> a >> b;
    if (a < 60 && b < 60)
    {
        cout << "Student Failed:(" << endl;
    }
    else if (a >= 95 and b >= 95)
    {
        cout << "Student Graduated with Honors:)" << endl;
    }
    else
    {
        cout << "Student Graduated!" << endl;
    }
    return 0;
}