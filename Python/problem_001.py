
def sum_multiple(m, treshold):
    """
    Returns the sum of the multiple of n until the treshold (not included)
    """
    n = (treshold - 1) // m
    return sum_arit(n) * m


def sum_arit(n):
    """
    It returns the arithmetic sum from 1 to n with n elements with n elements to be added.
    """
    return n*(n+1) >> 1  # better than actually dividing by 2 for very large n


result_2 = sum_multiple(3,1000) + sum_multiple(5,1000) - sum_multiple(3*5,1000)
result = sum((x for x in range(3,1000, 3))) + sum((x for x in range(5,1000, 5) if x % 3 != 0))

# assertation to make sure that the result is the same as before
assert (result_2 - result) == 0.0
print(result)
