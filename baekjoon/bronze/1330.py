input = input().split(" ")
a = int(input[0])
b = int(input[1])

if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")
