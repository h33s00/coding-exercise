# 이상한 문자 만들기


# def solution(s):
#     answer = ""
#     word = s.strip().split()
#     new = []
#     for item in word:
#         # 임시 변수 초기화
#         temp = ""
#         for n in range(len(item)):
#             # 짝수이거나 첫번째 문자열인 경우
#             if n % 2 == 0 or n == 0:
#                 temp = temp + item[n].upper()
#             else:
#                 temp = temp + item[n].lower()
#         new.append(temp)

#     for i in range(len(word)):
#         if s[i] == " ":
#             answer += " "
#         else:
#             for item in new:
#                 for k in range(len(item)):
#                     answer += item[k]

#     return answer


def solution(s):
    answer = ""
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
        else:
            for k in range(i, len(s)):
                if s[k] == " ":
                    print(s[i:k])
                    break
    return answer


# 테스트 케이스
# s = "   try hello      world          "
# s = " try try             try "
# s = " i Love You"
# s = " aaaa "
# s = " i "
# s = " tlqkf             w        hy        "
# s = "AAAAAAAAAAA A A A A AAAAA AAA "
# s = "A "
s = "try hello world strys"
# s = "tlqkf sj skgksxp dhodlfjsl wlsWK "
# s = "tlqkftoRldi"
# s = "tlqkf tlqkf tlqkf"
# s = " hello"
a = solution(s)

# 결과값 비교
print(f"'{s}'", len(s), type(s))
print(f"'{a}'", len(a), type(a))
