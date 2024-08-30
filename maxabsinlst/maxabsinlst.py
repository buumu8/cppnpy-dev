# Implement function max_abs_val(lst),
# which returns the maximum absolute value of the elements in list.
# For example, given a list lst: [-19, -3, 20, -1, 0, -25],
# the function should return 25. The name of the method should be max_abs_val
# and the method should take one parameter which is the list of values to test.

# Here is an example call to the function:

# print(max_abs_val([-19, -3, 20, -1, 0, -25]))


def max_abs_val(lst):
    max = float("-inf")
    for l in lst:
        if abs(l) > max:
            max = abs(l)
    return max


# print(max_abs_val([-19, -3, 20, -1, 0, -25]))
