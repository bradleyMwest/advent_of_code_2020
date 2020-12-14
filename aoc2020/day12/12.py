def getDir(ANGLE):
    if ANGLE == 0:
        d = "N"
    elif ANGLE == 90:
        d = 'E'
    elif ANGLE == 180:
        d = 'S'
    elif ANGLE == 270:
        d = 'W'
    return d

def rotate(lr, mag, current_angle):
    if lr == 'L':
        new_angle = current_angle - mag
    elif lr == 'R':
        new_angle = current_angle + mag

    if new_angle < 0:
        new_angle += 360
    elif new_angle >= 360:
        new_angle -= 360
    
    return new_angle 




pos = {}
pos["N"] = 0
pos["E"] = 0
pos["S"] = 0
pos["W"] = 0

CURRENT_ANGLE = 90

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    action = line[0]
    mag = int(line[1:])

    if action in ["N", "S", "E", "W"]:
        pos[action] += mag
    
    elif action == "F":
        d = getDir(CURRENT_ANGLE)
        pos[d] += mag
    
    elif action in ["L", "R"]:
        CURRENT_ANGLE = rotate(action, mag, CURRENT_ANGLE)

manhattan = abs(pos["N"] - pos["S"]) + abs(pos['E'] - pos['W'])

print("Part 1: ",manhattan)        

way_point = {}
way_point["N"] = 1
way_point["E"] = 10
way_point["S"] = 0
way_point["W"] = 0

pos = {}
pos["N"] = 0
pos["E"] = 0
pos["S"] = 0
pos["W"] = 0

