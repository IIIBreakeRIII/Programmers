# 숫자의 표현

def solution(n):
    count = 0

    for i in range(1, n):
        result = 0
        for j in range(i, n):
            result += j
            if result == n:
                count += 1
                break
            elif result >= n:
                break

    return count + 1

print(solution(15))
