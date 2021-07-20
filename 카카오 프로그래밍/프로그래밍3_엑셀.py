def solution(n, k, cmd):
    answer = ['O'] * n
    delete = []

    for i in cmd:
        if(i[0] == 'U'):
            k -= int(i[2])
        elif(i[0] == 'D'):
            k += int(i[2])
        elif(i[0] == 'C'):
            answer[k] = 'X'
            delete.append(k)
            if(k == (n-1)):
                k -= 1
            n -= 1
        elif(i[0] == 'Z'):
            p = delete.pop()
            answer[p] = 'O'
            if(p<= k):
                k += 1    
            n += 1

    answer = ''.join(answer)

    return answer

p = solution(8, 2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
print(p)