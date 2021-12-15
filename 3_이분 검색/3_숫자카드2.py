from collections import Counter

a = int(input())
numList = Counter(input().split())

b = int(input())
mList = list(input().split())

print(numList)

for i in mList:
    print(numList[i], end=" ")
