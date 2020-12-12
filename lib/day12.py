"""

"""

from math import pi, cos, sin
from lib.helpers import timer


inputs = [(line[0], int(line[1:])) for line in open("inputs/day12_input.txt", "r").read().splitlines()]

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
RIGHT = 'R'
LEFT = 'L'
FORWARD = 'F'

clockwise = [EAST, SOUTH, WEST, NORTH]
c_clockwise = [EAST, NORTH, WEST, SOUTH]


def cardinal_add(cardinal, x, y, amount):
    nx = x
    ny = y
    if cardinal == NORTH:
        ny += amount
    elif cardinal == SOUTH:
        ny -= amount
    elif cardinal == EAST:
        nx += amount
    elif cardinal == WEST:
        nx -= amount

    return nx, ny


@timer
def part01(input_list):
    x = y = 0
    direction = EAST
    for orient, amount in input_list:
        if orient in clockwise:
            x, y = cardinal_add(orient, x, y, amount)
        elif orient in [RIGHT, LEFT]:
            rots = amount // 90
            turning = clockwise if orient == RIGHT else c_clockwise
            direction = turning[(turning.index(direction) + rots) % 4]
        else:
            if direction == EAST:
                x += amount
            elif direction == SOUTH:
                y -= amount
            elif direction == WEST:
                x -= amount
            elif direction == NORTH:
                y += amount

    return ((x, y), direction), abs(x) + abs(y)


@timer
def part02(input_list):
    x = y = 0
    wx = 10
    wy = 1
    for orient, amount in input_list:
        if orient in clockwise:
            wx, wy = cardinal_add(orient, wx, wy, amount)
        elif orient in [RIGHT, LEFT]:
            rots = amount // 90
            theta = -(pi/2) if orient == RIGHT else pi/2
            for i in range(rots):
                n_wx = int(round((wx * cos(theta)) - (wy * sin(theta))))
                n_wy = int(round((wx * sin(theta)) + (wy * cos(theta))))
                wx = n_wx
                wy = n_wy
        else:
            x += wx*amount
            y += wy*amount
    return (x, y), abs(x) + abs(y)


print(part01(inputs))
print(part02(inputs))
