#!/usr/bin/env python
# Author: Christopher Segale
# Date: 3/4/2013

def square_sum(num_list):
    return sum(num_list) ** 2

def sum_square(num_list):
    total = 0

    for index in range(0, len(num_list)):
        total += num_list[index] ** 2

    return total

def main():
    my_list = []
    square_of_sum = 0
    sum_of_squares = 0
    difference = 0

    for x in range(1, 101):
        my_list.append(x)

    square_of_sum = square_sum(my_list)
    sum_of_squares = sum_square(my_list)
    difference = square_of_sum - sum_of_squares

    print difference

if __name__ == '__main__':
    main()
