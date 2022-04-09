# 이상한 문자 만들기


def solution(s):
    answer = s
    word = s.strip().split(" ")
    print(word)

    for item in word:
        # 임시 변수 초기화
        temp = ""
        for n in range(len(item)):
            # 짝수이거나 첫번째 문자열인 경우
            if n % 2 == 0 or n == 0:
                temp = temp + item[n].upper()
            else:
                temp = temp + item[n].lower()
        print(temp)
        answer = answer.replace(item, temp, 1)
        print(answer)

    return answer


# 테스트 케이스
# s = "   try hello      world          "
# s = " try try             try "
# s = " i Love You"
# s = " aaaa "
# s = " i "
# s = " tlqkf             w        hy        "
# s = "AAAAAAAAAAA A A A A AAAAA AAA "
# s = "A        "
# s = "try hello world strys"
# s = "tlqkf sj skgksxp dhodlfjsl wlsWK "
# s = "tlqkftoRldi"
# s = "tlqkf tlqkf tlqkf"
# s = " hello"
# s = " AAAA "
# s = " Bye bYE MY lovE "
# s = " bye bye bye bye by eee ee e   bye "
s = "    e D ee e"
a = solution(s)

# 결과값 비교
print(f"'{s}'", len(s), type(s))
print(f"'{a}'", len(a), type(a))
