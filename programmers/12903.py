# 가운데 글자 가져오기

def solution(s):
    answer = ''
    # 기준
    std = len(s)//2
    # 짝수인 경우
    if len(s)%2 == 0:
        answer = s[:std][-1] + s[std:][0]
    # 홀수인 경우
    else:
        answer = s[std]
    return answer