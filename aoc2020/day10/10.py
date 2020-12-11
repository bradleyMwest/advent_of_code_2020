from aoc2020.utils import read_file

def check_adapters(adapters, verbose=False):
    adapters.sort()
    diff_1 = 0
    diff_3 = 1 #device difference
    current_joltage = 0
    for i in adapters:
        diff = i - current_joltage
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
        elif diff > 3:
            print("adapter doesnt work")
            break
        current_joltage = i
    if verbose: print(f"N adapters with 1 jolt difference = {diff_1}")
    if verbose: print(f"N adapters with 3 jolt difference = {diff_3}")
    return diff_1 * diff_3

# #test 1 
# adapters = read_file('test.txt')
# assert check_adapters(adapters) == 35

# #test 2
# adapters = read_file('test_2.txt')
# assert check_adapters(adapters) == 220

# # part 1
# adapters = read_file('input_10.txt')
# ans = check_adapters(adapters, verbose=True)
# print(f"the part 1 answer is {ans}")

#part 2 -- find all combinations
adapters = read_file('test.txt')
start_jolt = 0
end_jolt = max(adapters) + 3
adapters.extend([start_jolt, end_jolt])
adapters.sort()

current = start_jolt
diff = []
for i in adapters[1:]:
    diff.append(i-current)
    current = i
print(diff)
# for idx, jolt in enumerate(adapters):


