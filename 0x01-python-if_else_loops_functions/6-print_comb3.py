#!/usr/bin/python3
# 6-print_comb3.py
for digit in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, dight2))
        else:
            print("{}{}".format(dight1, dight2), end=",")
