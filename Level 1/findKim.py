# 서울에서 김서방 찾기

def solution(seoul):
    answer = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = '김서방은 {}에 있다'.format(i)
        else:
            pass
    return answer

solution(["Jane", "Kim"])
