import os
import sys
from aoc2020.utils import read_file

# part 1
def report_repair_1(input_list):
    '''
    problem 1 day 1. 
    Find two numbers in a list that add up to 2020
    and return their product
    '''
    for i in input_list:
        for j in input_list:
            if i != j and i + j == 2020:
                print(f"{i} + {j} = 2020\n{i} * {j} = {i*j}")
                return i*j

# part 2
def report_repair_2(input_list):
    '''
    problem 2 day 1. 
    Find three numbers in a list that add up to 2020
    and return their product
    '''
    for i in input_list:
        for j in input_list:
            for k in input_list:
                if (i != j and j!=k and i != k) and i + j  + k == 2020:
                    print(f"{i} + {j} + {k} = 2020\n{i} * {j} * {k} = {i*j*k}")
                    return i*j*k

if __name__ == "__main__":
    # get current file location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fname = os.path.join(current_dir, 'input_01.txt')
    input_list = read_file(fname)

    print("Part 1:")
    report_repair_1(input_list)

    print('\nPart 2:')
    report_repair_2(input_list)


