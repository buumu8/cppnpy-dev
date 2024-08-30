#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int weight;
    float height;
    cin >> weight;
    cin >> height;
    cout << "bmi is: " << round(weight * 0.453592 / pow(height * 0.0254, 2) * 100.0) / 100.0 << endl;
    return 0;
}