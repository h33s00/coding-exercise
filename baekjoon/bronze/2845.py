mine = input().split()
news = input().split()
ans = int(mine[0]) * int(mine[1]) # 정답
diff = []
for i in news: # 뉴스와 정답의 차
    diff.append(int(i) - ans)
diff = list(map(str, diff)) # int에서 str으로의 변환
print(' '.join(diff)) #list를 공백을 이용해서 str으로 변환