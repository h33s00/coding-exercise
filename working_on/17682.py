def solution(dartResult):
    # 한 세트씩 자르기

    second, third = 0, 0
    number = list(map(str, range(0, 11)))
    # print(number)
    for i in range(len(dartResult)):
        # print(i)
        if i != 0 and dartResult[i] in number:
            if second == 0:
                if
                second = i
            elif third == 0:
                third = i

    sets = [dartResult[:second], dartResult[second:third], dartResult[third:]]

    # calc = []

    # # 점수, 보너스, 옵션으로 자르기

    # for each in sets:
    #     # 10인 경우와 아닌경우
    #     if each[:2] in number:
    #         n = int(each[:2])
    #         bonus = each[2]
    #         if each[2] == each[-1]:  # 옵션이 없다면
    #             calc.append([n, bonus])
    #         else:
    #             calc.append([n, bonus, each[-1]])

    #     else:
    #         n = int(each[0])
    #         bonus = each[1]
    #         if each[1] == each[-1]:  # 옵션이 없다면
    #             calc.append([n, bonus])
    #         else:
    #             calc.append([n, bonus, each[-1]])

    # print(sets)
    # print(calc)

    # # 총 점수 계산하기

    # score = []
    # option = []

    # for i in range(3):
    #     if len(calc[i]) == 3:  # 옵션이 있다면
    #         if calc[i][-1] == "*":
    #             option.append([i, 2])
    #         elif calc[i][-1] == "#":
    #             option.append([i, -1])

    #     if calc[i][1] == "S":
    #         score.append(calc[i][0])
    #     if calc[i][1] == "D":
    #         score.append((calc[i][0]) ** 2)
    #     if calc[i][1] == "T":
    #         score.append((calc[i][0]) ** 3)

    # print(option)
    # if len(option) != 0:
    #     for item in option:
    #         if item[1] == 2:
    #             score[item[0]] *= 2
    #             if item[0] != 0:
    #                 score[item[0] - 1] *= 2
    #         if item[1] == -1:
    #             score[item[0]] *= -1

    # print(score)

    # return sum(score)
    return sets


dartResult1 = "1S2D*3T"
dartResult2 = "1D2S#10S"
dartResult3 = "1D2S0T"
dartResult4 = "1S*2T*3S"
dartResult5 = "1D#2S*3S"
dartResult6 = "1T2D3D#"
dartResult7 = "1D2S3T*"
dartResult8 = "0D#0S0S*"
dartResult9 = "10D4S10D"
a = solution(dartResult9)
print(a)


# 10에대한처리하기!!!!!!!!!!!!
# 함수화하기
# 효율적 풀이
