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
    elif n in (2, 3):
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


def generate_triangular_numbers():
    n = 0
    last_num = 0
    while True:
        n += 1
        last_num += n
        yield last_num


def infinite_number_generator(start=0, step=2):
    while True:
        start += step
        yield start


class InfinitePrimeGenerator:

    def __init__(self):
        self._primes = [2, 3, 5, 7]
        self._counter = -1

    def restart_counter(self):
        self._counter = -1
        return self

    def __next__(self):
        gen_numbers = infinite_number_generator(self._primes[-1], step=2)
        while True:
            self._counter += 1
            if self._counter + 1 > len(self._primes):
                next_num = next(gen_numbers)
                while not (is_prime(next_num)):
                    next_num = next(gen_numbers)
                self._primes.append(next_num)
                return (next_num)
            else:
                return self._primes[self._counter]


def compute_prime_factorization(n, prime_numbers_generator):
    primes = dict()
    if n == 1: return {1: 1}
    while n != 1:
        prime_number = next(prime_numbers_generator)
        while (n % prime_number) == 0:
            n //= prime_number
            primes[prime_number] = 1 + primes.get(prime_number, 0)
    return primes
