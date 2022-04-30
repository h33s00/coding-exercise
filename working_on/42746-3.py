# 가장 큰 수

# 세번째 시도
def solution(numbers):
    if sum(numbers) == 0:
        return "0"

    s_numbers = list(map(str, numbers))

    # 자릿수별로 리스트화
    s = {}
    for i, v in enumerate(s_numbers):
        if len(v) not in s:
            s[len(v)] = [v]
        else:
            s[len(v)].append(v)

    return s


# numbers = [6, 10, 2]
# numbers = [0, 0, 0, 0]
# numbers = [0, 0, 1, 0, 0]
# numbers = [15, 151]
numbers = [3, 33, 333, 3333, 39, 3]
# numbers = [10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = [3, 30, 34, 5, 9, 0]
# 34, 3, 30 / 34, 3, 31, / 35, 34, 3
# numbers = [9, 998]
# numbers = [7, 1000, 3, 30, 38, 340, 389, 8]
# numbers = [9, 9, 673, 439, 438]
print(solution(numbers))
