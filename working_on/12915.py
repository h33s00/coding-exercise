# 문자열 내 마음대로 정렬하기


# def solution(strings, n):
#     answer = []
#     my_std = []

#     # my_std = list(map(strings[i], v[n], ccv]))

#     for i, v in enumerate(strings):
#         my_std.append([i, v[n], v])

#     print(my_std)

#     my_std.sort(key=lambda x: (x[1], x[2]))
#     # print(my_std)

#     for each in my_std:
#         answer.append(strings[each[0]])

#     return answer


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


# strings, n = ["sun", "bed", "car"], 1
strings, n = ["abce", "abcd", "cdx"], 2
a = solution(strings, n)
print(a)
