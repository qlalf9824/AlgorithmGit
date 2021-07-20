import sys

while(1):
    a =  int(sys.stdin.readline())
    if(a == 0): break
    result = 0
    num = 0

    num_list = list(map(int, str(a)))
    l = len(num_list)
    for i in range(l):
        num = num_list[i]
        for j in range(1,l - i + 1):
            num *= j
        result += num

    print(result)
    