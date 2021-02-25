from util_euler import is_prime


def sum_of_primes_below(n):
    sum_primes = 2
    for i in range(3, n, 2):
        if is_prime(i):
            sum_primes += i
    return sum_primes


result = sum_of_primes_below(2 * 10 ** 6)
sum_of_primes_below(2 * 10 ** 6)
print(result)
