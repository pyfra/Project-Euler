import os
from problem_018 import solution

with open(os.path.join(os.getcwd(), '../files/p067_triangle.txt')) as f:
    # All the numbers in the file
    numbers = f.read()

print(solution(numbers))
