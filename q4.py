import math


def log100(num):
    return math.log(num, 100)


def add_patch():
    math.log100 = log100

# Example case.
add_patch()
print(math.log100(10))
