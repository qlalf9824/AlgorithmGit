from array import array

num = int(input())
d_list = []
result = [1 for i in range(num)]

for i in range(num):
    info = list(map(int, input().split()))
    d_list.append(info)

for i in range(num):
    for j in d_list:
        if(d_list[i][0] < j[0] and d_list[i][1] < j[1]):
             result[i] += 1


for i in result:
    print(i, "", end="")
