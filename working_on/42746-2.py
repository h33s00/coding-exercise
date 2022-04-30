# 가장 큰 수

# 두번째 시도
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

    # 자릿수별로 리스트화
    # s = {}
    # for i, v in enumerate(s_numbers):
    #     if len(v) not in s:
    #         s[len(v)] = [v]
    #     else:
    #         s[len(v)].append(v)


# numbers = [6, 10, 2]
numbers = [0, 0, 0, 0]
# numbers = [3, 30, 34, 5, 9, 0]
# 34, 3, 30 / 34, 3, 31, / 35, 34, 3
# numbers = [9, 998]
# numbers = [7, 3999999, 3, 30, 38, 340, 389, 8]
# numbers = [9, 9, 67300000, 439825, 4385042]
print(solution(numbers))
