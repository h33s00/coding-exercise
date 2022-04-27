# 약수의 개수와 덧셈


def numofdivisor(n):
    if n == 1:
        return 1
    else:
        answer = 2  # 1과 자기자신 포함.
        for div in range(2, n):
            if n % div == 0:
                # print(div)
                answer += 1
        return answer


# print(numofdivisor(14))


def solution(left, right):
    answer = 0
    between = list(range(left, right + 1))
    for each in between:
        # 약수의 개수가 짝수라면
        if numofdivisor(each) % 2 == 0:
            answer += each
        else:
            answer -= each

    return answer


# left, right = 13, 17
# left, right = 24, 27
left, right = 1, 1
a = solution(left, right)
print(a)
