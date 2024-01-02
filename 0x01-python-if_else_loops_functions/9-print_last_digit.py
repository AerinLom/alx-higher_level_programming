#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
        end_num = number % 10
        print(-(end_num), end='')
    else:
        end_num = number % 10
        print(end_num, end='')
    return abs(end_num)
