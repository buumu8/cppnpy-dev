# Write a program that reads a character (string of  length 1) from the user,
# and classifies it to one of the following: lower case letter, upper case letter, digit, or non-alphanumeric character.

# Sample output (4 different executions):

# Enter a character: j
# j is  a lower case  letter.

# Enter a character: 7
# 7 is  a digit.

# Enter a character: ^
# ^ is  a non-alphanumeric  character.

# Enter a character: C
# C is  an  upper case  letter.

c = input("Enter a character: ")

ascii_number = ord(c)
if 65 <= ascii_number <= 90:
    print(f"{c} is  an  upper case  letter.")
elif 97 <= ascii_number <= 122:
    print(f"{c} is  a lower case  letter.")
elif 48 <= ascii_number <= 57:
    print(f"{c} is  a digit.")
else:
    print(f"{c} is  a non-alphanumeric  character.")
