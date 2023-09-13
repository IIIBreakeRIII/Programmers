# 귤 고르기

def solution(k, tangerine):
    
    type = [0 for i in range(max(tangerine) + 1)]
    answer = 0

    for i in tangerine:
        type[i] += 1

    for i in range(len(type)):
        if k <= 0:
            break
        answer +=1
        max_value = max(type)
        k = k - max_value
        type[type.index(max_value)] = 0

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
