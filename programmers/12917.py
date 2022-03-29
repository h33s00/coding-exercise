# 문자열 내림차순으로 배치하기


def solution(s):
    temp = []
    for item in s:
        temp.append(ord(item))
    temp.sort(reverse=True)
    answer = list(map(chr, temp))
    return "".join(answer)


print(solution("Zbcdefg"))
