#!/usr/bin/env python
# Author: Christopher Segale
# Date: 3/11/2013

def main():
    is_loop = True
    a = 1
    b = a

    while a < 1000 / 3 and is_loop:
        b = a
        while b < 1000 / 2 and is_loop:
            c = 1000 - a - b

            if ((a ** 2) + (b ** 2)) == (c ** 2):
                is_loop = False
                print a * b * c
                break
            b += 1
        a += 1

if __name__ == '__main__':
    main()
