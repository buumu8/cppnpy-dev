# Fibonacci number is a series of numbers in which each number is the sum of the two preceding numbers.
# The first two numbers in the series are the number 1. Write a program to print first n Fibonacci Numbers.

# For example, one execution would look like this:

# Please enter a positive integer greater than 1: 4
# 1
# 1
# 2
# 3

n = int(input("Please enter a positive integer greater than 1: "))
n0 = 0
n1 = 1

print(n1)
for i in range(n - 1):
    n2 = n0 + n1
    print(n2)
    n0 = n1
    n1 = n2
