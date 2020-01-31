def sum_of_squares(n):
    return n*(n+1)*(2*n+1)//6

def squared_sum(n):
    return (n * (n + 1) // 2)**2

def diff_sums(n):
    return squared_sum(n) - sum_of_squares(n)

n = 100
print(diff_sums(n))
