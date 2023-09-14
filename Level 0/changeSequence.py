# 조건에 맞게 수열 변환하기3

def solution(arr, k):
    answer = []
    if k % 2 == 0:
        for i in arr:
            i += k
            answer.append(i)
        return answer
    else:
        for i in arr:
            i *= k
            answer.append(i)
        return answer
