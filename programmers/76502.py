# 음양 더하기


def solution(absolutes, signs):
    actual = []
    for i in range(len(absolutes)):
        if signs[i] is False:
            actual.append(absolutes[i] * -1)
        else:
            actual.append(absolutes[i])
    answer = sum(actual)
    return answer


print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))
