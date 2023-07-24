# 부족한 금액 계산하기

def solution(price, money, count):
    
    total_need = 0

    for i in range(count):
        total_need += price * (i + 1)

    if total_need - money <= 0:
        return 0
    else:
        return total_need - money

print(solution(3, 20, 4))
