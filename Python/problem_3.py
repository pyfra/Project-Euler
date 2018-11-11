from math import floor, sqrt
TARGET_NUMBER = 600851475143

def get_max_prime(num):
    #check whether it is divisible by 2, not needed for this problem as the number is clearly odd, but good for a general
    #case
    while num % 2 == 0:
        num //= 2
    if num == 1:
        return 1

    for x in range(3, floor(sqrt(num)) + 1, 2):
        while num % x == 0:
            num //= x
        if num == 1:
           return x
    else:
        return num

result = get_max_prime(TARGET_NUMBER)