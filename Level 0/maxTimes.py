# 최댓값 만들기

def solution(numbers):
    numbers.sort()
    a = numbers[0] * numbers[1]
    b = numbers[len(numbers) - 1] * numbers[len(numbers) - 2]
    if a > b:
        return a
    else:
        return b
