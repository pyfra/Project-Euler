from util_euler import is_palindrome

result = 0
for n in range(100, 1000):
    # we need to obtain a six digit number, and we avoid looping where this is not possible
    for m in range(100000//n + 1, 1000):
        temp = n*m
        if is_palindrome(str(temp)) and temp > result:
            result = temp

print(result)
