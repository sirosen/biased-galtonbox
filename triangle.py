from __future__ import print_function, division

def pascal(depth):
    if depth == 0:
        return []
    else:
        tri = [[1]]
        for i in range(depth-1):
            cur_row = tri[-1]
            l = len(cur_row)
            def new_val(i,maxindex):
                if i == 0:
                    return 1
                elif i == maxindex:
                    return 1
                else:
                    return cur_row[i-1] + cur_row[i]

            new_row = [new_val(i,l) for i in range(l+1)]
            tri.append(new_row)

        return tri

def probability_triangle(triangle):
    new_triangle = []
    for row in triangle:
        s = sum(row)
        new_row = [x/s for x in row]
        new_triangle.append(new_row)
    return new_triangle

def subtract_path(triangle, row_n, col_n):
    depth = len(triangle)
    if row_n > depth:
        raise Exception('Woah! We can\'t take things out of the triangle that are deeper than it!')

    to_subtract = probability_triangle(pascal(depth - row_n))
    v = triangle[row_n][col_n]
    for sub_row in to_subtract:
        for i in range(len(sub_row)):
            sub_row[i] *= v

    for r,sub_row in enumerate(to_subtract):
        for c,val in enumerate(sub_row):
            triangle[row_n+r][col_n+c] -= val
