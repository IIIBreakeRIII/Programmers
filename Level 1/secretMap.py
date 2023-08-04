# [1차] 비밀지도

def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for i in range(n):
        answer_temp = ""
        arr1_bin.append(bin(arr1[i])[2:])
        arr2_bin.append(bin(arr2[i])[2:])
        arr1_bin[i] = ('0' * (n-len(arr1_bin[i]))) + arr1_bin[i]
        arr2_bin[i] = ('0' * (n-len(arr2_bin[i]))) + arr2_bin[i]
    
        for p in range(n):
            if arr1_bin[i][p] == '1' or arr2_bin[i][p] == '1':
                answer_temp += '#'
            elif arr1_bin[i][p] == '0' and arr2_bin[i][p] == '0':
                answer_temp += ' '
        answer.append(answer_temp)
        
    return answer
