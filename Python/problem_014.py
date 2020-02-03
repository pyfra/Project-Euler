def next_collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


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
