"""

"""

# from time import perf_counter
# from functools import wraps
# def timer(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = perf_counter()
#         ret = func(*args, **kwargs)
#         print(f"{func.__name__.replace('_', ' ')} took: {perf_counter() - start:.8f} seconds")
#         return ret
#     return wrapper


input_list = sorted([int(line) for line in open("inputs/day10_input.txt", "r").read().splitlines()])
# input_list.insert(0, 0)
input_list.append(max(input_list)+3)
# print(input_list)


def part01():
    prev_digit = 0
    diff = []
    for ind, digit in enumerate(input_list):
        diff.append(digit - prev_digit)
        prev_digit = digit
    return diff.count(1) * diff.count(3)


def part02():
    """
    2-pointers to check chunks from the end of the list backwards, adding successful chunks each time.
    :return:
    :rtype:
    """
    ptr = 0
    chunk_sum = 0
    valid_paths = [0] * len(input_list)

    for ind, digit in enumerate(input_list):
        while ptr < ind and input_list[ptr] < digit-3:
            chunk_sum -= valid_paths[ptr]
            ptr += 1

        valid_paths[ind] = chunk_sum + (digit <= 3)
        chunk_sum += valid_paths[ind]

    return int(valid_paths[-1])


# print(part01())
part02()
