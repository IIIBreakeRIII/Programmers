# 치킨 쿠폰

def solution(chicken):
    answer = 0
    while True:
        answer = answer + (chicken // 10)
        chicken = (chicken // 10) + (chicken % 10)
        if chicken < 10:
            break

    return answer
