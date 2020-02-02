from util_euler import is_prime, infinite_number_generator


def get_nth_prime(n):
    counter = 0
    inf_nums = infinite_number_generator(step=1)
    while counter < n:
        next_num = next(inf_nums)
        #print('testing num %d'%next_num)
        if is_prime(next_num):
            counter += 1
    return next_num

result = get_nth_prime(10001)
print(result)
