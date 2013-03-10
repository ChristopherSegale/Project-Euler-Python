#!/usr/bin/env python
# Author: Christopher Segale
# Date: 3/4/2013

def is_prime(n):
    index = 1

    while index < n:
        if n % index == 0 and index != 1:
            return False
        index += 1

    return True

def find_prime(n):
    number = 1
    prime_number = 2

    while number < n + 1:
        if is_prime(prime_number):
            number += 1
        if number < n + 1:
            prime_number += 1

    return prime_number

def main():
    print find_prime(10001) # takes too long to reach solution

if __name__ == '__main__':
    main()
