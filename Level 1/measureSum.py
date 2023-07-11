# 약수의 합

def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 0:
            answer = answer + i
        else:
            pass
    answer = answer + n
    return answer

solution(12)
solution(5)
