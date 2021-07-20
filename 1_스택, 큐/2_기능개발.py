import math

def solution(progresses, speeds):
    answer = []
    before = 0
    c = -1

    for i in range(len(progresses)):
       
        temp = 100 - progresses[i] 
        temp /= speeds[i]
        temp = math.ceil(temp)

        if(before >= temp):
            answer[c] += 1
        else:
            answer.append(1)
            before = temp
            c += 1

        
        
        print("temp : ", temp)

    return answer


pro =   [93, 30, 55, 60, 40, 65]
sp =  [1, 30, 5 , 10, 60, 7]

result = solution(pro, sp)
print(result)