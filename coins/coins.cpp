#include <iostream>
using namespace std;

int main()
{
    float quarters, dimes, nickels, pennies, dollars, cents;
    cout << "# of dollars: ";
    cin >> dollars;
    cout << "# of cents: ";
    cin >> cents;

    cents = (100 * dollars) + cents;

    quarters = int(cents / 25);
    cents -= quarters * 25;

    dimes = int(cents / 10);
    cents -= dimes * 10;

    nickels = int(cents / 5);
    cents -= nickels * 5;

    pennies = int(cents);

    cout << "the coins are " << int(quarters) << " quarters, " << dimes << " dimes, " << nickels << " nickels and " << pennies << " pennies" << endl;
    return 0;
}