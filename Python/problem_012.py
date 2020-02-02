from util_euler import generate_triangular_numbers, InfinitePrimeGenerator, compute_prime_factorization
from functools import reduce


def solve(target_num_divisor=500):
    num_divisor = 0
    gen_triangular_numbers = generate_triangular_numbers()
    gen_prim_number = InfinitePrimeGenerator()
    while num_divisor <= target_num_divisor:
        triang_number = next(gen_triangular_numbers)
        prime_factorization = compute_prime_factorization(triang_number, gen_prim_number.restart_counter())
        num_divisor = reduce(lambda x, y: x * y, [el + 1 for _, el in prime_factorization.items()])
    return triang_number


result = solve(500)
print(result)
