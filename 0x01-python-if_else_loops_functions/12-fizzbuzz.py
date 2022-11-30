#!/usr/bin/python3
"""Print the numbers from 1 to 100 seperated by a space.
  For multile of three, print Fizz instead of the number
  For multiles of five, print Buzz instead of the number
  For mulltiples of three and five, print FizzBuz insteead of the number.
  """


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
