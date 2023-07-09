def solution(a, b):
    if(a <= b):
        return sum(range(a, b)) + b
    else:
        return sum(range(a, b, -1)) + b

print(solution(3, 5))