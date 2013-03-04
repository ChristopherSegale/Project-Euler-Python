#!/usr/bin/env python
# Author: Christopher C. Segale
# Date: 2/19/13
# Incomplete

def is_divisible_by(divisor, n):
    return not n % divisor

def is_prime(n):
    index = 1

    while index < n / 2:
        if is_divisible_by(index, n) and index != 1:
            return False

        index += 1

    return True

def main():
    largest_prime_factor = 0
    index = 1

    while index / 2 < 600851475143:
        if is_prime(index):
            prime_factor = index

        index += 1

    print prime_factor

if __name__ == '__main__':
    main()
