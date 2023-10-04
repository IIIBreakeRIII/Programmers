# 더 크게 합치기

def solution(a, b):
    if int(str(a) + str(b)) >= int(str(b) + str(a)):
        return int(str(a) + str(b))
    else:
        return int(str(b) + str(a))
