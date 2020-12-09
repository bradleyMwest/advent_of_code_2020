from aoc2020.utils import read_file

# part 1
def report_repair(input_list, next_number, verbose=False):
    '''
    problem 1 day 1. 
    Find two numbers in a list that add up to 2020
    and return their product
    '''
    for i in input_list:
        for j in input_list:
            if i != j and i + j == next_number:
                if verbose: print(f"{i} + {j} = {next_number}")
                return True
    return False

def get_first_wrong_number(lines, preamble, verbose = False):
    start = 0
    for i in range(preamble,len(lines)):
        numbers_to_check = lines[start:preamble+start]
        next_number = lines[preamble+start]
        valid = report_repair(numbers_to_check, next_number)
        start+=1
        if not valid:
            if verbose: print(f"{next_number} is invalid")
            return next_number
    return None 

def check_contiguous_sum(input_list, number):
    for i in range(len(input_list)):
        for j in range(2,len(input_list)):
            if sum(input_list[i:j]) == number:
                return min(input_list[i:j]) + max(input_list[i:j])
    return None

#part 1 & 2 test
lines = read_file('test.txt')
preamble = 5
assert get_first_wrong_number(lines, preamble) == 127
assert check_contiguous_sum(lines, 127) == 62

# run part 1 & 2
lines = read_file('input_09.txt')
preamble = 25        
number = get_first_wrong_number(lines, preamble)
print(f"The first wrong number is: {number}")
summed = check_contiguous_sum(lines, number)
print(f"The encryption weakness = {summed}")

