def sum_digits_number(n):
    return sum([int(char) for char in str(n)])


print(sum_digits_number(2 ** 1000))
