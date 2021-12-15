import math
import itertools

def solution(numbers):
    answer = 0

    n = 10 ** len(numbers)
    #소수
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1


    num_list = []
    # 만들 수 있는 숫자
    for j in range(1, len(numbers)+1):
        iter = itertools.permutations(numbers, j)
        li = list(set(iter))

        for i in range(len(li)):
            li[i] = list(li[i])
            s = "".join(li[i])
            num_list.append(int(s))

    num_list = list(set(num_list))

    #print(num_list)

    for i in num_list:
        if(i == 0 or i == 1):
            continue
        if(array[i] == True):
            answer += 1

    return answer


numbers = "011"
print(solution(numbers))

