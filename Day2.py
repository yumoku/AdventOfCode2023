
import sys
from pathlib import Path
import re

input_file = '/Users/yuxiao/PycharmProjects/AdventOfCode2023/Day2_data.txt'

test_items = {
    "red": 12,
    "green": 13,
    "blue": 14
}
max_items = {}
counter = 0
index = 0
power = 0

def convert_string_to_dict(in_string):
    result_dict = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    in_list = []

    in_list = in_string.split(',')

    for item in in_list:
        item = item.strip(' ').split(' ')

        if "red" in item[1]:
            result_dict["red"] = int(item[0])
        if "blue" in item[1]:
            result_dict["blue"] = int(item[0])
        if "green" in item[1]:
            result_dict["green"] = int(item[0])

    return result_dict


def calculate_max_items(in_string):
    items = {}
    max_items = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    modified_string = []
    each_line = ""

    modified_string = in_string.split(':')[1].strip(' ').split(';')

    for item in modified_string:
        each_line = item.strip(' ')
        items = convert_string_to_dict(each_line)
        #print(items)

        if items["red"] > max_items["red"]:
            max_items["red"] = items["red"]
        if items["blue"] > max_items["blue"]:
            max_items["blue"] = items["blue"]
        if items["green"] > max_items["green"]:
            max_items["green"] = items["green"]

    return max_items

def compare_items(max_list, test_list):
    flag = True

    if max_list["red"] > test_list["red"]:
        flag = False
        #print("red flag is: ", flag)
    if max_list["blue"] > test_list["blue"]:
        flag = False
        #print("blue flag is: ", flag)
    if max_list["green"] > test_list["green"]:
        flag = False
        #print("green flag is: ", flag)
    return flag

with open(input_file, 'r') as input_file:
    for line in input_file:
        index += 1
        max_items = calculate_max_items(line)

        if compare_items(max_items, test_items):
            # print(f"Game {index} passes")
            counter += index

        power += max_items["red"] * max_items["blue"] * max_items["green"]

print("The output of first half of the game is: ", counter)
print("The output of the second half of the game is: ", power)
