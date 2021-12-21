import sys

num = int(sys.stdin.readline())
num_list = map(int, sys.stdin.readline().split())

for n in list(num_list):
    i = 2
    if(n == 1):
        num -= 1
        continue
    while(i < n):
        if(n % i == 0):
            num -= 1
            break
        i += 1

print(num)