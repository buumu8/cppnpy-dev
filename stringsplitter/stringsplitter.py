# Read from the user a string containing
# odd number of characters. Your program should:

#    a) Print the middle character.
#    b) Print the string up to but not including the middle character (i.e., the first half of the string).
#    c) Print the string from the middle character to the end (not including the middle character).

# Sample output:

# Enter an odd length string: Fortune favors the bold
# Middle character: o
# First half: Fortune fav
# Second half: rs the bold

s = input("Enter an odd length string: ")
middle_pos = len(s) // 2
middle = s[middle_pos]
print(f"Middle character: {middle}")
print(f"First half: {s[0:middle_pos]}")
print(f"Second half: {s[middle_pos+1:]}")
