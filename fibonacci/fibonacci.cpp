#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int n;
    // n = atoi(argv[1]);
    cout << "Please enter a positive integer greater than 1: ";
    cin >> n;
    int n0 = 0;
    int n1 = 1;

    cout << n1 << endl;
    for (int i = 0; i < n - 1; i++)
    {
        int n2;
        n2 = n0 + n1;
        cout << n2 << endl;
        n0 = n1;
        n1 = n2;
    }

    return 0;
}