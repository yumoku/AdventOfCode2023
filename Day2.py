
import sys
from pathlib import Path

input_file = '/Users/yuxiao/Documents/Projects/exercise/AdventOfCode2023/data.txt'

counter = 0
container = []
number = 0

def count_digit(in_string):
    container = []
    for index in range(0, len(in_string)):
        if in_string[index].isdigit():
            container.append(int(in_string[index]))

    sum_digits = int(str(container[0]) + str(container[-1]))

    return sum_digits

with open(input_file, 'r') as input_file:
    for line in input_file:
        number = 0

        number = count_digit(line)
        counter += number

print(counter)

