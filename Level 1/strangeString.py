# 이상한 문자 만들기

def solution(s):
    answer = ''
    word_list = s.split(" ")
    for i in word_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "

    return answer[0:-1]

print(solution("try hello world"))
