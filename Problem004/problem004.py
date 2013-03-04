#!/usr/bin/env python
# Author: Christopher Segale
# Date 3/3/2013

def is_palindrome(num):
    n = str(num)

    for x in range(0, len(n)):
        if n[x] != n[len(n) - 1 - x]:
	    return False

    return True
    
def main():
    palindrome = 0

    for product1 in range(100, 1000):
        for product2 in range(100, 1000):
            if is_palindrome(product1 * product2) and palindrome < product1 * product2:
                palindrome = product1 * product2

    print palindrome

if __name__ == '__main__':
    main()
