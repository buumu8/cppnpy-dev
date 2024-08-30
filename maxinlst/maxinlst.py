# Implement function max_val(lst),
# which returns the maximum value of the elements in list.
# For example, given a list lst: [-19, -3, 20, -1, 5, -25],
# the function should return 20.
# The name of the method should be max_val and the method should take one parameter which is the list of values to test.

# Here is an example call to the function:

# print(max_val([-19, -3, 20, -1, 5, -25]))


def max_val(lst):
    max = float("-inf")
    for l in lst:
        if l > max:
            max = l
    return max


# print(max_val([-19, -3, 20, -1, 5, -25]))
