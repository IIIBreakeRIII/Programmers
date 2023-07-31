# 예산

def solution(d, budget):
    d.sort()
    count = 0
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            break
        else:
            count += 1

    return count

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
