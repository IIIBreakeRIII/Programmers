# n^2 배열 자르기
# 시간 초과

def solution(n, left, right):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    answer_list = []

    for i in range(n):
        for j in range(n):
            if i > j:
                arr[i][j] = i + 1
            else:
                arr[i][j] = j + 1

    for i in range(n):
        for j in range(n):
            answer_list.append(arr[i][j])
    
    print(arr)
    print(answer_list)

    return answer_list[left:right + 1]

print(solution(3, 2, 5))
print(solution(4, 7, 14))
print(solution(3, 3, 4))
