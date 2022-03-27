# 시저 암호


def solution(s, n):
    answer = ""
    for i in range(len(s)):
        # print(f"여기 '{s[i]}'입니다.")
        # 공백
        if s[i] == " ":
            # print(f"{i}는 빈칸입니다.")
            answer += " "
        else:
            nn = ord(s[i]) + n
            # 대문자
            if s[i].isupper():
                print(i, s[i], ord(s[i]), nn)
                if nn > 90:
                    nn = 64 + (nn - 90)
                    print(nn, chr(nn))
            # 소문자
            else:
                print(i, s[i], ord(s[i]), nn)
                if nn > 122:
                    nn = 96 + (nn - 122)
                    print(nn, chr(nn))

            answer += chr(nn)

    print(f"답은 '{answer}'입니다.")
    return answer


# solution("AB", 1)
# solution("z", 1)
# solution("a b ", 1)
# solution("a B z", 20)
solution("      A           Bz", 25)
# solution("AAAA", 4)
# solution("AaZz", 25)
# solution("bC", 25)
