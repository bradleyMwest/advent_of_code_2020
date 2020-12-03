def read_map(file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    return lines

def count_trees(terrain, slope, start_pos, verbose = False):
    map_size = (len(terrain), len(terrain[0]))
    n_trees = 0
    
    row = start_pos[0]
    col = start_pos[1]
    while row < map_size[0]:
        if terrain[row][col] == '#':
            n_trees += 1
        if verbose: print(f'Coord = {(row, col)}, Trees = {n_trees}, spot = {terrain[row][col]}')
        row += slope[0]
        col += slope[1]
        if col >= map_size[1]:
            col -= map_size[1]
    
    return n_trees

terrain = read_map('input_03.txt') 

# part 1
slope = (1,3) # rows x columns
start_pos = (0,0) #upper left corner

n_trees = count_trees(terrain, slope, start_pos)
print(f'You Encountered {n_trees} trees with slope {slope} in Part 1.')
print()

#part 2
slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
prod = 1
for slope in slopes:
    n_trees = count_trees(terrain, slope, start_pos)
    print(f'You Encountered {n_trees} trees with slope {slope} in Part 2.')
    prod *= n_trees
print(f"Total Product = {prod}")