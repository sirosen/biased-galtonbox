from __future__ import print_function, division
from triangle import remove_slice

def get_diff(target, xs):
    return abs(sum(xs) - target)

def walk_to_val(target, xs, epsilon):
    i = 0
    while i < len(xs):
        if epsilon > abs(xs[i] - target):
            return i
        else:
            i += 1

    return -1

def prefix_sums(xs):
    ys = xs[:]
    tot = 0
    for i in range(len(ys)):
        tot += ys[i]
        ys[i] = tot
        i += 1
    return ys

def closest_left_slice(target, distribution, epsilon):
    ps = prefix_sums(distribution)
    return walk_to_val(target, ps, epsilon)

def closest_right_slice(target, distribution, epsilon):
    ps = prefix_sums(distribution[::-1])
    i = walk_to_val(target, ps, epsilon)
    if i == -1: return -1
    else: return len(distribution) - i

def find_slices(dist_triangle, buckets, margin):
    cur_buckets = buckets[:]
    left_slice_points = []
    right_slice_points = []
    for row_index,row in enumerate(dist_triangle):
        left, right = True, True
        while left or right:
            left = right = False
            col_index = closest_left_slice(cur_buckets[1], row, margin*cur_buckets[1])
            if col_index != -1:
                left = True
                left_slice_points.append((row_index,col_index))
                remove_slice(dist_triangle, row_index, col_index)
            col_index = closest_right_slice(cur_buckets[-1], row, margin*cur_buckets[-1])
            if col_index != -1:
                right = True
                right_slice_points.append((row_index,col_index))
                remove_slice(dist_triangle, row_index, col_index)

    return (left_slice_points, right_slice_points)
