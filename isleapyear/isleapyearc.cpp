// Write a program for determining if a year is a leap year.
// In the Gregorian calendar system you can check if it is a leaper if it is divisible by 4 but
// not by 100 unless it is also divisible by 400. For example, 1896, 1904, and 2000 were leap years but 1900 was not.

// Write a program that takes in a year as input (as a command line argument)
// and prints the string "{year} was a leap year'' if true and "{year} was not a leap year'' if false.

// Here is a possible example call to the program:

// .\isleapyearc 1896

// output:

// 1896 was a leap year

// Here is a negative example call to the program:

// .\isleapyearc 1897

// output:

// 1897 was not a leap year

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    if (argc > 1)
    {
        bool is_leap = false;

        int year = atoi(argv[1]);
        is_leap = (year % 4 == 0 && year % 100 != 0) || (year % 4 == 0 && year % 100 == 0 && year % 400 == 0);
        if (is_leap)
        {
            cout << year << " was a leap year";
        }
        else
        {
            cout << year << " was not a leap year";
        }
    }

    return 0;
}
