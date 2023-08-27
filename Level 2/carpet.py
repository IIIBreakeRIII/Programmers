# 카펫

def solution(brown, yellow):

    carpet = brown + yellow
    temp = 3
    carpet_list = []

    while temp <= carpet:
        if carpet % temp == 0:
            carpet_list.append([temp, carpet // temp])
            temp += 1
        else:
            temp += 1

    for i in carpet_list:
        if (i[0] - 2) * (i[1] - 2) == yellow:
            return [max(i), min(i)]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
