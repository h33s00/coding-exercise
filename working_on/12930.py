# 이상한 문자 만들기

def solution(s):
    answer = ''
    word = s.strip().split()
    
    for item in word:
        temp = ''
        for n in range(len(item)):
            if n%2 == 0:
                temp = temp + item[n].upper()
            else:
                temp = temp + item[n].lower()
        if temp.lower() in s:
            s = s.replace(temp.lower(), temp)
    
    answer = s
    return answer

# print(solution("try hello world"))
# print(solution("   try hello      world          "))