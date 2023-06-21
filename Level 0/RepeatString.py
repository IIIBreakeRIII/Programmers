# 문자열 반복해서 출력하기

a, b = map(str, input().split())

for _ in range(int(b)):
    print(a, end="")
