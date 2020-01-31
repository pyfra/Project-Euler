# using numpy and recursion
import numpy as np

def compute_lcm(list_numbers,cum_lcm=1):
    if len(list_numbers)==1:
        return np.lcm(cum_lcm, list_numbers[0])
    return compute_lcm(list_numbers[1:], np.lcm(list_numbers[0], cum_lcm))

result = compute_lcm(list(range(1,20)))
print(result)
