#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst = number % 10

if lst > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lst))

elif lst == 0:
    print("Last digit of {} is {} and is 0".format(number, lst))

elif lst < 6 and lst != 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
                .format(number, lst))
