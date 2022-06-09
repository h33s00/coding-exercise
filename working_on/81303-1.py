# 표 편집
# 첫번째 시도...
def solution(n, k, cmd):
    table = list(range(0, n))
    pointer = k
    recently_deleted = 0
    end = len(table) - 1

    for each in cmd:
        print("table: ", table)
        print("pointer is at: ", pointer)
        print("the command is: ", each)
        print("-------------------------------")

        if len(each) == 1:
            # 삭제
            if each == "C":
                table[pointer] = -1
                recently_deleted = pointer
                # 포인터의 이동
                if recently_deleted == end:
                    if table[pointer - 1]:
                        pointer -= 1
                    else:
                        pointer = move("U", 1, pointer, table)
                        if table[pointer] == -1:
                            pointer += 1
                else:
                    if table[pointer + 1]:
                        pointer += 1
                    else:
                        pointer = move("D", 1, pointer, table)
                        if table[pointer] == -1:
                            pointer += 1

            # 복구
            if each == "Z":
                table[recently_deleted] = "BACK"

        else:
            # UP 또는 DOWN
            dir, num = each.split(" ")
            pointer = move(dir, int(num), pointer, table)
            if table[pointer] == -1:
                pointer += 1

    answer = ""
    for each in table:
        if each == -1:
            answer += "X"
        else:
            answer += "O"

    return answer


def move(dir, int, pointer, table):
    cnt = 0
    if dir == "U":
        while cnt != int:
            if table[pointer] != -1:
                cnt += 1
            pointer -= 1

    if dir == "D":
        while cnt != int:
            if table[pointer] != -1:
                cnt += 1
            pointer += 1

    return pointer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
# cmd = ["D 2", "C", "U 3"]
# UP, DOWN, CUT, Z
print(solution(n, k, cmd))
