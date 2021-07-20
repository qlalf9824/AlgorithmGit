def solution(answers):
    
    supoja1 = [1,2,3,4,5]
    supoja2 = [2,1,2,3,2,4,2,5]
    supoja3 = [3,3,1,1,2,2,4,4,5,5]

    collect = [0,0,0]
    
    for i in range(len(answers)):

        if(answers[i] == supoja1[i%len(supoja1)]):
            collect[0] += 1
        if(answers[i] == supoja2[i%len(supoja2)]):
            collect[1] += 1
        if(answers[i] == supoja3[i%len(supoja3)]):
            collect[2] += 1
    

    answer = [i+1 for i in range(3) if max(collect) == collect[i]]

    return answer


answers = [1,2,3,4,5]
print(solution(answers))