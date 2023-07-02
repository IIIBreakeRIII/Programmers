# 문자열 내 p와 y의 개수

def solution(s):
    list_s = list(map(str, str(s)))
    count_p = 0
    count_y = 0

    for i in range(len(list_s)):
        if list_s[i] == "p" or list_s[i] == "P":
            count_p += 1
        elif list_s[i] == "y" or list_s[i] == "Y":
            count_y += 1
        else:
            pass

    if count_p == count_y:
        return True
    else:
        return False

solution("pPoooyY")
solution("Pyy")
