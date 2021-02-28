def next_collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def simple_solution():
    number_max_sequence, len_max_sequence = 0, 0

    for i in range(1, 10 ** 6):
        number = i
        len_sequence = 0
        while number != 1:
            len_sequence += 1
            number = next_collatz(number)

        if len_sequence > len_max_sequence:
            len_max_sequence = len_sequence
            number_max_sequence = i

    print("longest sequence of %d for number %d" % (len_max_sequence, number_max_sequence))


# With memoization
def count_length_collatz(number, computed_values={}):
    if number in computed_values:
        return computed_values[number]

    len_sequence = 0
    number_next = number
    if number_next != 1:
        len_sequence += 1
        number_next = next_collatz(number_next)
        len_sequence += count_length_collatz(number_next, computed_values)
    computed_values[number] = len_sequence
    return len_sequence


def solution_memoization():
    computed_values = dict()
    len_max_sequence = 0
    for i in range(1, 10 ** 6):
        len_sequence = count_length_collatz(i, computed_values)
        if len_sequence > len_max_sequence:
            len_max_sequence = len_sequence
            number_max_sequence = i
    print("longest sequence of %d for number %d" % (len_max_sequence, number_max_sequence))


if __name__ == '__main__':
    import time

    t1 = time.perf_counter()
    simple_solution()
    t2 = time.perf_counter()
    print(f'time simple solution {t2 - t1}')

    t1 = time.perf_counter()
    solution_memoization()
    t2 = time.perf_counter()
    print(f'time solution memoization {t2 - t1}')
