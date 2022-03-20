#1550-1
hex = input()
# print(len(hex)) #몇 자리수?
result = 0
b = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
for digit in range(len(hex)):
    if hex[digit] in b:
        result = result + (b[hex[digit]]*pow(16,(len(hex)-digit-1)))
    else:
        result = result + (int(hex[digit])*pow(16,(len(hex)-digit-1)))
    
print(result)