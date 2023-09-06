# 점프와 순간 이동

def solution(n):

    ans = 1

    if n == 1:
        return 1
    elif n % 2 == 0:
        pass
    else:
        n -= 1
        ans += 1

    while n != 1:
        if n == 1:
            break

        if n % 2 == 0:
            n /= 2
        else:
            n = (n - 1) // 2
            ans += 1

    return ans

print(solution(5))
print(solution(5000))
print(solution(6))
print(solution(15))
