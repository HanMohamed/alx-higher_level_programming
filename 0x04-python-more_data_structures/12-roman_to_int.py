#!/usr/bin/python3

# Create a function that converts a Roman numeral to an integer.
# You can assume the number will be between 1 to 3999.
# If the roman_string is not a string or None, return 0
def roman_to_int(roman_string):
    int_number = 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
             'D': 500, 'M': 1000}

    if roman_string is None or not isinstance(roman_string, str):
        return 0
    myiter = iter(range(0, len(roman_string)))
    for i in myiter:
        if (i + 1 < len(roman_string)) and\
           (roman[roman_string[i]] < roman[roman_string[i + 1]]):
            int_number += (roman[roman_string[i + 1]] - roman[roman_string[i]])
            next(myiter, None)
        else:
            int_number += roman[roman_string[i]]
    return int_number
