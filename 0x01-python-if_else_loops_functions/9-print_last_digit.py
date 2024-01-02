#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        end_num = abs(number) % 10
        print((end_num), end='')
    else:
        end_num = number % 10
        print(end_num, end='')
    return abs(end_num)
