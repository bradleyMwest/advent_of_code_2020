import numpy as np


def swap_seats(seat_map):
    new_map = seat_map.copy()
    rows, cols = seat_map.shape
    changes = 0
    for row in range(rows):
        for col in range(cols):
            current_seat = seat_map[row, col]
            if current_seat == 0:
                continue

            min_row = 0 if row - 1 < 0 else row - 1
            max_row = rows if row + 2 > rows else row+2
            
            min_col = 0  if col - 1 < 0 else col - 1
            max_col = cols if col + 2 > cols else col + 2

            window = seat_map[min_row:max_row, min_col:max_col]

            #print(min_row, max_row, '\t', min_col, max_col)
            #print(window)
            #print(f"\t{np.sum(window)}\t{np.sum(window) - current_seat}\t{np.sum(window == 1)}")

            if current_seat == 'L' and np.sum(window == '#') == 0:
                changes += 1
                new_map[row,col] = '#'

            elif current_seat == '#' and np.sum(window == "#") >= 5:
                changes += 1
                new_map[row,col] = 'L'
    return new_map, changes

''' 
  NW    N   NE
     \  :  /
      \ : /
  W---- . ---- E
      / : \
     /  :  \
  SW    S   SE
'''
    

def W(m, row, col):
    return m[row, 0:col][::-1]

def E(m, row, col):
    return m[row, col+1:m.shape[1]]

def N(m, row, col):
    return m[0:row, col][::-1]

def S(m, row, col):
    return m[row+1:m.shape[0], col]

def NE(m, row, col):
    w = m[0:row, col+1:m.shape[1]]
    r, c = w.shape
    if r > c:
        w = w[-c:, :c]
    elif r < c:
        w = w[-r:, :r]
    return np.flipud(w).diagonal()

def NW(m, row, col):
    "checked"
    w = m[0:row, 0:col]
    r, c = w.shape
    if r > c:
        w = w[-c:, -c:]
    elif r < c:
        w = w[-r:, -r:]
    return w.diagonal()[::-1]

def SW(m, row, col):
    w = m[row+1:m.shape[0], 0:col]
    r, c = w.shape
    if r > c:
        w = w[:c, -c:]
    elif r < c:
        w = w[:r, -r:]
    return np.flipud(w).diagonal()[::-1]

def SE(m, row, col):
    "checked"
    w = m[row+1:m.shape[0],  col+1:m.shape[1]]
    r, c = w.shape
    if r > c:
        w = w[:c, :c]
    elif r < c:
        w = w[:r, :r]
    return w.diagonal()

def check_all_directions(m, row, col, verbose=False):
    visible_seats = []
    debug = {}
    for func in [N, E, S, W, NE, NW, SE, SW]:
        res = func(m, row, col)
        if res.size == 0: continue
        first_non_floor_index = np.argmax(res != '.')
        debug[func.__name__] = (res)
        visible_seats.append(res[first_non_floor_index])
    if verbose: print(debug)
    return np.array(visible_seats)
    

def swap_vis_seats(seat_map):
    new_map = seat_map.copy()
    rows, cols = seat_map.shape
    changes = 0
    for row in range(rows):
        for col in range(cols):
            current_seat = seat_map[row, col]
            if current_seat == '.':
                continue
            
            near_by_seats = check_all_directions(seat_map, row, col)
            

            if current_seat == 'L' and np.sum(near_by_seats == '#') == 0:
                changes += 1
                new_map[row,col] = '#'

            elif current_seat == '#' and np.sum(near_by_seats == "#") >= 5:
                changes += 1
                new_map[row,col] = 'L'
    return new_map, changes

# swap seats until no more changes
iterations = 0
changes = 1


with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

seat_map_orig = np.array([[place for place in line] for line in lines])
seat_map = seat_map_orig.copy()

while changes != 0:
    iterations += 1
    seat_map, changes = swap_seats(seat_map)

N_occupied = (seat_map == "#").sum()
print(f"Part 1: After {iterations} iterations. Equilibrium is reached and {N_occupied} seats are occupied")

changes = 1
iterations = 0
seat_map = seat_map_orig.copy()
while changes != 0:
    iterations += 1
    seat_map, changes = swap_vis_seats(seat_map)

N_occupied = (seat_map == "#").sum()
print(f"Part_2 After {iterations} iterations. Equilibrium is reached and {N_occupied} seats are occupied")