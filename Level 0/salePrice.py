# 옷가게 할인 받기

def solution(price):
    if 300000 > price >= 100000:
        return int(price * 0.95)
    elif 500000 > price >= 300000:
        return int(price * 0.90)
    elif price >= 500000:
        return int(price * 0.80)
    return price

print(solution(580000))
