// Counting Even and Odd Numbers Lab:

// Write a program that inputs four numbers separated by spaces. The program should count how many odd and even numbers there are. The program should then output one of three possibilities depending on how many even and odd numbers are entered:

// more evens
// more odds
// same number of evens and odds

// For example, an execution could look like this:

// Please enter 4 positive integers, separated by a space: 2 3 5 7

// more odds
#include <iostream>
using namespace std;

int main()
{
    int a, b, c, d, odd, even;
    odd = 0;
    even = 0;
    cout << "Please enter 4 positive integers, separated by a space: ";
    cin >> a >> b >> c >> d;

    if (a % 2 != 0)
    {
        odd = odd + 1;
    }
    else
    {
        even = even + 1;
    }
    if (b % 2 != 0)
    {
        odd = odd + 1;
    }
    else
    {
        even = even + 1;
    }
    if (c % 2 != 0)
    {
        odd = odd + 1;
    }
    else
    {
        even = even + 1;
    }
    if (d % 2 != 0)
    {
        odd = odd + 1;
    }
    else
    {
        even = even + 1;
    }
    if (even > odd)
    {
        cout << "more evens" << endl;
    }
    else if (odd > even)
    {
        cout << "more odds" << endl;
    }
    else
    {
        cout << "same number of evens and odds" << endl;
    }
    return 0;
}