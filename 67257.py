# 수식 최대화

import re
import queue
from itertools import permutations


def calculator(ex, priority):
    print(ex, "시작")
    while not priority.empty():
        op = priority.get()[1]
        while ex.count(op) != 0:
            opi = ex.index(op)
            print("연산자: ", op, opi)
            # 연산
            if op == "+":
                ex[opi] = int(ex[opi - 1]) + int(ex[opi + 1])
                ex[opi - 1] = "None"
                ex[opi + 1] = "None"
            elif op == "*":
                ex[opi] = int(ex[opi - 1]) * int(ex[opi + 1])
                ex[opi - 1] = "None"
                ex[opi + 1] = "None"
            elif op == "-":
                ex[opi] = int(ex[opi - 1]) - int(ex[opi + 1])
                ex[opi - 1] = "None"
                ex[opi + 1] = "None"
            print(ex)
            ex = list(filter(("None").__ne__, ex))

    print(ex, "끝")
    return int(ex[0])


def solution(expression):
    candidates = []
    operands = []

    # split using multiple delimiter
    e = re.split("(\+|\*|-)", expression)

    # 있는 연산자 모음 :)
    if "+" in e:
        operands.append("+")
    if "*" in e:
        operands.append("*")
    if "-" in e:
        operands.append("-")

    print(operands)

    p = permutations(operands, len(operands))

    for each in p:
        ex = e[:]
        print(each, "이 조합은?")
        # create all possible priority queues
        q = queue.PriorityQueue()
        for i in range(1, len(operands) + 1):
            q.put((i, each[i - 1]))
        candidates.append(abs(calculator(ex, q)))

    return max(candidates)


expression = "100-200*300-500+20"
# expression = "50*6-3*2"
# expression = "0-70-80*20"
# expression = "50+1-4"
# expression = "2*2*2*2*2-2*2*2"
print(solution(expression))


# 배운 점: 리스트에 remove 등의 함수를 쓴다면 clone은 필수!,
# 만약 리스트에서 값으로 지워주면 중복 수 처리가 안된다!!!
# 해당 인덱스 값을 임의값으로 변경 후 일괄 처리 (filter 함수 이용)
