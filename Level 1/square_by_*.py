def solution(a, b):
    a, b = map(int, input().strip().split(' '))
    print(("*" * a + "\n") * b)

solution(5, 3)