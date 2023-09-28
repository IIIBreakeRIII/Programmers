# 배열의 원소만큼 추가하기

def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        for j in range(arr[i]):
            answer.append(arr[i])

    return answer
