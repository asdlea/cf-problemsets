def find_xy(matrix):
    i_l = [sum(x) for x in matrix]
    i_l = i_l.index(1)
    x = M[i_l].index(1)
    return (-x, -i_l)

M = [[int(x) for x in input().split()] for _ in range(5)]
x2, y2 = -2,-2
x1, y1 = find_xy(M)

print(abs(x2-x1)+abs(y2-y1))