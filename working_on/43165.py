# 타겟 넘버

from itertools import product


def solution(numbers, target):

    # 타겟이 배열안의 수가 모두 양수일때의 합보다도 크다면,
    # 조건을 만족시키는 조합은 없다.
    if target > sum(numbers):
        return 0

    # 경우의 수 카운트
    answer = 0

    # -1, 1 을 numbers의 개수와 같은 조합을 만든다.
    # 예) [-1, 1, 1, -1]

    p = product([-1, 1], repeat=len(numbers))

    for each in p:
        # print(each)
        total = 0

        for i in range(len(numbers)):
            total += each[i] * numbers[i]

        if total == target:
            answer += 1

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
# numbers = [4, 1, 2, 1]
# target = 4


print(solution(numbers, target))
