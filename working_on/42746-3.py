# 가장 큰 수

# 세번째 시도
# 문자열을 반복한 후 자르는 방법


def solution(numbers):
    if sum(numbers) == 0:
        return "0"

    s_numbers = list(map(str, numbers))

    s_numbers.sort(
        key=lambda x: int((x * 4)[:4]),
        reverse=True,
    )

    return "".join(s_numbers)


# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9, 0]
numbers = [30, 3021]
# numbers = [15, 151]
# numbers = [0, 0, 70]
# numbers = [0, 0, 0, 0]
# numbers = [0, 0, 1, 0, 0]
# numbers = [9, 998]

print(solution(numbers))
