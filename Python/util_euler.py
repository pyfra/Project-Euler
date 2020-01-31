import math
from math import gcd

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
    elif n in (2,3):
        return True
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def is_palindrome(x):
    """
    check whether a string is palindrome
    :return: bool
    """
    return x == x[::-1]

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)
