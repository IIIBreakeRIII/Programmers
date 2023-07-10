# 신규 아이디 추천

import string

def solution(new_id):
    
    # 1단계 대문자 소문자 치환
    lower_new_id = new_id.lower()
    print("No. 1")
    print(lower_new_id)
    print("-----")

    # 2단계 문자 제거
    list_new_id = list(map(str, str(lower_new_id)))
    temp_word = ''
    
    for i in range(len(list_new_id)):
        if list_new_id[i] in string.ascii_lowercase or list_new_id[i] in "-_." or list_new_id[i] in string.digits:
            temp_word = temp_word + list_new_id[i]
    
    print("No. 2")
    print(temp_word)
    print("-----")

    # 3단계 ".." => "." 로 치환
    while ".." in temp_word:
        temp_word = temp_word.replace('..', ".")
    
    print("No. 3")
    print(temp_word)
    print("-----")

    # 4단계 "." 처음 끝에 있으면 제거
    list_temp_word = list(map(str, str(temp_word)))
    if len(list_temp_word) <= 1:
        if len(list_temp_word) == 0:
            pass
        else:
            if list_temp_word[0] == ".":
                del list_temp_word[0]
    else:
        if list_temp_word[0] == ".":
            del list_temp_word[0]
        if list_temp_word[len(list_temp_word) - 1] == ".":
            del list_temp_word[len(list_temp_word) - 1]

    print("No. 4")
    print(list_temp_word)
    print("-----")

    # 5단계 빈 문자열이라면 "a"추가
    if len(list_temp_word) == 0:
        list_temp_word.append("a")

    print("No. 5")
    print(list_temp_word)
    print("-----")


    # 6단계 길이가 16자 이상이면 15자까지만 나타냄, 마지막 "."이면 제거
    if len(list_temp_word) >= 16:
        del list_temp_word[15:]
        if list_temp_word[14] == ".":
            del list_temp_word[14]

    print("No. 6")
    print(list_temp_word)
    print("-----")

    # 7단계 길이가 2자 이하면 마지막 문자를 길이가 3이 될 때까지 반복
    while len(list_temp_word) <= 2:
        list_temp_word.append(list_temp_word[len(list_temp_word) - 1])

    print("No. 7")
    print(list_temp_word)

solution("...!@BaT#*..y.abcdefghijklm")
print("---------------------")
solution("z-+.^.")
print("---------------------")
solution("=.=")
print("---------------------")
solution("123_.def")
print("---------------------")
solution(".ab......cd.")
print("---------------------")
solution("")
