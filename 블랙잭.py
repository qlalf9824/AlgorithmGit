a, max_num = map(int, input().split())
num_list = list(map(int, input().split()))

flag = True
i, j, k = 0, 0, 0
s = 0
result = 0

while(flag and i < a):
    s = 0
    s += num_list[i]
    j = i + 1
    while(flag and j < a):
        s += num_list[j]
        k = j + 1
        while(flag and k < a):
            s += num_list[k]
            if(s == max_num):
                flag = False
                result = s
                break
            elif(s > result and s < max_num):
                result = s
            s -= num_list[k]
            k += 1
        s -= num_list[j]
        j += 1
    i += 1

print(result)