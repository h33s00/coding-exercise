# 소수 찾기


from itertools import permutations


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


def solution(numbers):
    count = 0
    candidates = []
    numlist = list(numbers)

    for i in range(1, len(numlist) + 1):
        p = permutations(numlist, i)
        for each in p:
            n = int("".join(each))
            # print(n)
            if n not in candidates:
                candidates.append(int("".join(each)))

    # print(candidates)

    for item in candidates:
        if isPrime(item) is True:
            count += 1
    return count


numbers = "17"
# numbers = "011"
print(solution(numbers))
