# 다음 큰 숫자

def solution(n):

    n_decimal = format(n, 'b')
    n_decimal_count = 0

    for i in n_decimal:
        if i == "1":
            n_decimal_count += 1

    while n <= 1000000:
        n += 1
        n_decimal = format(n, 'b')
        temp = 0

        for i in n_decimal:
            if i == "1":
                temp += 1

        if temp == n_decimal_count:
            break
    
    return n

print(solution(78))
print(solution(15))
