#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, number, dictionary):
        
        result = ""

        dictionary.sort()
        dict_len = [len(i) for i in dictionary]
        
        for i in number:
            if(int(i) in dict_len):
                num = dict_len.index(int(i)) 
                result += dictionary[num] + " "
                dictionary.pop(num)
                dict_len.pop(num)

        return result[:-1]

sol = Solution()
re = sol.solution("31415926",  ["may","i","have","a","large","container","of","coffee"])
print(re)