# 푸드 파이트 대회

def solution(food):

    result = ''

    for i in range(1, len(food)):
        if food[i] == 1:
            pass
        elif food[i] % 2 == 0:
            result += str(i) * (food[i] // 2)
        else:
            result += str(i) * ((food[i] - 1) // 2)

    result += str(0)

    for i in reversed(range(1, len(food))):
        if food[i] == 1:
            pass
        elif food[i] % 2 == 0:
            result += str(i) * (food[i] // 2)
        else:
            result += str(i) * ((food[i] - 1) // 2)

    return result

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))
