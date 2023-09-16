# 명예의 전당

def solution(k, score):
    price_list = []
    answer = []

    for i in score:
        if len(price_list) < k:
            price_list.append(i)
        else:
            if min(price_list) <= i:
                price_list[price_list.index(min(price_list))] = i

        print(price_list)

        answer.append(min(price_list))

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
