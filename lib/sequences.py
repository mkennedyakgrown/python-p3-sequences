#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fib = [0, 1]
        for i in range(1, length - 1):
            fib.append(fib[i] + fib[i - 1])
        print(fib)