# 콜라츠 추측

def solution(n):

    count = 0

    while n > 1:
        if n % 2 == 0:
            n = n // 2
            count = count + 1
        else:
            n = n * 3 + 1
            count = count + 1
    else:
        if count > 500:
            count = -1

        else:
            pass

        return count

solution(6)
solution(16)
solution(626331)
