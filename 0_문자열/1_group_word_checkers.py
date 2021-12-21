import sys

num = int(sys.stdin.readline())

result = num

for s in range(num):
    s = sys.stdin.readline()
    for idx in range(len(s)-1):
        if(s[idx] != s[idx+1] and s[idx] in s[idx+1:]):
            result -= 1
            break;

print(result)

##https://www.acmicpc.net/problem/1316