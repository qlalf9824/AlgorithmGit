def solution(participant, completion):
    answer = ''
    dic = {}

    for i in participant:
        if(i in dic):
            dic[i] += 1
        else:
            dic.update({i:1})

    for i in completion:
        if(dic[i] > 1):
            dic[i] -= 1
        else:
            del dic[i]
    
    name = list(dic.keys())
    answer = name[0]

    return answer

result = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
print(result)