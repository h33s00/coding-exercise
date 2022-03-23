# 이상한 문자 만들기


def solution(s):
    answer = s  # 원본 복사
    word = s.strip().split(" ")

    # 이상한 공백도 들어가 버려서 그것 정리 ...
    new = []
    for item in word:
        if len(item) >= 1:
            new.append(item)

    # print(word)
    # print(new)

    for item in new:
        # 임시 변수 초기화
        temp = ""
        for n in range(len(item)):
            # 짝수이거나 첫번째 문자열인 경우
            if n % 2 == 0 or n == 0:
                temp = temp + item[n].upper()
            else:
                temp = temp + item[n].lower()
        # print(temp)
        answer = answer.replace(item, temp)

    return answer


# 테스트 케이스
s = "   try hello      world          "
# s = " i Love You"
# s = " i "
# s = " tlqkf             w        hy        "
# s = "tlqkf sj skgksxp dhodlfjsl wlsWK "
# s = "tlqkf                                                    toRLdi dhodl fo    "
# s = "tlqkftoRldi"
# s = "tlqkf tlqkf tlqkf"
# s = " hello"
a = solution(s)

# 결과값 비교
print(f"'{s}'", len(s), type(s))
print(f"'{a}'", len(a), type(a))
