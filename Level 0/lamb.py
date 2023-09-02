# 양꼬치

def solution(n, k):
    service = n // 10
    k -= service
    return 12000 * n + 2000 * k
