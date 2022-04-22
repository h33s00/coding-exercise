# a = [4, 4, 5, 2, 1]

# print(a.count(4))

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# new = list(map(lambda x: format(x, "b"), arr1))
# new = list(map(lambda x: "0" + x if (len(x) < n) else x, new))

# print(new)

# # 대문자 65부터 90까지
# up = list(map(chr, range(65, 91)))
# # 소문자 97부터 123까지
# low = list(map(chr, range(97, 123)))

# print(chr(65))
# print(chr(90))

# print(chr(97))
# print(chr(122))
# print("C".islower())
# print(up[-2])


for i in range(5):
    for k in range(i + 1, 5):
        print(i, k)
