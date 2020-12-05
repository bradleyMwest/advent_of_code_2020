from math import ceil

def read_input(file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    return lines

def get_row_seat(index, verbose=False):
    row_pos = [0, 127]
    seat_pos = [0, 7]
    for i in index:
        row_diff = ceil((row_pos[1]-row_pos[0])/2)
        seat_diff = ceil((seat_pos[1]-seat_pos[0])/2)
        if i == "F":
            row_pos[1] -= row_diff
        elif i == "B":
            row_pos[0] += row_diff
        elif i == "L":
            seat_pos[1] -= seat_diff
        elif i == "R":
            seat_pos[0] += seat_diff
        if verbose: print(f"{i}, {row_pos}, {seat_pos}")
    if verbose: print(f"the final row = {row_pos[0]} and seat {seat_pos[0]}")
    return row_pos[0], seat_pos[0]

def find_your_seat(seats):
    seats.sort()
    your_seat = None
    prev_seat = seats[0]
    for seat in seats:
        if seat - prev_seat > 1:
            your_seat = prev_seat + 1 
            return your_seat
        prev_seat = seat
    return your_seat

boarding_passes = read_input("input_05.txt")

# part 1
max_id = -1
for bpass in boarding_passes:
    row, seat = get_row_seat(bpass)
    seat_id = row*8+seat
    #print(f"{bpass}: row {row}, seat {seat}, id {row*8+seat}")
    max_id = max(max_id, seat_id)
print(f"The max_id is {max_id}")

print()

# part 2
seats = []
for bpass in boarding_passes:
    row, seat = get_row_seat(bpass)
    seat_id = row*8+seat
    seats.append(seat_id)
your_seat = find_your_seat(seats)
print(f"Your seat number is {your_seat}")