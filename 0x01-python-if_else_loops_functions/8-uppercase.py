#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and orrd(i) <= 122:
            i = hr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
