usr = input().split()
s = 0 # 고유번호
for i in usr: # iterate list 'usr'
    s = s + int(i)**2
print(s%10)