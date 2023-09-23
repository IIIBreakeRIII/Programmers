# 할인 행사

def solution(want, number, discount):

    result = []
    answer = 0
    buy = {}

    for i in range(len(want)):
        buy[want[i]] = number[i]

    discount_day = 0

    for i in number:
        discount_day += i

    discount_index = 0

    for i in range(len(discount)):

        for i in range(len(want)):
            buy[want[i]] = number[i]

        if discount_day > len(discount):
            break

        for j in range(discount_index, discount_day):
            if discount[j] in buy.keys():
                if buy[discount[j]] == 0:
                    pass
                else:
                    buy[discount[j]] -= 1

        result.append(sum(buy.values()))
        buy.clear()

        discount_index += 1
        discount_day += 1

    for i in result:
        if i == 0:
            answer += 1

    if answer == 0:
        return 0
    else:
        return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
