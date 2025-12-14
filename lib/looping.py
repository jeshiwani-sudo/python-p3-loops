#!/usr/bin/env python3
def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    square = [num * num for num in int_list]
    return square


def fizzbuzz():
    a = 1
    while a <= 100:
        if a % 3 == 0 and a % 5 == 0:
            print("FizzBuzz")
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else:
            print(a) 
        a += 1
