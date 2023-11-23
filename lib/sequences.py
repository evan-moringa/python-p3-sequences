#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []

    for i in range(length):
        if i == 0:
            fib_sequence.append(0)
        elif i == 1:
            fib_sequence.append(1)
        else:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print(fib_sequence)


print_fibonacci(9)

