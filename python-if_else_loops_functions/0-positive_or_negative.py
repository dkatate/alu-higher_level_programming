#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = [random.randint(-10, 10)]
for num in number:
    if num > 0:
        print(f"{num} is positive")
    elif num == 0:
        print (f"{num} is zero")
    else:
        print(f"{num} is negative")
