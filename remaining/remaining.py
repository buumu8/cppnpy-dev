# Write a function that is given a phrase and returns the phrase we get if we take out the first word from the input phrase.
# For example, given ‘the quick brown fox’, your function should return ‘quick brown fox’.

# Here is an example call to the function:

# print(remainingwords(“the quick brown fox”)):


def remainingwords(phrase):
    return phrase[phrase.index(" ") + 1 :]


print(remainingwords("the quick brown fox"))
