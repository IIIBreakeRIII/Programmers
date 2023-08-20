# JadenCase 문자열 만들기

def solution(n):
    answer = ''
    list_n = n.split(" ")
    for i in range(len(list_n)):
        if not list_n[i].isdecimal():
            if list_n[i] == "":
                pass
            else:
                list_n[i] = list_n[i][0].upper() + list_n[i][1:].lower()

    answer = " ".join(list_n)
    return answer

print(solution("3people unFollowed me"))
print(solution("A "))
