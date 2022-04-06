# 문자열 내 p와 y의 개수


def solution(s):
    input = list(s.lower())  # 대소문자 구분 안함!
    if input.count("p") == input.count("y") == 0:
        answer = True
    elif input.count("p") == input.count("y") != 0:
        answer = True
    else:
        answer = False

    return answer


print(solution("pPoooyY"))
print(solution("Pyy"))
