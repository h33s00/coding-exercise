# 소수 만들기

from itertools import combinations


def isPrime(n):
    if n == 2:
        return True
    elif n == 3:
        return True
    for k in range(2, (n // 2) + 1):
        # print(f"{n}%{k}")
        if n % k == 0:
            # print(f"{n}은 소수가 아닙니다!")
            return False
        else:
            if k == (n // 2):
                # print(f"{n}은 소수입니다.")
                return True


# print(isPrime(11))


def solution(nums):
    answer = 0
    combi = combinations(nums, 3)
    for each in combi:
        # print(each, sum(each))
        if isPrime(sum(each)) is True:
            answer += 1

    return answer


# nums = [1, 2, 3, 4]
nums = [1, 2, 7, 6, 4]
a = solution(nums)
print(a)
