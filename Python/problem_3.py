from util_euler import is_prime

"""
Slow solution

TARGET_NUMBER = 600851475143
primes = filter(lambda x: is_prime(x) and TARGET_NUMBER % x == 0, range(3, TARGET_NUMBER, 2))
result = max(primes)
print(result)

"""

#Faster solution, dividing every time by the first prime we find, drasticalle reduce the search space
TARGET_NUMBER = 600851475143
def get_max_prime(num):
    for x in range(3, num + 1, 2):
        if is_prime(x) and num % x == 0:
            num //= x
            if num == 1:
                return x
            else:
                return get_max_prime(num)

result = get_max_prime(TARGET_NUMBER)