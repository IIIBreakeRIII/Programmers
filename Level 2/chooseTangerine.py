def sorting(dictionary):

    tan_list = []

    for i in dictionary:
        tan_list.append(dictionary[i])

    tan_list.sort(reverse=True)

    return tan_list

def solution(k, tangerine):

    type = {}
    answer = 0
    index = 0

    for i in tangerine:
        if i in type.keys():
            type[i] += 1
        else:
            type[i] = 1

    temp = sorting(type)

    while k > 0:
        answer += 1
        k -= temp[index]
        index += 1

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
