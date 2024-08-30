# Coin Converter Lab:

# Description

# Write a program that asks the user to enter an amount of money in the format of dollars and remaining cents.  The program should calculate and print the minimum number of coins (quarters, dimes, nickels and pennies) that are equivalent to the given amount.

# Hint: In order to find the minimum number of coins, first find the maximum number of quarters that fit in the given amount of money, then find the maximum number of dimes that fit in the remaining amount, and so on.


# File Name

# coins.py

# the coins are 9 quarters, 1 dimes, 1 nickels and 2 pennies 9/4 = 2.25 + 1/10 = 0.1 + 1/20 = 0.05 + 2/100 = 0.02 = 2.42

dollars = float(input(""))
cents = float(input(""))

cents = (100 * dollars) + cents

quarters, dimes, nickles, pennies = 0, 0, 0, 0

quarters = int(cents // 25)
cents -= quarters * 25

if cents > 0:
    dimes = int(cents // 10)
    cents -= dimes * 10

if cents > 0:
    nickles = int(cents // 5)
    cents -= nickles * 5

pennies = int(cents)

print(
    f"the coins are {quarters} quarters, {dimes} dimes, {nickles} nickels and {pennies} pennies"
)
