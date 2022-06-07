import random

i=1
while True:
    x = random.randint(-1000000, 1000000)
    print(i, "\t", x, "\t", bin(x), "\t", oct(x), "\t", hex(x))
    i=i+1