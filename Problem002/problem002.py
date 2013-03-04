#!/usr/bin/env python
# Author: Christopher C. Segale
# Date: 2/19/13

def fib_finder(f, s):
    return f + s

def is_even(n):
    return not n % 2 == 0

def main():
    first_term = 1
    second_term = 2
    current_term = fib_finder(first_term, second_term)
    sum = second_term

    while current_term < 4000000:
        if is_even(current_term):
            sum += current_term

        first_term = second_term
        second_term = current_term
        current_term = fib_finder(first_term, second_term)

    print sum

if __name__ == '__main__':
    main()
