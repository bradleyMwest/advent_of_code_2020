def doPart1(lines, verbose = False):
    repeat = False # boolean flag if a rule has been repeated
    acc = 0        # global accumulator value
    rule_index = 0 # line index for current rule
    rule_history = [] #line history for previous rules

    while repeat is False and rule_index != len(lines):
        #get current rule 
        line = lines[rule_index]
        if verbose: print(f"{rule_index}\t{acc}\t{line}")
        rule_history.append(rule_index)
        
        #read the rule and do the action
        op, value = line.split(' ')
        if op == 'acc':
            acc += int(value)
            rule_index += 1
        elif op == 'nop':
            rule_index += 1
        elif op == 'jmp':
            rule_index += int(value)
        
        #check if rule is a repeat
        if rule_index in rule_history:
            if verbose: print(f"Repeated Operatation:\n\tAccumulator value = {acc}")
            repeat = True
        
    return acc, rule_history, repeat

def line_edit(lines, index):
    op, val = lines[index].split(' ')
    if op == 'nop':
        lines[index] = 'jmp ' + val
    elif op == 'jmp':
        lines[index] = 'nop ' + val
    return lines

#read the rules
with open('input_08.txt', 'r') as f:
    lines = f.read().splitlines()

#part 1
acc, rule_history, repeat = doPart1(lines)
if repeat: print(f"Repeated Operatation:\n\tAccumulator value = {acc}")


#part 2
for rule in rule_history:
    lines = line_edit(lines, rule)# flip the rule
    
    acc, rule_history, repeat = doPart1(lines)
    if not repeat:
        print(f"The Infinite loop is gone! Acc value = {acc}")
        break
    
    lines = line_edit(lines, rule)#flip it back
