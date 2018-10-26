from util_euler import is_palindrome

result = 0
for n in range(100, 1000):
    for m in range(100, 1000):
        temp = n*m
        if is_palindrome(str(temp)) and temp > result:
            result = temp


