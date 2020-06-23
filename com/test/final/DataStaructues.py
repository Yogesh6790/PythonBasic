#  1) tuple - you cannot change it
my_tuple = 1,2,3
print(len(my_tuple))
print(my_tuple[1])

def calculate_product(*args):
    product = 1
    for val in args:
        product *= val
    return product

print(calculate_product(*range(1,6,2)))


c = [22, 33, 44]

print(c[-3])

numbers = list(range(1,16))
print(numbers)
