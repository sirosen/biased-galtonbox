def pascal(depth):
    if depth == 0:
        return []
    else:
        tri = [[1]]
        for i in range(depth):
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
