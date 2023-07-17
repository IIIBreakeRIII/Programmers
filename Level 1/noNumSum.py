# 없는 숫자 더하기

def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]
