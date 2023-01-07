#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dgt = abs(number) % 10
if number < 0:
    dgt = -dgt
print("Last digit of {} is {}".format(number, dgt), end="")
if dgt == 0:
    print(" and is 0")
elif dgt > 5:
    print(" and is greater than 5")
else:
    print(" and is less than 6 and not 0")
