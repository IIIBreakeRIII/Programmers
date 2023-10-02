# 접두사인지 확인하기

def solution(my_string, is_prefix):
    if is_prefix in my_string:
        if is_prefix[0:] == my_string[0:len(is_prefix) - 1]:
            return 1
        
    return 0
