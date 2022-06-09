# import re

# a = "100-200*300-500+20"
# b = re.split("\+|-|\*", a)
# # + 와 * 는 특별한 문자열이기 때문!
# print(b)

ex = [[1, 0, 0, 0, 1], [3, 2, 0, 0, 1], [1, 0, -2, -2, 1], [3, 2, 0, 0, 1]]
answer = 0
for each in ex:
    answer += len([x for x in each if x > 0])
    print(answer)
