def is_pythagorean_triplet(a, b, c):
    return (a**2 + b**2) == c**2

def find_product_triplet(sum_to=1000):
    for a in range(1, sum_to//3):
        for b in range(a, (sum_to - 1)//2):
            c = 1000 - b - a
            if is_pythagorean_triplet(a, b, c):
                print("triplet is a: %d, b: %d, c: %d"%(a,b,c))
                return a * b * c
                
result = find_product_triplet(sum_to=1000)
print(result)
