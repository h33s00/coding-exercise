# 프린터


# import queue


# def solution(priorities, location):
#     order = []
#     q = queue.PriorityQueue()
#     for i, v in enumerate(priorities):
#         q.put((v * -1, i))

#     for i in range(len(priorities)):
#         order.append(q.get())

#     for i in range(len(order)):
#         if order[i][1] == location:
#             return i + 1


def solution(priorities, location):
    order = []
    q = []
    for i, v in enumerate(priorities):
        q.append((v, i))  # 우선순위, 위치(고유값)

    print(q)

    while len(q) != 0:
        if q[0][0] == max(priorities):
            order.append(q[0])
            priorities.remove(q[0][0])

            print(q)
        else:
            q.append(q[0])  # 맨 뒤로 갑니다.

            print(q)
        q.remove(q[0])

    print(order)

    for i in range(len(order)):
        if order[i][1] == location:
            return i + 1


# priorities = [2, 1, 3, 2]
priorities = [1, 1, 9, 1, 1, 1]
# location = 2
location = 0
print(solution(priorities, location))
