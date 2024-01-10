#!/usr/bin/python3

def roman_to_int(roman_string: str):

    if roman_string is None or type(roman_string) != str:
        return 0

    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    
    for ch in range(len(roman_string)):

        if ch > 0 and roman_numbers[roman_string[ch]] > roman_numbers[roman_string[ch - 1]]:
            integer += roman_numbers[roman_string[ch]] - 2 * roman_numbers[roman_string[ch - 1]]

        else:
            integer += roman_numbers[roman_string[ch]]

    return integer
