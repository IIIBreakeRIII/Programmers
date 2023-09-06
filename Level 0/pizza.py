# 피자 나눠 먹기

def solution(n):
    if n <= 7:
        return 1
    elif n % 7 == 0:
        return n // 7
    return n // 7 + 1
