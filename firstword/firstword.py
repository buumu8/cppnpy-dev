# Write a function that is given a phrase and returns the first word in that phrase.
# For example, given ‘the quick brown fox’, your function should return ‘the’.

# Here is an example call to the function:

# print(firstword(“the quick brown fox”)):


def firstword(phrase):
    return phrase[0 : phrase.index(" ")]


# print(firstword("the quick brown fox"))
