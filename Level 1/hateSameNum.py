# 같은 숫자는 싫어

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i] == arr[i - 1]:
                continue
            else:
                answer.append(arr[i])

    return answer

print(solution([1, 1, 2, 2, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
