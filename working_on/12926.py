# 시저 암호


def solution(s, n):
    lowal = list(map(chr, range(97, 123)))
    print(lowal)
    answer = s  # 원본 복사
    print(answer)
    input = s.strip().split()
    new = []

    for item in input:
        if len(item) >= 2:
            # 문자열 하나 단위로 쪼개기
            for i in range(len(item)):
                new.append(item[i])
        else:
            new.append(item)
    print(new)
    # print(f"'{answer}'")
    # print(input)

    for item in new:
        print(item)
        new_index = lowal.index(item.lower()) + n
        if new_index >= 26:
            new_index = new_index - 26

        if item.isupper() is True:
            answer = answer.replace(item, lowal[new_index].upper())
            print(answer)
        else:
            answer = answer.replace(item, lowal[new_index])

    print(f"'{answer}'")

    return answer


solution("AB", 1)
# solution("z", 1)
# solution("a B z", 4)
# solution("      A           Bz", 4)
# solution("AAAA", 4)
