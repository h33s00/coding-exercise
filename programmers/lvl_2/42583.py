# 다리를 지나는 트럭


def solution(bridge_length, weight, truck_weights):
    t = 0
    on = []
    off = []
    wait = truck_weights[:]

    while len(off) != len(truck_weights):
        # print(f"시간 ::: {t}")
        # print(f"다 건넜다 ! ::: {off}")
        # print(f"빵빵 ! 지나갑니다 ::: {on}")
        # print(f"기다리는 트럭 ::: {wait}")
        for truck in on:
            truck[1] -= 1
        for truck in on:
            if truck[1] == 0:
                on.pop(0)
                off.append(truck[0])

        #                 올릴 수 있는 경우

        if len(wait) != 0:
            temp = [item[0] for item in on]
            if (sum(temp) + wait[0]) <= weight and len(on) < bridge_length:
                on.append([wait.pop(0), bridge_length])

        t += 1

    return t
