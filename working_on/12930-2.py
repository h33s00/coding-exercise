# 이상한 문자 만들기
# 최적의 풀이...


def toWeirdCase(s):
    return " ".join(
        map(
            lambda x: "".join(
                [a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]
            ),
            s.split(" "),
        )
    )


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
a = toWeirdCase(s)

# 결과값 비교
print(f"'{s}'", len(s), type(s))
print(f"'{a}'", len(a), type(a))
