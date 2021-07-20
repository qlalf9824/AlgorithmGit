#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, s):
        result = 0
        copy_s = s

        for i in range(len(s)-1):
            revers_s = copy_s[::-1]
            if(revers_s == copy_s):
                break
            c = s[:i+1]
            copy_s = s + c[::-1]

        return len(copy_s)

s =Solution()
re = s.solution("abacaba")
print(re)