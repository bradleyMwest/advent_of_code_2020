import sys
import logging


def report_repair(input_list):
    '''
    problem 1 day 1. 
    Find two numbers in a list that add up to 2020
    and return their product
    '''
    for i in input_list:
        for j in input_list:
            if i != j and i + j == 2020:
                print(f"{i} * {j} = {i*j}")
                return i*j

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter input file path")
        exit
    elif len(sys.argv) == 2:
        fname = sys.argv[1]
    
    with open(fname, 'r') as f:
        file = f.read().splitlines() # this reads each line in as a string
        input_list = [int(i) for i in file] # convert string to int

    answer = report_repair(input_list)
    print(answer)

    

