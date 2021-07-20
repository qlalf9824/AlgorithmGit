num = int(input())
s = input()

result = 0

for i in range(num):
    h = ord(s[i]) - 96
    result += h * (31 ** i)

print(result % 1234567891)

