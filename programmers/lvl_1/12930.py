# 이상한 문자 만들기


def strangify(word):
    new_word = ""
    for i in range(len(word)):
        if i % 2 == 0 or i == 0:
            new_word += word[i].upper()
        else:
            new_word += word[i].lower()
    return new_word


def solution(s):
    answer = ""
    pieces = []
    temp = []
    for i in range(len(s)):
        print(temp)
        print(pieces)
        if s[i] == " ":
            if len(temp) != 0:
                pieces.append("".join(temp))
                temp = []
            pieces.append(s[i])

        else:
            temp.append(s[i])
            if i == len(s) - 1:
                pieces.append("".join(temp))

    for item in pieces:
        if item == " ":
            answer += item
        else:
            answer += strangify(item)

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
