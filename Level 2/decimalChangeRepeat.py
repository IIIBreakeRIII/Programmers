# 이진 변환 반복하기

def change_decimal(count, s):

    temp_count = 0

    for i in s:
        if i == "0":
            i = i.replace("0", "")
            count += 1

    for i in s:
        temp_count += 1

    s = s.replace("0", "")

    temp = format(len(s), "b")
    new_s = format(int(temp), 'd')

    return count, new_s

def solution(s):

    count = 0
    func_count = 0

    while s != "1":
        func_count += 1
        count, s = change_decimal(count, s)
        if s == "1":
            break
    
    return [func_count, count]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
