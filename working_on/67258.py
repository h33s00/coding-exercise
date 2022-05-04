def solution(gems):
    gemtypes = set(gems)
    # len(gemtypes)~len(gems) 길이의 구간 확인 필요

    for i in range(len(gemtypes), len(gems) + 1):
        for k in range(len(gems) - i + 1):
            # print(k, k + i)
            c = gems[k : k + i]
            if set(c) == gemtypes:
                # print(c)
                return [k + 1, k + i]


# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]


print(solution(gems))
