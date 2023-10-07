# 꼬리 문자열

def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex in i:
            continue
        else:
            answer += i

    return answer
