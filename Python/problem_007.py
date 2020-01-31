from util_euler import is_prime

def infinite_number_generator(step=2):
    n = 0
    while True:
        n += step
        yield n

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
