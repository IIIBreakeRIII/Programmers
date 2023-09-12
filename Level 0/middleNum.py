# 중앙값 구하기

def solution(array):
    array.sort()
    return array[len(array) // 2]
