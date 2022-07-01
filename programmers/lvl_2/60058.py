# 괄호 변환

# 균형잡힌 문자열 체크
def balanced(li):
    # 빈 문자열도 True 반환
    if li.count("(") == li.count(")"):
        return True
    else:
        return False


# 올바른 문자열 체크
def correct(li):
    # 오픈과 클로즈의 수가 같을 때,
    # 클로즈 괄호 수가 더 많아지는 순간 올바른 문자열이 될 수 없음!
    oc = 0  # 오픈 카운터
    cc = 0  # 클로즈 카운터
    for i in range(len(li)):
        if cc > oc:
            return False
        if li[i] == "(":
            oc += 1
        if li[i] == ")":
            cc += 1
    return True


def solution(p):
    if correct(p):
        return p

    # 1. 입력이 빈 문자열인 경우
    if len(p) == 0:
        return p

    else:
        # 2. 두 "균형잡힌 괄호 문자열" u, v로 분리
        li = list(p)
        i = 1
        u = li[:i]
        while not balanced(u):
            u = li[:i]
            i += 1
        v = li[i - 1 :]
        # print("U문자열: ", u)
        # print("V문자열: ", v)

        # 3. u가 올바른 괄호 문자열인 경우
        if correct(u):
            return "".join(u) + solution("".join(v))

        # 4. u가 올바른 괄호 문자열이 아닌경우
        elif not correct(u):
            vtemp = "(" + solution("".join(v)) + ")"
            utemp = u[1:-1]
            # print(utemp)
            for k in range(len(u[1:-1])):
                if utemp[k] == "(":
                    utemp[k] = ")"
                elif utemp[k] == ")":
                    utemp[k] = "("

            # print("VTEMP", vtemp)
            # print("UTEMP", utemp)
            return vtemp + "".join(utemp)
