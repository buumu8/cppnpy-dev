# Coin Counter Lab:

# Description

# Write a program that asks the user to enter a number of quarters, dimes, nickels and pennies and then outputs the monetary value of the coins in the format of dollars and remaining cents. Your program should interact with the user exactly as it shows in the following example:


# Please enter the number of coins:
# of quarters: 20 / 4 = 5 dollars
# of dimes: 4 / 10 = 4 cents
# of nickels: 13 / 20 = 0.65 cents
# of pennies: 17 / 100 = 17 cents
# The total is 6 dollars and 22 cents

print("Please enter the number of coins:")
quarters = int(input("# of quarters: "))
dimes = int(input("# of dimes: "))
nickels = int(input("# of nickels: "))
pennies = int(input("# of pennies: "))

dollars = quarters / 4 + dimes / 10 + nickels / 20 + pennies / 100
# print(dollars)
if dollars / 10 > 0:
    print(
        f"The total is {int(dollars)} dollars and {int((dollars - int(dollars))*100)} cents "
    )
