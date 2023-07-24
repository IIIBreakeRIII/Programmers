# 문자열 내림차순으로 배치하기

def solution(s):
    return "".join(reversed(sorted(s)))

print(solution("Zbcdefg"))
