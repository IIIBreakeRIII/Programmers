# 멀리 뛰기

def solution(n):
    fib_list = [1, 2, 3]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3

    index = 3
    while index != n:
        if index == n:
            break
        fib_list.append(fib_list[index - 1] + fib_list[index - 2])
        index += 1

    return fib_list[len(fib_list) - 1] % 1234567

print(solution(4))
print(solution(3))
print(solution(1))
print(solution(2))
