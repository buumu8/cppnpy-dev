#include <iostream>
using namespace std;

int main()
{
    float quarters, dimes, nickels, pennies, dollars;
    cout << "Please enter the number of coins:" << endl;
    cout << "# of quarters: ";
    cin >> quarters;
    cout << "# of dimes: ";
    cin >> dimes;
    cout << "# of nickels: ";
    cin >> nickels;
    cout << "# of pennies: ";
    cin >> pennies;

    dollars = quarters / 4 + dimes / 10 + nickels / 20 + pennies / 100;
    cout << "The total is " << int(dollars) << " dollars and " << int((dollars - int(dollars)) * 100) << " cents" << endl;
    return 0;
}