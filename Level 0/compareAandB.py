# 두 수의 연산값 비교하기

def solution(a, b):
    plus = int(str(a) + str(b))
    time = 2 * a * b
    if plus >= time:
        return plus
    else:
        return time
