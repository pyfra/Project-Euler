import math

def generator_fibonacci():
    """
    Returns a generator of Fibonacci Numbers
    """
    n_1 = n_2 = 1
    while True:
        n_1, n_2 = n_2, n_1 + n_2
        yield n_2

def is_prime(n):
    """
    Check primality for a given number
    :param n: the number to check
    :return: Boolean (if True, then n is a prime)
    """
    if n <= 1:
        return False
    elif n in (2,3) or n % 2 == 0:
        return True
    else:
        for i in range(3, math.floor(math.sqrt(n)), 2):
            if n % i == 0:
                return False
        return True