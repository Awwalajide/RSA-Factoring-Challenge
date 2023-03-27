import sys
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def factorize(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0 and is_prime(i) and is_prime(num//i):
            return "{}={}*{}".format(num, i, num//i)
    return "{}={}*{}".format(num, num, 1)

filename = sys.argv[1]

with open(filename, 'r') as f:
    num = int(f.readline().strip())
    print(factorize(num))

