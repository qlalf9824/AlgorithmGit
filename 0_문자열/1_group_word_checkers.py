num = int(input())
s_list = [input() for _ in range(num)]

result = num

for s in s_list:
    for idx in range(len(s)-1):
        if(s[idx] != s[idx+1] and s[idx] in s[idx+1:]):
            result -= 1
            break;

print(result)

##https://www.acmicpc.net/problem/1316