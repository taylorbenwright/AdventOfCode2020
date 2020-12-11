"""

"""

from itertools import chain
from copy import deepcopy
from time import perf_counter
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        ret = func(*args, **kwargs)
        print(f"{func.__name__.replace('_', ' ')} took: {perf_counter() - start:.8f} seconds")
        return ret
    return wrapper


class NonNegativeList(list):
    def __getitem__(self, item):
        if item < 0:
            raise IndexError('...')
        return list.__getitem__(self, item)


inputs = NonNegativeList([NonNegativeList([char for char in line]) for line in open("inputs/day11_input.txt", "r").read().splitlines()])

EMPTY = 'L'
FLOOR = '.'
OCCUPIED = '#'


def get_occupied_cells(input_list, row, column, skip_empty=False):
    itr = 0

    ind = 1
    while True:  # top left
        try:
            if input_list[row-ind][column-ind] == OCCUPIED:
                itr += 1
                break
        except IndexError:
            break
        if not skip_empty:
            break
        ind += 1

    ind = 1
    while True:  # top middle
        try:
            if input_list[row-ind][column] == OCCUPIED:
                itr += 1
                break
        except IndexError:
            break
        if not skip_empty:
            break
        ind += 1

    ind = 1
    while True:  # top right
        try:
            if input_list[row-ind][column+ind] == OCCUPIED:
                itr += 1
                break
        except IndexError:
            break
        if not skip_empty:
            break
        ind += 1

    ind = 1
    while True:  # center left
        try:
            if input_list[row][column-ind] == OCCUPIED:
                itr += 1
                break
        except IndexError:
            break
        if not skip_empty:
            break
        ind += 1

    ind = 1
    while True:  # center right
        try:
            if input_list[row][column+ind] == OCCUPIED:
                itr += 1
                break
        except IndexError:
            break
        if not skip_empty:
            break
        ind += 1

    ind = 1
    while True:  # bottom left
        try:
            if input_list[row+ind][column-ind] == OCCUPIED:
                itr += 1
                break
        except IndexError:
            break
        if not skip_empty:
            break
        ind += 1

    ind = 1
    while True:  # bottom middle
        try:
            if input_list[row+ind][column] == OCCUPIED:
                itr += 1
                break
        except IndexError:
            break
        if not skip_empty:
            break
        ind += 1

    ind = 1
    while True:  # bottom right
        try:
            if input_list[row+ind][column+ind] == OCCUPIED:
                itr += 1
                break
        except IndexError:
            break
        if not skip_empty:
            break
        ind += 1

    return itr


@timer
def fill_seats(input_list, occupied_threshold=4, skip_empty=False):
    loops = 0
    while True:
        buffer_list = deepcopy(input_list)
        for ind1, row in enumerate(input_list):
            for ind2, state in enumerate(row):
                occupied_cells = get_occupied_cells(input_list, ind1, ind2, skip_empty=skip_empty)
                if state == EMPTY and occupied_cells == 0:
                    buffer_list[ind1][ind2] = OCCUPIED
                elif state == OCCUPIED and occupied_cells >= occupied_threshold:
                    buffer_list[ind1][ind2] = EMPTY

                # if occupied_cells == 0 and state == EMPTY:
                #     buffer_list[ind1][ind2] = OCCUPIED
                # elif occupied_cells >= occupied_threshold and state == OCCUPIED:
                #     buffer_list[ind1][ind2] = EMPTY
                # print(occupied_cells)
                # if state == EMPTY:
                #     if check_empty_rule(occupied_cells):
                #         buffer_list[ind1][ind2] = OCCUPIED
                # elif state == OCCUPIED:
                #     if check_occupied_rule(occupied_cells, 4):
                #         buffer_list[ind1][ind2] = EMPTY

        loops += 1
        if input_list == buffer_list:
            break
        input_list = buffer_list
    return list(chain(*input_list)).count(OCCUPIED)


print(fill_seats(inputs))
print(fill_seats(inputs, occupied_threshold=5, skip_empty=True))

# print(list(chain(*input_list)).count(OCCUPIED), loops)
