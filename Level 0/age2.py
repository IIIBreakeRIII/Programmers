# [PCCE 기출문제] 3번 / 나이 계산

year = int(input())
age_type = input()
answer = 0

if age_type == "Korea":
    answer = 2030 - year + 1
elif age_type == "Year":
    answer = 2030 - year

print(answer)
