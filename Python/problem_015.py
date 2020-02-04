from math import factorial


def binomial_coefficient(a, b):
    return factorial(a + b) / (factorial(a) * factorial(b))


print(int(binomial_coefficient(20, 20)))
