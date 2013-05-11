from __future__ import print_function, division

def get_diff(target, xs):
    return abs(sum(xs) - target)

def closest_left_slice(target, distribution, epsilon):
    index = 0
    while index < len(distribution) and \
            get_diff(target, distribution[:index]) > epsilon:
        index += 1

    if index == len(distribution):
        return 0

    cur_diff = get_diff(target, distribution[:index])
    while index < len(distribution):
        if get_diff(target, distribution[:index+1]) < cur_diff:
            index += 1
        else:
            break

    return index

def closest_right_slice(target, distribution, epsilon):
    index = len(distribution)
    while index >= 0 and \
            get_diff(target, distribution[index:]) > epsilon:
        index -= 1

    if index == -1:
        return len(distribution)

    cur_diff = get_diff(target, distribution[index:])
    while index > 0:
        if get_diff(target, distribution[index-1:]) < cur_diff:
            index -= 1
        else:
            break

    return index



def find_slices(dist_triangle, buckets, margin):
    cur_buckets = buckets[:]
    slice_points = []
    for row_index,row in enumerate(triangle):
        col_index = closest_left_slice(cur_buckets[1], row, margin*cur_buckets[1])
        if col_index >= 0:
            slice_points.append((row_index,col_index))
        rindex = closest_right_slice(cur_buckets[:
