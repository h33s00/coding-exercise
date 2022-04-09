# 없는 숫자 더하기


def solution(numbers):
    return sum(list(set(range(0, 10)) - set(numbers)))


numbers = [1, 2, 3, 4, 6, 7, 8, 0]
print(solution(numbers))
