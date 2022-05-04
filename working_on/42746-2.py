# 가장 큰 수

# 두번째 시도
# 앞자리가 같은 경우 양옆의 수를 비교


def solution(numbers):
    if sum(numbers) == 0:
        return "0"

    s_numbers = list(map(str, numbers))
    s_numbers.sort(
        key=lambda x: (int(x[0]), len(x)),
        reverse=True,
    )

    print(s_numbers)

    for i in range(len(s_numbers) - 1):
        a = s_numbers[i]
        b = s_numbers[i + 1]
        if int(a + b) <= int(b + a):
            s_numbers[i] = b
            s_numbers[i + 1] = a

    print(s_numbers)

    return "".join(s_numbers)


# 1-9 테스트케이스 실패

# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9, 0]
numbers = [30, 3021]
# numbers = [15, 151]
# numbers = [0, 0, 70]
# numbers = [0, 0, 0, 0]
# numbers = [0, 0, 1, 0, 0]
# numbers = [9, 998]

print(solution(numbers))
