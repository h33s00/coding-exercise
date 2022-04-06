# 자연수 뒤집어 배열로 만들기


def solution(n):
    return list(map(int, str(n)[::-1]))


print(solution(4652352352))
