# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    num = x
    for i in range(n):
        answer.append(num)
        num = num + x
    return answer