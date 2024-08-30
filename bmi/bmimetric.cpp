#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int weight;
    float height;
    cout << "Please enter weight in kilograms: ";
    cin >> weight;
    cout << "Please enter height in meters: ";
    cin >> height;
    cout << "BMI is: " << ceil(weight / (height * height) * 100.0) / 100.0 << endl;
    return 0;
}