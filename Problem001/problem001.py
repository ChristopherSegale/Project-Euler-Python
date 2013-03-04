#!/usr/bin/env python
# Author: Christopher C. Segale
# Date: 2/17/13
 
def is_divisible_by(divisor, n):
    return not n % divisor
 
def main():
    sum = 0
    for index in range(1000):
        if is_divisible_by(3, index) or is_divisible_by(5, index):
            sum += index
    print sum
 
if __name__ == '__main__':
    main()
