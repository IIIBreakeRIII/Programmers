# 제곱근 판별

def solution(n):
    result = n ** 0.5
    if n ** 0.5 == int(result):
        print(1)
        return int((result + 1) ** 2)
    else:
        print(-1)
        return -1

solution(121)
solution(3)
