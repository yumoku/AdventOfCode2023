
import sys
from pathlib import Path

input_file = '/Users/yuxiao/PycharmProjects/AdventOfCode2023/Day1_data.txt'

counter = 0
container = []
number = 0
digits_in_letter = {'one': 1,
                    'two': 2,
                    'three': 3,
                    'four': 4,
                    'five': 5,
                    'six': 6,
                    'seven': 7,
                    'eight': 8,
                    'nine': 9}

def combine_digits(in_string):
    '''

    :param: a string
    :return: combine the first digit and the last digit into a number

    '''
    container = []
    for index in range(0, len(in_string)):
        if in_string[index].isdigit():
            container.append(int(in_string[index]))

    sum_digits = int(str(container[0]) + str(container[-1]))

    return sum_digits

def combine_digits_v2(in_string):
    '''

    :param in_string:
    :return: combine the first digit and the last digit into a number including number in letter
    '''

    container = []
    digits_info = {}
    fist_and_last_digits = []
    sum_digits = 0

    digits_info = find_all_digits(in_string)
    first_and_last_digits = find_first_and_last_digits(digits_info)
    #print(first_and_last_digits)

    sum_digits = int(str(first_and_last_digits[0]) + str(first_and_last_digits[-1]))

    return sum_digits

def find_all_digits(in_string):
    '''

    :param in_string:
    :return: all the digits and their location
    '''
    digits_info = {}
    indexes = []

    for index in range(0, len(in_string)):
        if in_string[index].isdigit():
            digits_info[index] = int(in_string[index])

    for key, value in digits_in_letter.items():
        indexes = find_all_occurrences(in_string, key)

        for item in indexes:
            digits_info[item] = value

    return digits_info

def find_all_occurrences(main_string, sub_string):
    '''

    :param main_string:
    :param sub_string:
    :return: find all occurrence of the sub_string and return their indexes as list
    '''
    start = 0
    indexes = []
    while start < len(main_string):
        index = main_string.find(sub_string, start)
        if index == -1:
            break
        indexes.append(index)
        start = index + 1
    return indexes

def find_first_and_last_digits(in_dict):
    '''

    :return: find the first and the last digit in a string in both digit or letter
    '''
    first_and_last_digits = []
    indexes = []
    first = 0
    last = 0

    for key in in_dict.keys():
        indexes.append(int(key))

    first = min(indexes)
    last = max(indexes)
    first_and_last_digits = [in_dict[first], in_dict[last]]
    return first_and_last_digits

with open(input_file, 'r') as input_file:
    for line in input_file:
        number = combine_digits_v2(line)
        counter += number

print(counter)