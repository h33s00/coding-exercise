# 두번째 시도
# 슬라이딩 윈도우!
def solution(gems):
    gemtypes = set(gems)
    gemlength = len(gemtypes)
    print(gemtypes)

    for i in range(len(gems)):
        for k in range(i, i + gemlength):
            print(gems[i:k])


# 테스트케이스 11, 14 실패, 효율성 0점

# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]


print(solution(gems))
