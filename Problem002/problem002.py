#!/usr/bin/env python
# Author: Christopher C. Segale
# Date: 2/19/13

# deprecated
def fib_finder(f, s):
    if (f + s) % 2 == 0:
        return f + s
    else:
        return 0

def gen_fibs(limit):
    # Gotcha! Limit might overflow on 32bit platform!
    fib = [1, 2]
    first_term = 1
    second_term = 2
    current_term = first_term + second_term
    while current_term < limit:
        fib.append(current_term)
        first_term = second_term
        second_term = current_term
        current_term = first_term + second_term
    return fib

# deprecated
def is_even(n):
    return n % 2 == 0

def main():
    my_fib = gen_fibs(4000000)
    print my_fib

    fib_sum = sum([x for x in my_fib if x % 2 == 0])
    print fib_sum

if __name__ == '__main__':
    main()
