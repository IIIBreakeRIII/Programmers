# 아이스 아메리카노

def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money - (answer[0] * 5500))
    return answer
