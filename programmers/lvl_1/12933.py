# 정수 내림차순으로 배치하기


def solution(n):
    input = str(int(n))
    numlist = []
    for i in range(len(input)):
        numlist.append(input[i])
    numlist.sort(reverse=True)
    # for item in numlist:
    #     answer += item
    return int("".join(numlist))


print(solution(118372))
# print(type(solution(8000000000)))
print(solution(1))
