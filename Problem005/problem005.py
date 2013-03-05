#!/usr/bin/env python
# Author: Christopher Segale
# Date: 3/3/2013

def is_divisible_by(n, divisor):
    return n % divisor == 0

def smallest_multiple(low, high):
    smallest_multiple = 1
    is_loop = True
    divisor = low

    while is_loop:
        while divisor < high + 1:
            if not is_divisible_by(smallest_multiple, divisor):
                divisor = low
		smallest_multiple += 1
            elif is_divisible_by(smallest_multiple, divisor):
                is_loop = False
            divisor += 1

    return smallest_multiple

# Gives solution, but takes really long to compute it
def main():
    print smallest_multiple(1, 20)

if __name__ == '__main__':
    main()
