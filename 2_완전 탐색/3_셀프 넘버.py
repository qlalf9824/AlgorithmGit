list = []

for j in range(1, 10001):
    if(j in list):
        continue;
    print(j)
    start = j
    while(1):
        s = str(start)
        result = 0
        for i in s:
            result += int(i)
        result += start

        if(result > 100001 or result in list):
            break;

        list.append(result)
        start = result
