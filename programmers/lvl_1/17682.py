# 다트게임


def to_set(dartResult):
    # "1S2D*3T" 를 "1S/2D*/3T"로 잘라주는 함수
    # 자르는 포인트는 2개 존재하게 된다. 이를 '/'로 표시.
    second_bar, third_bar = 0, 0
    # 1부터 10까지의 숫자 문자열이 들어있는 배열
    number = list(map(str, range(0, 11)))
    for i in range(len(dartResult)):
        # 첫번째 문자열은 무조건 숫자이니 '/'가 될 수 없다.
        if i != 0 and dartResult[i] in number:
            # 직전 문자열도 숫자였다면 '10'이다.
            if dartResult[i - 1] in number:
                pass
            else:
                # 1-9까지의 숫자이다.
                # 포인트2가 갱신되지 않았다면,
                if second_bar == 0:
                    second_bar = i
                # 포인트2가 갱신된 상태이며, 포인트3이 갱신되지 않았다면
                elif third_bar == 0:
                    third_bar = i

    # 각 배열당 [점수, 보너스, 옵션] 으로 표시
    return [
        list(dartResult[:second_bar]),
        list(dartResult[second_bar:third_bar]),
        list(dartResult[third_bar:]),
    ]


def to_score(sets):
    # 세트 단위의 문자열로 나뉜 것을 점수로 바꿔주는 함수
    score = [0, 0, 0]
    bonus = [None, "S", "D", "T"]
    # 1-3 중 n번째 set에 대해,
    for n, set in enumerate(sets):
        # 10인경우 합쳐준다. 길이가 줄어든다.
        if set[0] == "1" and set[1] == "0":
            set[0] = "10"
            del set[1]
        # print(set)

        score[n] = int(set[0]) ** (bonus.index(set[1]))

        # 옵션 있는 경우 !
        if len(set) == 3:
            # 스타상
            if set[2] == "*":
                score[n] *= 2
                # 첫 번째 기회가 아닌 경우,
                if n != 0:
                    score[n - 1] *= 2
            # 아차상
            elif set[2] == "#":
                score[n] *= -1
    return score


def solution(dartResult):
    sets = to_set(dartResult)
    print(sets)
    score = to_score(sets)
    print(score)
    return sum(score)


dartResult1 = "1S2D*3T"
dartResult2 = "1D2S#10S"
dartResult3 = "1D2S0T"
dartResult4 = "1S*2T*3S"
dartResult5 = "1D#2S*3S"
dartResult6 = "1T2D3D#"
dartResult7 = "1D2S3T*"
dartResult8 = "0D#0S0S*"
dartResult9 = "10D4S10D"
a = solution(dartResult2)
print(a)
