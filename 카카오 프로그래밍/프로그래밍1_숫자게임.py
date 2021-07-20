def solution(s):
    answer = 0

    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in eng:
        if s.find(i) != -1:
            index = str(eng.index(i))
            s = s.replace(i, index)

    answer = int(s)
    return answer


sol = solution("one4seveneight")
print(sol)