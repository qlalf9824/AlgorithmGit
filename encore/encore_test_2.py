#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, price, cost):

        result = 0
        compare = 0

        for i in price:
            sell_cost = [j for j in range(len(price)) if price[j] >= i]
            sum = 0
            index = 0
            for j in range(len(sell_cost)):
                if(cost[sell_cost[j]] >= i):
                    break
                sum += cost[sell_cost[j]]
                index = j + 1
            re = index * i - sum
            if(compare < re):
                result = i
                compare = re

        return result

s = Solution()
re = s.solution( [10,10,20,20,5], [1,5,11,15,0])
print(re)