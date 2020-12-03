import numpy as np

def pwd_parser(pwd):
    pwd  = pwd.replace('-', ' ').replace(':','')
    return pwd.split(' ')

def read_passwords(file = 'input_02.txt'):
    with open(file, 'r') as f:
        lines =  file = f.read().splitlines()
    return lines

def check_compliance_part1(pwd_line):
    MIN, MAX, KEY, PWD = pwd_parser(pwd_line)
    valid = 0
    letters, counts = np.unique(list(PWD),  return_counts=True)
    if KEY in letters:
        N = counts[np.argmax(letters == KEY)]
        if N >= int(MIN) and N <= int(MAX):
            valid = 1
    #print(f'Valid = {valid}\t{pwd_line}')
    return valid

def check_compliance_part2(pwd_line):
    MIN, MAX, KEY, PWD = pwd_parser(pwd_line)
    valid = 0
    if PWD[int(MIN)-1] == KEY and PWD[int(MAX)-1] != KEY:
        valid = 1
    elif  PWD[int(MIN)-1] != KEY and PWD[int(MAX)-1] == KEY:
        valid = 1

    return valid

lines = read_passwords()

## part 1
valid = 0
for line in lines:
    valid += check_compliance_part1(line)
print(f"PART 1: There were {valid} valid passwords out of {len(lines)}")

## part 2
valid = 0
for line in lines:
    valid += check_compliance_part2(line)
print(f"PART 2: There were {valid} valid passwords out of {len(lines)}")
