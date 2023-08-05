# K 번째 수

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        first_index = commands[i][0] - 1
        last_index = commands[i][1]
        counts = commands[i][2] - 1

        temp_list = array[first_index:last_index]

        temp_list.sort()

        answer.append(temp_list[counts])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

