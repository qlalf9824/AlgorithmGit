import sys

num = int(sys.stdin.readline())

first = 0
second = 1
if(num == 0): second = 0
for _ in range(1, num):
    first, second = second, first + second

print(second)

# https://www.acmicpc.net/problem/10870