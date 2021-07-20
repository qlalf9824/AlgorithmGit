a,b = input().split()
b = int(b)

num = set(['0','1','2','3','4','5','6','7','8','9'])
result = 0
a_len = len(a)
for i in range(a_len):
    if(a[i] in num):
        n = ord(a[i]) - 48
    else:
        n = ord(a[i]) - 55

    for j in range(1, a_len - i):
        n *= b
    result += n

print(result)
