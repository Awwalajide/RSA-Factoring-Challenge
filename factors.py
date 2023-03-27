import sys
import math

def factorize(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return "{}={}*{}".format(num, i, num//i)
    return "{}={}*{}".format(num, num, 1)

filename = sys.argv[1]

with open(filename, 'r') as f:
    for line in f:
        num = int(line.strip())
        print(factorize(num))

