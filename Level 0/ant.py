# 개미 군단

def solution(hp):
    answer = 0
    
    answer += hp // 5
    hp = hp - (5 * (hp // 5))
    answer += hp // 3
    hp = hp - (3 * (hp // 3))
    answer += hp // 1

    return answer