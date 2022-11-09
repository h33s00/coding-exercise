# 1트 - 시간 복잡도를 고려해본 코드 (나름)
def solution(s):
    min, max = None, None
    temp = ""
    for i, letter in enumerate(s):
        if i == len(s) - 1 or letter == " ":
            if i == len(s) - 1:
                temp += letter
            temp_num = int(temp)
            if min == None or max == None:
                min, max = (
                    temp_num,
                    temp_num,
                )
            elif int(temp) < min:
                min = temp_num
            elif int(temp) > max:
                max = temp_num
            temp = ""
        else:
            temp += letter

    return str(min) + " " + str(max)


# 2트 - 머릿속에 떠올랐던 풀이... 이게 더 빠르다 ^^
def solution(s):
    s_list = list(map(int, s.split(" ")))
    return str(min(s_list)) + " " + str(max(s_list))


# s = "1 2 3 4"  # "1 4"
# s = "-1 -2 -3 -4"  # "-4 -1"
s = "-1 -1"  # "-1 -1"
print(solution(s))
