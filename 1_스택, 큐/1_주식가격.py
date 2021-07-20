def solution(prices):
    answer = []
    
    p_len = len(prices)
    print(p_len)
    for i in range(p_len):
        c = 0
        for j in range(i+1, p_len):
            c += 1
            if(prices[i] > prices[j]):
                break
            
        answer.append(c)
        

    return answer



price = [1, 2, 3, 2, 3]

result = solution(price)

print(result)

