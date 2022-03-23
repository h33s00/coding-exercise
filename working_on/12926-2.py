def solution(s, n):
    answer = s
    low_al = list(map(chr, range(97, 123)))
    input = s.strip().split()
    print(input)

    for item in input:
        if len(item) >= 2:
            # 문자열 하나 단위로 쪼개기
            temp = ""
            for i in range(len(item)):
                new_index = low_al.index(item[i].lower()) + n
                # 인덱스 넘어가는 경우
                if new_index >= 26:
                    new_index = new_index - 26
                # 대문자인 경우
                if item.isupper() is True:
                    temp = temp + low_al[new_index].upper()
                else:
                    temp = temp + low_al[new_index]
            answer = answer.replace(item, temp)

        else:
            new_index = low_al.index(item.lower()) + n
            if new_index >= 26:
                new_index = new_index - 26
            if item.isupper() is True:
                answer = answer.replace(item, low_al[new_index].upper())
            else:
                answer = answer.replace(item, low_al[new_index])

    print(answer)

    return answer


solution("AB", 1)
solution("z", 1)
solution("a B z", 4)
solution("      A           Bz", 4)
solution("AAAA", 4)
