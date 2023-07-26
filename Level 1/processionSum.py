# 행렬의 덧셈

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[i])):
            arr_sum.append(arr1[i][j] + arr2[i][j])
        answer.append(arr_sum)

    return answer

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
