# 하샤드 수

def solution(x):
    answer = True
    digit = []
    for i in str(x):
        digit.append(int(i))
    k = sum(digit)
    if x%k == 0:
        answer = True
    else:
        answer = False
    return answer