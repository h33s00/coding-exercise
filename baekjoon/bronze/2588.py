a = int(input())
b = list(input())

for i in range(1, 4):
    print(a * int(b[-i]))
print(a * int("".join(b)))
