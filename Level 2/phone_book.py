# 전화번호 목록

def solution(phone_book):
    
    phone_book.sort()
    
    for index in range(len(phone_book) - 1):
        if phone_book[index] in phone_book[index + 1][:len(phone_book[index])]:
            return False
    
    return True

def solution_2(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            print(temp)
            if temp in hash_map and temp != phone_number:
                answer = False
                print(temp, answer)
    return answer

print(solution_2(["12","123","1235","567","88"]))
