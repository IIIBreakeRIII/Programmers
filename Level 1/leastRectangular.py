# 최소 직사각형

def solution(sizes):
    max_height, max_width = 0, 0
    for i in range(len(sizes)):
        sizes[i].sort()
        if max_width <= sizes[i][0]:
            max_width = sizes[i][0]
        else:
            pass

        if max_height <= sizes[i][1]:
            max_height = sizes[i][1]
        else:
            pass

    return max_height * max_width

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
