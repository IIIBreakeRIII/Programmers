def solution(s):
    if len(s) % 2 == 1:         #홀수일 경우
        return s[len(s) // 2]
    
    else:                        #짝수일 경우
        return s[(len(s) // 2 - 1) : (len(s) // 2 + 1) ]

solution ("abcde")