from util_euler import generator_fibonacci

gen_fibonacci = generator_fibonacci()
n_seq = 0
result = 0
while n_seq <= 4 * 10**6:
    n_seq = next(gen_fibonacci)
    if n_seq % 2 == 0:
        result += n_seq

