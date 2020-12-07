import numpy as np

with open('input_06.txt', 'r') as f:
    lines = f.read()

# part 1
num_yes_answers = 0
for line in lines.split('\n\n'):
    line = line.replace('\n','')
    num_yes_answers += len(list(set(line)))

print(f"Part 1: Number of yes answers = {num_yes_answers}")

# part 2
unanimous_answers = 0
for group in lines.split('\n\n'):
    num_people = len(group.split('\n'))
    answers = group.replace('\n','')
    letters, counts = np.unique(list(answers),  return_counts=True)
    unanimous_answers += sum(counts == num_people)
print()
print(f"Part 2: Number of unanimous yes answers is {unanimous_answers}")

