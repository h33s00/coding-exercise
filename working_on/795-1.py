# INPUT #

# # 첫째 줄에 물약의 종류 N이 주어진다.
# n = int(input())
# # 둘째 줄에 물약의 가격이 공백을 사이에 두고 주어진다.
# c = list(map(int, input().split()))
# # 다음 줄부터, 물약 할인 정보가 N개 주어진다.
# discount = {}  # 할인 정보를 담는 배열
# for a in range(n):
#     p = int(input())  # 할인횟수
#     discount[a] = []
#     for i in range(p):
#         # [a번째 물약을 사면 (key): 물약이름, 할인금액]
#         # 주의! 나중에 물약이름에서 1빼서 인덱스와 맞춰주어야 함!
#         discount[a].append(list(map(int, input().split())))
#         print(discount)

# TEST #
c = [10, 15, 20, 25]
discount = {0: [[3, 10], [2, 20]], 1: [], 2: [[4, 10]], 3: [[1, 10]]}

# 정답이 들어갈 변수
total_cost = 0

sd = dict(sorted(discount.items(), key=lambda x: len(x[1]), reverse=True))
print(sd)


# print(total_cost)
# print(c)
# 가장 저렴하게 모든 종류의 물약을 하나씩 구매하는 법:
# 할인 횟수가 높은 물약 순서대로 구매.
for each in sd:
    # 물약 구매
    total_cost += c[each]
    # 할인 적용
    for i in range(len(sd[each])):
        print(sd[each][i])
        if c[sd[each][i][0] - 1] <= sd[each][i][1]:
            c[sd[each][i][0] - 1] = 1
        else:
            c[sd[each][i][0] - 1] -= sd[each][i][1]
        print(c)

print(total_cost)
