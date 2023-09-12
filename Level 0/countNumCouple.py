# 순서쌍의 개수

def solution(n):
    answer = []
    for i in range(1, n):
        if n % i == 0:
            answer.append(i)

    return len(answer) + 1
