#!/usr/bin/env python
# Author: Christopher Segale
# Date: 3/10/2013

def main():
    of = open("list.txt")
    numbers = of.read()
    of.close()

    max_product = 0
    number_one = 0
    number_two = 0
    number_three = 0
    number_four = 0
    number_five = 0
    product = 0

    for index in range(0, len(numbers) - 5):
        number_one = int(numbers[index])
	number_two = int(numbers[index + 1])
	number_three = int(numbers[index + 2])
	number_four = int(numbers[index + 3])
	number_five = int(numbers[index + 4])
	product = number_one * number_two * number_three * number_four * number_five
	if max_product < product:
            max_product = product

    print max_product

if __name__ == '__main__':
    main()
