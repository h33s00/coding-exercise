# 폰켓몬


def solution(nums):
    answer = 0
    sel = len(nums) // 2
    max = len(list(set(nums)))
    # 고르는 수가 종류의 수보다 작거나 같다면
    if sel <= max:
        answer = sel
    # 고르는 수가 종류의 수보다 크다면
    else:
        answer = max

    # print(sel, max)

    return answer


# nums = [3, 1, 2, 3]
nums = [3, 3, 3, 2, 2, 4]
# nums = [3, 3, 3, 2, 2, 2]
# nums = [3, 3, 3, 3, 3, 2, 3, 3]

print(solution(nums))
