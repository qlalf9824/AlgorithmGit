def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        num = arr1[i] | arr2[i]
        print("arr1", bin(arr1[i]))
        print("arr2", bin(arr2[i]))
        print(bin(num))

        num = bin(num)
        num = num[2:]
        num = num.replace('0',' ').replace('1','#')

        if(len(num) != n):
            a = ' ' * (n - len(num))
            a += num
        else:
            a = num
        answer.append(a)

    return answer


answer = solution(6,[46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])
print(answer)