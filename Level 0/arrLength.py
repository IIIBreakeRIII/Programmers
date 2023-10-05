# 배열의 길이에 따라 다른 연산하기

def solution(arr, n):
    if len(arr) % 2 == 0:
        for i in range(len(arr)):
            if i % 2 == 1:
                arr[i] += n

    else:
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] += n

    return arr
