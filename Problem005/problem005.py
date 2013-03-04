#!/usr/bin/env python
# Author: Christopher Segale
# Date: 3/3/2013

def is_divisible_by(n, divisor):
    return not n % divisor

def is_inner_loop_running(smallest_multiple, divisor):
    if not is_divisible_by(smallest_multiple, divisor):
	return False
    else:
        return True

def smallest_multiple(low, high):
    smallest_multiple = 1
    is_loop = True

    while is_loop:
        for x in range(low, high + 1):
            is_loop_running = is_inner_loop_running(smallest_multiple, x)
            if not is_loop_running:
                smallest_multiple+= 1
                x = low
            elif is_loop_running and x == high:
                is_loop = False
            
    return smallest_multiple

def main():
    print smallest_multiple(1, 20)

if __name__ == '__main__':
    main()
