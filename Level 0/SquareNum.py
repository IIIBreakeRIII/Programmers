# 제곱수 판별

def solution(n):
    if n ** (0.5) - int(n ** (0.5)) == 0:       # 정수형 판별
        return 1
    else:
        return 2